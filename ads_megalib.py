import requests
import json
from ads_lib import get_library


######### Parameters #########
mega_lib_name = 'MEGALIB'
mega_lib_description = "Union of all libraries"
######################################

t = json.load(open('mysecrets'))
my_token = t['my_token']
base_url = "https://api.adsabs.harvard.edu/v1/biblib"
headers = {'Authorization': "Bearer " + my_token,
           "Content-type": "application/json"}
######################################

# Get all your libraries
r = requests.get(base_url+"/libraries",
                 headers=headers)
my_libraries = r.json()['libraries']
print("Merging {} libraries".format(str(len(my_libraries))))

# Get bibcodes for each library
# check if mega_lib_name exists
bibs = []
config = {}

config['headers'] = headers
config['url'] = base_url

mega_lib_id = 0

for library in my_libraries:

    bib = get_library(library['id'], library['num_documents'], config)

    bibs.extend(bib)

    if library['name'] == mega_lib_name:
        mega_lib_id = library['id']

# Keep unique bibcodes
my_bibs = list(set(bibs))
print("Found {} unique bibcodes".format(len(my_bibs)))


if mega_lib_id == 0:
    # If mega_lib_name exists, append to library, if not create it.
    url = base_url+"/libraries"

    querystring = {"name": mega_lib_name,
                   "description": mega_lib_description,
                   "bibcode": my_bibs}

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=json.dumps(querystring))

    print(response)

else:
    # If mega_lib_name exists, append to library, if not create it.
    url = base_url+"/documents/"+mega_lib_id

    querystring = {"name": mega_lib_name,
                   "action": "add",
                   "bibcode": my_bibs}

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=json.dumps(querystring))

    print(response)
