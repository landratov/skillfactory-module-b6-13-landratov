1. Поднимаем сервер "python server.py"
2. Для получения списка альбомов открываем в браузере "http://localhost:8080/albums/beatles"
3. Для добавления нового альбома надо отправить POST-запрос: "http -f POST localhost:8080/albums artist=Artist year=2020 album=Album genre=Genre"
4. Если в БД есть альбом, у которого совпадают все параметры, будет возвращена 409 ошибка
