# Upsert Resolver Redirect

## Usage

From the Upsert Resolver Redirect [workflow overview](https://github.com/caltechlibrary/upsert-resolver-redirect/actions/workflows/upsert.yml) page press the **Run workflow** dropdown button. In the form enter the required Resolver Key and Redirect URL. Then press the green **Run workflow** submit button.

### Example Use Case

We want the resolver entry at *https://resolver.caltech.edu/CaltechOH:OH_Brooks_N* to redirect to the current *https://digital.archives.caltech.edu/collections/OralHistories/OH_Brooks_N/* URL instead of the legacy *https://oralhistories.library.caltech.edu/306/* EPrints URL.

Enter values in the following manner:

- Resolver Key: **CaltechOH:OH_Brooks_N**
- Redirect URL: **https://digital.archives.caltech.edu/collections/OralHistories/OH_Brooks_N/**

In this case, the existing resolver entry will be updated. If the resolver entry did not exist, it would be created.
