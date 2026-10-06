# Upsert Resolver Redirect

## Usage

From the Upsert Resolver Redirect [workflow overview](https://github.com/caltechlibrary/upsert-resolver-redirect/actions/workflows/upsert.yml) page press the **Run workflow** dropdown button. In the form enter the required Resolver Key and Redirect URL. Then press the green **Run workflow** submit button.

### Example Use Case

We want the resolver entry at *https://resolver.caltech.edu/CaltechOH:OH_Brooks_N* to redirect to the current *https://digital.archives.caltech.edu/collections/OralHistories/OH_Brooks_N/* URL instead of the legacy *https://oralhistories.library.caltech.edu/306/* EPrints URL.

Enter values in the following manner:

- Resolver Key: **CaltechOH:OH_Brooks_N**
- Redirect URL: **https://digital.archives.caltech.edu/collections/OralHistories/OH_Brooks_N/**

In this case, the existing resolver entry will be updated. If the resolver entry did not exist, it would be created.

## Bulk Redirects From a CaltechAUTHORS Search

The [Upsert Resolver Redirects From Search](https://github.com/caltechlibrary/upsert-resolver-redirect/actions/workflows/upsert-from-search.yml) workflow takes a CaltechAUTHORS search URL (copied from the browser), fetches the matching records from the API, and for every record with a `resolverid` identifier points that resolver key at the record's CaltechAUTHORS URL.

- Search URL: **https://authors.library.caltech.edu/search?q=metadata.creators.person_or_org.identifiers.identifier%3A%22Katz-J-N%22**
- Dry run: leave checked to only list the redirects in the job log; uncheck to update them.

Only the search query (`q`) is used, and it is always run across all record versions. Only identifiers with the `resolverid` scheme are updated. Resolver keys that appear on more than one record are skipped and listed in the job log so they can be handled separately.
