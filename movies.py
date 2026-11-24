def add_movie(movies):
    title = input("Введите название фильма: ")


    if not title.strip():
        print("Ошибка: название фильма не может быть пустым!")
        return

    try:
        duration = int(input("Введите продолжительность фильма в минутах: "))
    except ValueError:
        print("Ошибка: введите число!")
        return

    if duration <= 0:
        print("Ошибка: продолжительность должна быть положительной!")
        return

    movie = {
        "id": len(movies) + 1,
        "title": title,
        "duration": duration
    }

    movies.append(movie)
    print("Фильм успешно добавлен!")

def show_movies(movies):
    if not movies:
        print("Список фильмов пуст!")
        return

    print("\nСписок фильмов:")

    for movie in movies:
        print(f"ID: {movie['id']}")
        print(f"Название: {movie['title']}")
        print(f"Продолжительность: {movie['duration']} минут")
        print("--------------------")

def delete_movie(movies):
            if not movies:
                print("Список фильмов пуст!")
                return

            show_movies(movies)

            try:
                movie_id = int(input("Введите ID фильма для удаления: "))
            except ValueError:
                print("Ошибка: введите правильный ID!")
                return

            for movie in movies:
                if movie["id"] == movie_id:
                    movies.remove(movie)
                    print("Фильм успешно удалён!")
                    return

            print("Ошибка: фильм с таким ID не найден!")
