import pytest
import invertedindex


class TestClass1:
    def test_1(self):
        documents = invertedindex.load_documents('C:\\Users\\User\\PycharmProjects\\inverted_index_lib\\test_data')
        inverted_index = invertedindex.build_inverted_index(documents)
