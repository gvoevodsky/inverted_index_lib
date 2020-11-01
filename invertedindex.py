import json
import re
import codecs


class InvertedIndex:

    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def query(self, words: list) -> list:
        """Return the list of relevant documents for the given query"""
        if len(words) < 1: #check for empty data
            print('No arguments')
            return None

        for word in words: #check for data == str
            if word is not str:
                print('One of the input words is not int')
                return None

        lowercase_words = [x.lower() for x in words] #fast check for missing word
        for word in lowercase_words:
            if word in self.inverted_index.keys():
                pass
            else:
                print(f'No matching results for {word}')
                return None

        set_of_indexes = set(self.inverted_index[lowercase_words[0]])
        for word in lowercase_words:
            set_of_indexes.intersection_update(set(self.inverted_index[word]))
        list_of_indexes = sorted(list(set_of_indexes))
        return list_of_indexes

    def dump(self, filepath: str):  # сохранить инвертированный индекс на диск
        file = open(filepath, "w")
        file.write(json.dumps(self.inverted_index))
        file.close()

    @classmethod
    def load(cls, filepath: str):  # загрузить инвертированный индекс с диска
        file = open(filepath, "r")
        text = file.read()
        dictionary = json.loads(text)
        inverted_index = cls(dictionary)
        return inverted_index


def load_documents(filepath: str):  # загрузить файл в переменную
    file = codecs.open(filepath, "r", "utf_8_sig")  # может стоить поменять на библиотеку io
    text = file.read()
    file.close()
    return text


def build_inverted_index(documents):  # построить инвертированный индекс из документа (должен return InvertedIndex())
    list_of_articles = documents.split('\n')  # список всех статей
    all_unique_words = set()
    article_id_to_list_of_words_in_article = {}  # словарь {id статьи : множество слов в статье}
    for article in list_of_articles:
        list_of_words = re.sub(r'\W', ' ', article, flags=re.I).split()
        lowercase_list_of_words = [x.lower() for x in list_of_words]
        set_of_words = set(lowercase_list_of_words)
        all_unique_words.update(set_of_words)
        if len(lowercase_list_of_words) > 1:
            article_id_to_list_of_words_in_article[list_of_words[0]] = set_of_words
    print('\nSet of words and {article ID : Set of words in article} formed\n')

    inverted_index = {}
    for key, value in article_id_to_list_of_words_in_article.items():
        for word in all_unique_words:
            if word in value:
                if word not in inverted_index.keys():
                    inverted_index[word] = [key]
                else:
                    inverted_index[word].append(key)
            else:
                pass
        print('building on article: ', key)

    return InvertedIndex(inverted_index)


def main():
    documents = load_documents("C:\\Users\\User\\PycharmProjects\\inverted_index_lib\\test_data")
    inverted_index = build_inverted_index(documents)
    inverted_index.dump("inverted.index")
    inverted_index = InvertedIndex.load("inverted.index")
    document_ids = inverted_index.query(['two', 'words'])
    print(document_ids)


if __name__ == "__main__":
    main()
