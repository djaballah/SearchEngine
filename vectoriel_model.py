import inverted_index
import operations
from operator import itemgetter
import math


def respond_to_query(query, fun):
    """
    Return a list of document that satisfy the query
    :param query: The query entered by the user
    :type: str
    :return: list of document
    :type; list
    """
    query = operations.tokenizeText(query)
    query = operations.remove_stop_words(query)
    query = operations.remove_punctuation(query)
    #query = operations.stem_tokens(query)
    documets_set = documents_per_query(query)
    res = dict()
    for document in documets_set:
        val = None
        if (fun == 'Inner Product'):
            val = inner_product(query, document)
        if (fun == 'Dice Coefficient'):
            val = dice_coefficient(query, document)
        if (fun == 'Cosinus Measure'):
            val = cosinus_measure(query, document)
        if (fun == 'Jackard Measure'):
            val = jackard_measure(query, document)
        res[document] = val
    sorted_document = sorted(res.items(), key= itemgetter(1), reverse= True)
    return sorted_document

def documents_per_query(query):
    """
    Return a set of all documents containing at least one term of the query
    :param query: The query
    :return: set of documents
    :type: set
    """
    documents = set()
    for term in query:
        doc_list = inverted_index.doc_per_term(term)
        documents.update([item[0] for item in doc_list])
    return documents


def inner_product(query, doc_name):
    """
    Return the inner product between a document and a query
    :param query:The query string
    :type: str
    :param doc_name: the document name
    :type: str
    :return: inner product
    :type: float
    """

    sum_ = 0
    for term in query:
        x = 1
        y = inverted_index.weight(term, doc_name)
        sum_ += x * y

    return sum_

def dice_coefficient(query, doc_name):
    """
    Return Dice coefficient between a document and a query
    :param query:The query string
    :type: str
    :param doc_name: the document name
    :type: str
    :return: inner product
    :type: float
    """
    x_values = [1 for term in query]
    y_values = [pow(inverted_index.weight(term, doc_name), 2) for term in query]
    x_sum = sum(x_values)
    y_sum = sum(y_values)
    coeff = (2 * inner_product(query, doc_name)) / x_sum + y_sum
    return coeff


def cosinus_measure(query, doc_name):
    """
    Return Cosinus measure between a document and a query
    :param query:The query string
    :type: str
    :param doc_name: the document name
    :type: str
    :return: inner product
    :type: float
    """
    x_values = [1 for term in query]
    y_values = [pow(inverted_index.weight(term, doc_name), 2) for term in query]
    x_sum = sum(x_values)
    y_sum = sum(y_values)
    measure = inner_product(query, doc_name) / math.sqrt(x_sum * y_sum)
    return measure

def jackard_measure(query, doc_name):
    """
    Return jackard measure between a document and a query
    :param query:The query string
    :type: str
    :param doc_name: the document name
    :type: str
    :return: inner product
    :type: float
    """
    x_values = [1 for term in query]
    y_values = [pow(inverted_index.weight(term, doc_name), 2) for term in query]
    x_sum = sum(x_values)
    y_sum = sum(y_values)
    measure = inner_product(query, doc_name) / (x_sum + y_sum - inner_product(query, doc_name))
    return measure

if __name__ == '__main__':
    doc = respond_to_query("artificial  intelligence machine learning learn")
    print(doc)