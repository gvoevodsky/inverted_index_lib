import json
import re
import codecs


class InvertedIndex:

    def __init__(self):
        pass  # TODO ??

    def query(self, words: list) -> list:  # принимает список слов и возвращает ID подходящих документов
        """Return the list of relevant documents for the given query"""
        pass

    def dump(self, filepath: str):  # сохранить инвертированный индекс на диск
        pass

    @classmethod
    def load(cls, filepath: str):  # загрузить инвертированный индекс с диска
        pass


def load_documents(filepath: str):  # загрузить файл в переменную
    file = codecs.open(filepath, "r", "utf_8_sig")  # может стоить поменять на библиотеку io
    text = file.read()  # или читайте по строке
    file.close()
    return text


def build_inverted_index(documents):  # построить инвертированный индекс из документа (должен return InvertedIndex())

    # wordList = re.sub("[^\w]", " ", documents).split()
    # all_unique_words = set(wordList)  # множество всех возможных слов
    # list_of_articles = documents.split('\n')  # список всех статей
    #
    # article_id_to_list_of_words_in_article = {}  # словарь {id статьи : список слов в статье}
    # for article in list_of_articles:
    #    list_of_words = re.sub("[^\w]", " ", article).split()
    #    if len(list_of_words) > 1:
    #        article_id_to_list_of_words_in_article[list_of_words[0]] = list_of_words
    #
    # inverted_index = {}
    #
    # for word in all_unique_words:
    #    for key, value in article_id_to_list_of_words_in_article.items():
    #        if word in value:
    #            if word not in inverted_index.keys():
    #                inverted_index[word] = [key]
    #            else:
    #                inverted_index[word].append(key)
    #        else:
    #            pass
    #    print(word)
    #
    list_of_articles = documents.split('\n')  # список всех статей TODO альтернативный обход
    all_unique_words = set()
    article_id_to_list_of_words_in_article = {}  # словарь {id статьи : список слов в статье}
    for article in list_of_articles:
        list_of_words = re.sub("[^\w]", " ", article).split()
        set_of_words = set(list_of_words)
        all_unique_words.update(set_of_words)
        if len(list_of_words) > 1:
            article_id_to_list_of_words_in_article[list_of_words[0]] = list_of_words

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
        print(key)

    print(inverted_index)

    return InvertedIndex()







def main():
    documents = load_documents("C:\\Users\\User\\PycharmProjects\\inverted_index_lib\\wikipedia_sample")
    inverted_index = build_inverted_index(documents)
    # inverted_index.dump("/path/to/inverted.index")
    # inverted_index = InvertedIndex.load("/path/to/inverted.index")
    # document_ids = inverted_index.query(["two", "words"])


if __name__ == "__main__":
    main()
