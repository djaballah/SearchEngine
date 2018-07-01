import document
import collections
import json
from os import listdir
from os.path import isfile, join
import math

inverted_index_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/inverted_index"
collection_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/collection"


def construct_index(document):
    """
    Construct te inverted index of document
    :param document:
    :return:
    """
    # assert isinstance(document, document.Document)
    inverted_index_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/inverted_index"
    files = set(
        join(inverted_index_path, f) for f in listdir(inverted_index_path)
                                            if isfile(join(inverted_index_path, f)))
    print(files)
    doc_index = document.getIndex()
    for key in doc_index.keys():
        file_name = join(inverted_index_path, key + ".json")
        existing_inverted_index = {}
        if (file_name in files):
            with open(file_name, "r") as existing_inverted_index_file:
                existing_inverted_index = json.load(existing_inverted_index_file)
                # print(existing_inverted_index['artifici'])
        else:
            with open(file_name, "w") as existing_inverted_index_file:
                pass

        terms = doc_index[key]
        print('{}: {}'.format(key, terms))
        counter = collections.Counter(terms)
        for term in set(terms):
            if (term in set(existing_inverted_index.keys())):
                existing_elemnts = set(item[0] for item in existing_inverted_index[term])
                if (document.getDocumentName() not in existing_elemnts):
                    existing_inverted_index[term].append((document.getDocumentName(),
                                                          counter[term]))
            else:
                existing_inverted_index[term] = [(document.getDocumentName(), counter[term])]
        with open(file_name, "w") as jsonFile:
            json.dump(existing_inverted_index, jsonFile)


def load_inverted_index(file_name):
    """
    Load the inverted index in memory
    :return:
    """
    inverted_index_path = "/media/djaballah/54523AA71752BD7A/SII/S3/RI/Tp/RiProject/inverted_index"
    files = set(
                join(inverted_index_path, f) for f in listdir(inverted_index_path)
                        if isfile(join(inverted_index_path, f)))
    file_name = join(inverted_index_path, file_name)
    if (file_name not in files):
        pass
        # Error
    else:
        with open(file_name, 'r') as fp:
            index = json.load(fp)
            return index


def term_per_document(doc_name):
    """
    Return the document terme's
    :param doc_name: name of the document
    :type: str
    :return: list of term
    :type: list
    """
    assert isinstance(doc_name, str)
    doc_terms = []
    files = set(
        join(inverted_index_path, f) for f in listdir(inverted_index_path)
                                    if isfile(join(inverted_index_path, f)))
    for file in files:
        index = load_inverted_index(file)
        for key, val in index.items():
            for doc in val:
                if doc[0] == doc_name:
                    doc_terms.append((key, doc[1]))
    return doc_terms


def doc_per_term(term):
    """
    Return a list of docuents that contain the term term
    :param term: a term
    :type: str
    :return: list of document
    :type: list
    """
    assert isinstance(term, str)
    print(term)
    inverted_index_name = term[0] + ".json"
    inverted_index_name = join(inverted_index_path, inverted_index_name)
    index = load_inverted_index(inverted_index_name)
    doc_list = []
    try:
        doc_list = index[term]
    except (KeyError, TypeError):
        print('---------')
        pass
    return doc_list


def frequence(term, doc_name):
    """
    Return the freuence of terme in doc_name
    :param term: a term to look for it's frequence
    :type: str
    :param doc_name: a document name
    :type: str
    :return: frequence of term in doc_name
    :type: integer
    """
    assert isinstance(term, str)
    assert isinstance(doc_name, str)
    freq = 0
    doc_contain_term = doc_per_term(term)
    for item in doc_contain_term:
        if item[0] == doc_name:
            freq = int(item[1])
    return freq


def max_freq(doc_name):
    """
    Return the frequence of the most occured term in doc_name
    :param doc_name: the document name
    :type: str
    :return: the maximum frequence
    :type: int
    """
    assert isinstance(doc_name, str)
    doc = document.Document(join(collection_path, doc_name))
    maximum = doc.get_max_freq()
    return maximum


def num_of_doc_per_term(term):
    """
    Return the number of documents containing the term term
    :param term: a term
    :type: str
    :return: number of documents containing the term term
    :type: int
    """
    assert isinstance(term, str)
    doc_list = doc_per_term(term)
    return len(doc_list)


def number_document_in_collection():
    """
    Return the number of document in the collection
    :return: number of document in the collection
    :type: int
    """
    doc_list = listdir(collection_path)
    return len(doc_list)


def weight(term, doc_name):
    """
    Return the weight of a term contained in a document
    :param term: The term we are looking for it's weight
    :type: str
    :param doc_name: the document name we're looking for the terme in it
    :type: str
    :return: the weight
    :type: float
    """
    assert isinstance(term, str)
    assert isinstance(doc_name, str)
    N = number_document_in_collection()
    ni = num_of_doc_per_term(term)

    try:
        weigh = (frequence(term, doc_name) / max_freq(doc_name)) * math.log10((N / ni) + 1)
    except ZeroDivisionError:
        weigh = 0
    return weigh

# if __name__ == '__main__':
# print(weight('artificial', 'test.txt'))
