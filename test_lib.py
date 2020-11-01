import pytest
import invertedindex


@pytest.fixture(scope="session")
def inverted_index():
    path = 'C:\\Users\\User\\PycharmProjects\\inverted_index_lib\\wikipedia_sample'  # change for linux?
    documents = invertedindex.load_documents(path)
    inverted_index = invertedindex.build_inverted_index(documents)
    inverted_index.dump('pytest_invertedindex')
    print(type(inverted_index))
    return inverted_index


class TestClass1:

    @pytest.mark.xfail
    def test_wrong_filepath_to_dump(self, inverted_index):
        inverted_index.dump('')

    @pytest.mark.xfail
    def test_wrong_filepath_to_load(self, inverted_index):
        inverted_index.load('unexistent_file')

    def test_for_empty_file(self, inverted_index):
        inverted_index.query(['a'])

    def test_for_non_existent_word(self, inverted_index):
        result = inverted_index.query(['qweqqwerqwersadfsavdsfhqwertfggvqerg'])
        assert result is None

    def test_for_empty_word(self, inverted_index):
        result = inverted_index.query(['', ' '])
        assert result is None

    def test_for_uppercase(self, inverted_index):
        result = inverted_index.query(['abracadabra'])
        result_2 = inverted_index.query(['Abracadabra'])
        assert result == result_2
