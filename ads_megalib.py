import requests
import json
from ads_lib import get_library

t = json.load(open('mysecrets'))
my_token = t['my_token']
mega_lib_name = 'MEGALIB'

# Get all your libraries
r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries",
                 headers={"Authorization": "Bearer " + my_token})
my_libraries = r.json()['libraries']
print("Merging {} libraries".format(str(len(my_libraries))))

# Get bibcodes for each library
# check if mega_lib_name exists
bibs = []
config = {}
mega_lib_id = 0

for library in my_libraries:

    #    r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/" + library['id'],
    #                     headers={"Authorization": "Bearer " + my_token})

    config['headers'] = {"Authorization": "Bearer " + my_token,
                         'Content-Type': 'application/json'}
    config['url'] = "https://api.adsabs.harvard.edu/v1/biblib"

    bib = get_library(library['id'], library['num_documents'], config)

    bibs.extend(bib)

    if library['name'] == mega_lib_name:
        mega_lib_id = library['id']

print("Found {} unique bibcodes".format(len(bibs)))

# TODO: script works but run limit of 100 pages (2525 papers)

# Keep unique bibcodes
my_bibs = list(set(bibs))

if mega_lib_id == 0:
    # If mega_lib_name exists, append to library, if not create it.
    url = "https://api.adsabs.harvard.edu/v1/biblib/libraries"

    querystring = {"name": mega_lib_name,
                   "description": "Union of all libraries",
                   "bibcode": my_bibs}

    headers = {'Authorization': "Bearer " + my_token,
               "Content-type": "application/json"}

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=json.dumps(querystring))

    print(response)

else:
    print(mega_lib_id)
    # If mega_lib_name exists, append to library, if not create it.
    url = "https://api.adsabs.harvard.edu/v1/biblib/documents/"+mega_lib_id

    querystring = {"name": mega_lib_name,
                   "action": "add",
                   "bibcode": my_bibs}

    headers = {'Authorization': "Bearer " + my_token,
               "Content-type": "application/json"}

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=json.dumps(querystring))

    print(response)
