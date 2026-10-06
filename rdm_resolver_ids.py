"""Print "<resolver key>\t<record url>" for every record matching an RDM search URL.

Usage: python rdm_resolver_ids.py "https://authors.library.caltech.edu/search?q=..."
"""

import json
import re
import sys
import urllib.parse
import urllib.request

USER_AGENT = "caltechlibrary/upsert-resolver-redirect"
KEY_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:._-]*$")


def api_url(search_url):
    parsed = urllib.parse.urlparse(search_url)
    query = urllib.parse.parse_qs(parsed.query).get("q", [""])[0]
    params = urllib.parse.urlencode(
        {"q": query, "allversions": "true", "size": 100, "page": 1}
    )
    return f"{parsed.scheme}://{parsed.netloc}/api/records?{params}"


def main(search_url):
    url = api_url(search_url)
    seen = {}
    duplicates = set()
    while url:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request) as response:
            data = json.load(response)
        for record in data["hits"]["hits"]:
            for identifier in record["metadata"].get("identifiers", []):
                if identifier.get("scheme") != "resolverid":
                    continue
                key = identifier["identifier"].strip()
                if not KEY_PATTERN.match(key):
                    print(f"Skipping invalid resolver key {key!r}", file=sys.stderr)
                    continue
                target = record["links"]["self_html"]
                if key in seen and seen[key] != target:
                    duplicates.add(key)
                seen.setdefault(key, target)
        url = data["links"].get("next")
    # Keys shared by multiple records are handled by a separate process
    for key in sorted(duplicates):
        print(f"Skipping duplicate resolver key {key}", file=sys.stderr)
    for key, target in seen.items():
        if key not in duplicates:
            print(f"{key}\t{target}")


if __name__ == "__main__":
    main(sys.argv[1])
