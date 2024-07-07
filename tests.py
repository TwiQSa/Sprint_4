import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_any_genre_from_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

    def test_get_book_genre_from_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

    @pytest.mark.parametrize('book_genre, book_name', [['Ужасы','Тёмная Башня'], ['Ужасы','Сияние']])
    def test_get_books_with_specific_genre_horror(self, book_genre, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_with_specific_genre(book_genre) == [book_name]

    @pytest.mark.parametrize('book_genre, book_name', [['Ужасы', 'Тёмная Башня'], ['Фантастика', 'Гарри Поттер и философский камень']])
    def test_get_books_with_genre_list_of_books_and_genres(self, book_genre, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == {book_name: book_genre}

    def test_get_books_for_children_with_horror_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Тёмная Башня')
        collector.set_book_genre('Тёмная Башня', 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_cartoons_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка о рыбаке и рыбке')
        collector.set_book_genre('Сказка о рыбаке и рыбке', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Сказка о рыбаке и рыбке']

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        assert 'Гарри Поттер и философский камень' in collector.favorites

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')

        assert 'Гарри Поттер и философский камень' not in collector.favorites

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')

        assert collector.get_list_of_favorites_books() == ['Сияние']





