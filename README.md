# ads_megalib
Merge all ADS libraries into one

`ads_megalib.py` creates a library on your ADS account that is the union of all of your libraries.

`ads_exportlib.py` exports all or some of your libraries into a single local file.

**Usage**

In the same folder as the scripts, create a file called `mysecrets` and store your ADS API token.
The file `example_mysecrets` shows the expected format.

The code will use your token and fetch your library information.

**Megalib parameters**

At the top of the script you can adjust the name and description of the new library.

`mega_lib_name = 'MEGALIB'`

`mega_lib_description = "Union of all libraries"`


**Exportlib parameters**

At the top of the script you can choose:

the exported filename (overwritten if exists):

`export_filename = 'export_bib.bib'`

the [output format](http://adsabs.github.io/help/actions/export):

`export_format = 'bibtex'`

which libraries to export. Leave empty to export all your libraries or use comma-separated names of your libraries:

`library_name = ''`

the [keyword format](http://adsabs.github.io/help/actions/export):

`bibtex_keyformat = "%1H%R"`

and finally the [sorting of your references:](http://adsabs.github.io/help/actions/sort)

`sort_format = "first_author asc"`

