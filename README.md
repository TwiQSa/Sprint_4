# test_add_new_book_add_one_book -  проверяет, что при добавлении новой книги, количество книг увеличится, поэтому используем len и get_books_genre(), чтобы проверить, что книга появилась. 
# test_set_book_genre_any_genre_from_list - проверяет, что можно установить жанр из списка для уже добавленной книги. 
# test_get_book_genre_from_existing_book - проверяет, что можно получить и проверить, что жанр уже добавленной книги, соответствует этой книге.  
# test_get_books_with_specific_genre_horror - тут использовал параметризацию, чтобы получить список книг определенного жанра - ужасы. 
# test_get_books_with_genre_list_of_books_and_genres - с помощью параметризации проверил, что можно получить список всех добавленных книг с их жанрами. 
# test_get_books_for_children_with_horror_genre - проверяет, что жанры ужасы не отображаются в списке книг для детей. 
# test_get_books_for_children_with_cartoons_genre- проверяет, что жанр мультфильмы отображается в списке книг для детей. 
# test_add_book_in_favorites_one_book - проверяет, что можно добавить книгу в список избранных и книга появляется в списке collector.favorites
# test_delete_book_from_favorites_one_book - проверяет, что можно удалить книгу из списка избранных и ее нет в списке collector.favorites
# test_get_list_of_favorites_books_one_book - проверяет, что можно получить список избранных книг.