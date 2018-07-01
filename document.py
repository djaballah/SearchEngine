import nltk.tokenize
from nltk.corpus import stopwords
import collections
import string

class Document:
    """
    A class for representing a document
    """

    def __init__(self, document_name):
        """
        crate an Object document representing the document
        :param document_name: document name
        :type str
        """
        assert isinstance(document_name, str)
        text = self._read_file(document_name)
        tokens_list = self._tokenizeText(text)
        print(text)
        print(tokens_list)
        filtered_tokens_list = self._remove_stop_words(tokens_list)
        filtered_tokens_list = self._remove_punctuation(filtered_tokens_list)

        stems_list = filtered_tokens_list
        #stems_list = self._stem_tokens(filtered_tokens_list)
        self._number_of_stems = len(stems_list)
        self._index =  self._construct_index(stems_list)
        self._name = self._set_documen_name(document_name)



    def _tokenizeText(self, text):
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
        #tokens_list = nltk.tokenize.word_tokenize(text, language='french')
        return tokens_list

    def _read_file(self, file_name):
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

    def _remove_stop_words(self, tokens_list):
        """
        Remove stop words from a list of tokens and return a new list without stop words
        :param tokens_list: List of tokens
        :type list
        :return: list
        """

        assert isinstance(tokens_list, list)
        #stop_words = set(stopwords.words('english'))
        stop_words = ['La','la','d','est','un','qui','de','faire','pour','selon','son','en','il','sur','ou','des','entre','et','une','du']
        filtered_tokens = [token for token in tokens_list if
                           token not in stop_words]  # A list of tokens without the stop words
        return filtered_tokens

    def _remove_punctuation(self, token_list):
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

    def _stem_tokens(self, token_list):
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

    def _construct_index(self, stem_list):
        """
        Return an index of stems in list
        :param stem_list: list of stems
        :type list
        :return: index of stems
        :type dict
        """
        assert isinstance(stem_list, list)
        key_set = set(key for key in "0123456789abcdefghijklmnopqrstuvwxyz")
        d = {key: [] for key in key_set}
        index = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
        for stem in stem_list:
            first_caracter = stem[0]
            if first_caracter in key_set:
                index[first_caracter].append(stem)
        return index

    def getIndex(self):
        """
        Return the index
        :return: index
        :type OrderedDict
        """
        return self._index

    def getLength(self):
        """
        Return the length of the document
        :return: self._number_of_stems
        :type int
        """
        return  self._number_of_stems

    def getDocumentName(self):
        """
        Return the name of the indexed document
        :return: name of the indexed document
        :type str
        """
        return self._name

    def _set_documen_name(self, document_path):
        """
        Return the document name without the pat
        :param document_path: The document path
        :return: document name
        """
        assert isinstance(document_path, str)
        l = document_path.split("/")
        return l[-1]

    def get_max_freq(self):
        """
        Return the frequence of the most occured term
        :return: frequence
        :type: int
        """
        index = self.getIndex()
        maximum = 0
        for key, val in index.items():
            for item in val:
                count = 0
                for element in val:
                    if item == element:
                        count += 1
                if (count > maximum):
                    maximum = count
        return maximum

    
