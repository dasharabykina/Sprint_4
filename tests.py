import pytest
from main import BooksCollector

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating (а точно правильно? не вижу такого словаря и метода соответсвенно), который нам возвращает метод get_books_rating, имеет длину 2
        # поправила так как думаю правильно (если только ошибка не задумана)
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name, result', [
        ("", 0),         
        ('Книга №1', 1),  
        ('Очень длинное название книги больше 41 символа', 0)    
    ])
    def test_get_books_genre_success(self, collector, name, result):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == result

    #тест установки жанра книги
    @pytest.mark.parametrize('name, genre, result', [
        ('Книга №1', 'Фантастика', 'Фантастика'),  # Корректная установка жанра
        ('Книга №2', 'Несуществующий Жанр', '')       # Недопустимый жанр
    ])
    def test_set_book_genre_for_valid_and_invalid_genre_success(self, collector, name, genre, result):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == result 

    #тест получения жанра книги по её имени
    @pytest.mark.parametrize("name, genre, expected_genre", [
    ("Книга 1", "Фантастика", "Фантастика"),
    ("Книга 2", "", "")
    ])
    def test_get_book_genre_success(self, collector, name, genre, expected_genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == expected_genre

    #тест фильтр книги по жанру
    @pytest.mark.parametrize("genre, expected_result", [
        ("Детективы", ["Книга №3"]),                   # Одна книга указанного жанра
        ("Ужасы", []),                                 # Нет книг указанного жанра
        ("Несуществующий жанр", []),                   # Несуществующий жанр
        ("Фантастика", ["Книга №1", "Книга №2"])       # Несколько книг одного жанра      
    ])
    def test_get_books_with_specific_genre_returns_correct_list(self, collector, genre, expected_result):
        collector.add_new_book("Книга №1")
        collector.set_book_genre("Книга №1", "Фантастика")
        collector.add_new_book("Книга №2")
        collector.set_book_genre("Книга №2", "Фантастика") 
        collector.add_new_book("Книга №3")
        collector.set_book_genre("Книга №3", "Детективы") 
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_result

    #тест фильтр книг, подходящие детям
    @pytest.mark.parametrize('genre, expected_result', [
        ('Ужасы', False),     # Жанр с возрастным рейтингом
        ('Фантастика', True),  # Жанр без возрастного рейтинга
        ('Детективы', False),   # Другой жанр с возрастным рейтингом
        ('Несуществующий', False) # Жанр отсутствует в системе
    ])
    def test_get_books_for_children_books_with_genres_from_age_rating_list_are_excluded(self, collector, genre, expected_result):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', genre)
        result = 'Детская книга' in collector.get_books_for_children() 
        assert result == expected_result

    #тест добавления в избранное
    @pytest.mark.parametrize("name, genre", [("Книга №1", "Фантастика")])     
    def test_add_book_in_favorite_positive_result(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()


    #тест удаления из избранного
    @pytest.mark.parametrize("name", ["Книга №1"])  
    def test_delete_book_from_favorites_existing_book_removes_from_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)      
        assert name not in collector.get_list_of_favorites_books()

    #тест корректности получения списка избранного при добавлении неск книг
    def test_get_list_of_favorites_books_add_multiple_books_returns_all_books(self, collector):
        books = ['Книга №1', 'Книга №2', 'Книга №3']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert set(collector.get_list_of_favorites_books()) == set(books)