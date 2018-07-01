import nltk.tokenize
from nltk.corpus import stopwords
import string

def tokenizeText(text):
    """
    Tokenize text and return a list of tokens

    :param text: Text to tokenize
    :type String
    :return: list of tokens
    """
    assert isinstance(text, str)
    from nltk.tokenize import WordPunctTokenizer
    word_punct_tokenizer = WordPunctTokenizer()
    tokens_list = word_punct_tokenizer.tokenize(text)
    #tokens_list = nltk.tokenize.word_tokenize(text)
    return tokens_list

def read_file(file_name):
    """
    Open a text file and return the a lower case version of the text it's containing

    :param file_name: The file name
    :type String
    :return: The text conatained in the file
    :type String
    """
    assert isinstance(file_name, str)
    with open(file_name) as f:
        text = f.read()
        return text.lower()

def remove_stop_words(tokens_list):
    """
    Remove stop words from a list of tokens and return a new list without stop words
    :param tokens_list: List of tokens
    :type list
    :return: list
    """

    assert isinstance(tokens_list, list)
    stop_words = set(stopwords.words('english'))
    #stop_words = ['La','la','d','est','un','qui','de','faire','pour','selon','son','en','il','sur','ou','des','entre','et','une','du']
    filtered_tokens = [token for token in tokens_list if token not in stop_words] #A list of tokens without the stop words
    return filtered_tokens

def stem_tokens(token_list):
    """
    Return a list of stem of the tokens in token_list
    :param token_list: list of token
    :type list
    :return: list of stems
    :type list
    """

    assert isinstance(token_list, list)
    porter_stemmer = nltk.PorterStemmer()
    stem_list = [porter_stemmer.stem(token) for token in token_list]
    return stem_list

def remove_punctuation(token_list):
    """
    Remove punctuation token from a list of token
    :param token_list: list of tokens
    :type list
    :return:tokens list withoud token punctuation
    :type list
    """
    assert isinstance(token_list, list)
    punctuation_set = set(string.punctuation)
    filtered_list = [token for token in token_list if token not in punctuation_set]
    return filtered_list


if __name__ == '__main__':
    pass



