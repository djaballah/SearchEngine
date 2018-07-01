
def nb_pertinent_retrived_doc(retrieved_documents, pertinent_document):
    """
    Return the number of pertinent retrieved document
    :param retrieved_documents: List of retrived documents returned by the system
    :type: list
    :param pertinent_document: List of Selected pertinent document by the user
    :type: list
    :return: The number of pertinent document retrieved by the system
    :type: int
    """

    nb = 0
    pertinent_document = set(pertinent_document)
    for doc in retrieved_documents:
        if doc in pertinent_document:
            nb += 1

    return nb

def rappel(nb_pertinent_retrieved_doc, nb_total_pertinent_doc):
    """
    Return The rappel value
    :param nb_pertinent_retrieved_doc: The number Of pertinent retrieved document returned by the system
    :type: list
    :param nb_total_pertinent_doc: The number of total pertinent document selected by the user
    :type: list
    :return: The rappel value
    :type: float
    """
    return nb_pertinent_retrieved_doc / nb_total_pertinent_doc

def precision(nb_pertinent_retrieved_doc, nb_total_retrieved_doc):
    """
    Return The precision value
    :param nb_pertinent_retrieved_doc: The number Of pertinent retrieved document returned by the system
    :type: list
    :param nb_total_pertinent_doc: The number of total document returned by the system
    :type: list
    :return: The precision value
    :type: float
    """
    return nb_pertinent_retrieved_doc / nb_total_retrieved_doc
