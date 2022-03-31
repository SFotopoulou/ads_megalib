# Intented usage: use keywords to filter paper selection, e.g. in Zotero
# Each bibcode will be saved once in one large library.
# Add keyword with library name and optional prefix per paper to retain library categorisation in ADS
import os
import math
import requests
import json
from ads_lib import get_library, fix_authornames
from ads_lib import fix_journal_abbr
from ads_lib import add_keyword_tag,sanitise_multi

######### Parameters #########
export_filename = 'WP9-AGN-changing_look.bib'
export_format = 'bibtex'
# leave empty to export all your libraries
# or use comma-separated names of your libraries
library_name = 'AGN,Coevolution'
bibtex_keyformat = "%1H%R"
sort_format = "first_author asc"
# Use short or long journal names instead of journal TeX abbreviations; \aj
fix_journal = True
add_keyword = True
######################################

# Connect to ADS
t = json.load(open('mysecrets'))
my_token = t['my_token']
base_url = "https://api.adsabs.harvard.edu/v1/biblib"
headers = {'Authorization': "Bearer " + my_token,
           "Content-type": "application/json"}

# Find all your libraries
r = requests.get(base_url+"/libraries",
                 headers=headers)
all_libraries = r.json()['libraries']

if library_name == '':
    my_libraries = all_libraries
else:
    libs = library_name.split(',')
    lib_list = [l.lower() for l in libs]
    my_libraries = []
    my_libraries = [
        lib for lib in all_libraries if lib['name'].lower() in lib_list]

print("Exporting from {} libraries".format(str(len(my_libraries))))

# Get bibcodes for each library

config = {}
config['headers'] = headers
config['url'] = base_url


fout = open(export_filename, 'w')

megalib = []
for library in my_libraries:
    lib_name = library['name'].replace(' ', '-')

    # get bibcodes
    my_bibs = get_library(library['id'], library['num_documents'], config)
    #
    print(f"{lib_name} has {len(my_bibs)} bibcodes")

    export_url = "https://api.adsabs.harvard.edu/v1/export/"+export_format
    #
    start = 0
    rows = 2000
    num_paginates = int(math.ceil(len(my_bibs) / (1.0*rows)))
    #
    s1 = start
    s2 = rows
    #
    for i in range(num_paginates):
        #
        querystring = {"bibcode": my_bibs[s1:s2],
                       "keyformat": bibtex_keyformat,
                       "sort": sort_format}
        #
        response = requests.request("POST",
                                    export_url,
                                    headers=headers,
                                    data=json.dumps(querystring))
        #
        expbib = fix_authornames(response.json()['export'])
        #
        if fix_journal == True:
            expbib = fix_journal_abbr(expbib, format='short')
        #
        if add_keyword == True:
            expbib = add_keyword_tag(expbib, tag=f'ADS:{lib_name}')
        #   
        megalib.append( expbib )
        #
        s1 = s1 + rows
        s2 = s2 + rows
        #
# sanitise multiple occurencies; merge keywords

final_lib = sanitise_multi(megalib)

print(f"Total {final_lib.count('@')} unique bibcodes")
print(f"Output in {export_filename}")
fout.write(final_lib)
fout.close()
print(response)
