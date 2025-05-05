**test_add_new_book_add_two_books** - уже созданный тест, проверяет добавление двух валидных книг
**test_get_books_genre_success** - проверяет корректное получение словаря books_genre (при валидных и невалидных данных)
**test_set_book_genre_for_valid_and_invalid_genre_success** - проверяет установку валидного/невалидного жанра
**test_get_book_genre_success** - получения жанра книги по её имени
**test_get_books_with_specific_genre_returns_correct_list** - возвращает список книг указанного жанра. Для несуществующих жанров возвращает пустой список.
**test_get_books_for_children_books_with_genres_from_age_rating_list_are_excluded** - по сути проверяю, что возвращаются только детские книги, добавляя жанры с/без возрастного рейтинга
**test_add_book_in_favorite_positive_result** - добавление книги в избранное
**test_delete_book_from_favorites_existing_book_removes_from_favorites**- удаление книги из избранного
**test_get_list_of_favorites_books_returns_all_added_favorites** - корректность возвращаемого списка избранного при добавлении нескольких книг