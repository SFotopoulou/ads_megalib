import math
import requests
# https://github.com/adsabs/ads-examples/blob/master/library_csv/lib_2_csv.py


def get_library(library_id, num_documents, config):
    """
    Get the content of a library when you know its id. As we paginate the
    requests from the private library end point for document retrieval,
    we have to repeat requests until we have all documents.
    :param library_id: identifier of the library
    :type library_id:
    :param num_documents: number of documents in the library
    :type num_documents: int
    :return: list
    """

    start = 0
    rows = 25
    num_paginates = int(math.ceil(num_documents / (1.0*rows)))
    documents = []
    for i in range(num_paginates):
        print('Pagination {} out of {}'.format(i+1, num_paginates))

        r = requests.get(
            '{}/libraries/{id}?start={start}&rows={rows}'.format(
                config['url'],
                id=library_id,
                start=start,
                rows=rows
            ),
            headers=config['headers']
        )

        # Get all the documents that are inside the library
        try:
            data = r.json()['documents']
        except ValueError:
            raise ValueError(r.text)

        documents.extend(data)

        start += rows

    return documents
