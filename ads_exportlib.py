import os
import math
import requests
import json
from ads_lib import get_library

######### Parameters #########
t = json.load(open('mysecrets'))
my_token = t['my_token']
export_filename = 'export_bib.bib'
export_format = 'bibtex'
# leave empty to export all your libraries
# or use comma-separated names of your libraries
library_name = ''
bibtex_keyformat = "%1H%R"
sort_format = "first_author asc"
#
base_url = "https://api.adsabs.harvard.edu/v1/biblib"
headers = {'Authorization': "Bearer " + my_token,
           "Content-type": "application/json"}
######################################

# Finds all your libraries
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
bibs = []
config = {}
config['headers'] = headers
config['url'] = base_url

for library in my_libraries:

    bib = get_library(library['id'], library['num_documents'], config)

    bibs.extend(bib)

# Keep unique bibcodes
my_bibs = list(set(bibs))
print("Found {} unique bibcodes".format(len(my_bibs)))
# Export in bibtex
try:
    os.remove(export_filename)
except OSError:
    pass

export_url = "https://api.adsabs.harvard.edu/v1/export/"+export_format


start = 0
rows = 2000
num_paginates = int(math.ceil(len(my_bibs) / (1.0*rows)))

s1 = start
s2 = rows

for i in range(num_paginates):

    querystring = {"bibcode": my_bibs[s1:s2],
                   "keyformat": bibtex_keyformat,
                   "sort": sort_format}

    response = requests.request("POST",
                                export_url,
                                headers=headers,
                                data=json.dumps(querystring))

    print(response)
    fout = open(export_filename, 'a')
    fout.write(response.json()['export'])

    s1 = s1 + rows
    s2 = s2 + rows

fout.close()
