import document
import inverted_index
import json
from os import listdir
from os.path import join
import pprint as pp
import boolean_model


if __name__ == '__main__':

    #collection_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/collection"
    #collection = [f for f in listdir(collection_path)]
    #for document_name in collection:
        #print(document_name)
        #doc = document.Document(join(collection_path, document_name))
        #inverted_index.construct_index(doc)
    #index = inverted_index.load_inverted_index("l.json")
    #pp.pprint(index)
    doc_terms = boolean_model.respond_to_query('decomposit or draw')
    print(doc_terms)
