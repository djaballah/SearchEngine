import inverted_index
import operations

operators = set(["and", "or", "(", ")", "not"])

def respond_to_query(query):
    """
    Return a list of document that satisfy the query
    :param query: The query entered by the user
    :type: str
    :return: list of document
    :type; list
    """
    assert isinstance(query, str)
    #terms_list = query.split(' ')
    terms_list = operations.tokenizeText(query)
    terms_list = operations.remove_stop_words(terms_list)
    terms_list = operations.remove_punctuation(terms_list)
    #terms_list = operations.stem_tokens(terms_list)
    #print(terms_list)
    index = dict()
    documents = set()
    for term in terms_list:
        if term not in operators:
            try:
                index[term] = inverted_index.doc_per_term(term)
                documents.update(item[0] for item in index[term])
            except KeyError:
                index[term] = []
    doc_list = []   #List of document that satisfy the query
    for document in documents:
        reformulated_query = ""
        for term in terms_list:
            if term not in operators:
                if document in [item[0] for item in index[term]]:
                    reformulated_query += "1 "
                else:
                    reformulated_query += "0 "
            else:
                reformulated_query += term + " "
        print(reformulated_query)
        if (eval(reformulated_query)):
            doc_list.append(document)

    return doc_list
