import requests
import json
from ads_lib import get_library

# Parameters
t = json.load(open('mysecrets'))
my_token = t['my_token']
export_format = 'bibtex'
# leave empty to export all your libraries
# or use comma-separated names of your libraries
library_name = 'AGN,2.Identification,machine learning'
bibtex_keyformat = "%1H%R"
sort_format = "first_author asc"
##

# Finds all your libraries
r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries",
                 headers={"Authorization": "Bearer " + my_token})
all_libraries = r.json()['libraries']

if library_name == '':
    my_libraries = all_libraries
else:
    libs = library_name.split(',')
    lib_list = [l.lower() for l in libs]
    my_libraries = []
    my_libraries = [
        lib for lib in all_libraries if lib['name'].lower() in lib_list]
print(my_libraries)
print("Exporting from {} libraries".format(str(len(my_libraries))))

# Get bibcodes for each library
bibs = []
config = {}
for library in my_libraries:

    # r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/" + library['id'],
    #                 headers={"Authorization": "Bearer " + my_token})

    config['headers'] = {"Authorization": "Bearer " + my_token,
                         'Content-Type': 'application/json'}
    config['url'] = "https://api.adsabs.harvard.edu/v1/biblib"

    bib = get_library(library['id'], library['num_documents'], config)

    bibs.append(bib)

# Keep unique bibcodes
#print(bibs)
my_bibs = list(set(bibs))
print("Found {} unique bibcodes".format(len(my_bibs)))

# Export in bibtex
url = "https://api.adsabs.harvard.edu/v1/export/"+export_format

querystring = {"bibcode": my_bibs,
               "keyformat": bibtex_keyformat,
               "sort": sort_format}

headers = {'Authorization': "Bearer " + my_token,
           "Content-type": "application/json"}

response = requests.request("POST",
                            url,
                            headers=headers,
                            data=json.dumps(querystring))

print(response)
fout = open('export_bib.bib', 'w')
fout.write(response.json()['export'])
fout.close()
