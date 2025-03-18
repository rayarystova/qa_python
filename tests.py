import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    def test_get_book_genre_returns_empty_for_unset_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Без жанра')
        assert collector.get_book_genre('Без жанра') == ""


    def test_get_list_of_favorites_books_returns_empty_list_when_no_books(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []


    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        book_name = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(book_name)
        genre = 'Ужасы'
        collector.set_book_genre(book_name, genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


    @pytest.mark.parametrize("book_name, invalid_genre", [("Harry Potter", "Музыка"), ("Весна", "Роман")])
    def test_set_book_genre_check_invalid_genre(self, book_name, invalid_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == ""


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']


    @pytest.mark.parametrize('books, genre', [('Шерлок Холмс', 'Детективы'),
                                              ('Гарри Поттер', 'Фатнастика')])
    def test_get_list_of_favorites_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()


    def test_get_books_for_children_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' in collector.get_books_for_children()


    def test_get_books_for_children_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        assert 'Молчание ягнят' not in collector.get_books_for_children()

    
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        collector.add_book_in_favorites('Новая книга')
        assert 'Новая книга' in collector.get_list_of_favorites_books()

    
    def test_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

