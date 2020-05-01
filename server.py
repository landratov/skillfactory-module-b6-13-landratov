from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов артиста {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "У {} есть {}:<br><br>".format(artist.title(), make_russian(len(album_names)))
        result += "<br>".join(album_names)
    return result

@route("/albums", method = "POST")
def addAlbum():
    if "artist" not in request.forms or "album" not in request.forms or "genre" not in request.forms or "year" not in request.forms:
        message = "Для добавления альбома необходимо передать 4 параметра: artist, album, genre, year"
        result = HTTPError(400, message)
    elif not isinstance(request.forms.get("year"), int) and len(request.forms.get("year")) != 4:
        message = "В параметре year должно быть число из 4 символов"
        result = HTTPError(400, message)
    elif checkAlbumExist(request.forms.get("artist"), request.forms.get("album"), request.forms.get("genre"), request.forms.get("year")):
        message = "Альбом уже существует в базе"
        result = HTTPError(409, message)
    else:
        album.add(request.forms.get("artist"), request.forms.get("album"), request.forms.get("genre"), request.forms.get("year"))
        result = "Альбом был успешно сохранен"
    return result

def checkAlbumExist(artist, albumname, genre, year):
    if (album.checkAlbum(artist, albumname, genre, year)):
        return True
    else:
        return False

def make_russian(n):
    last_digit = n % 10
    last_two = n % 100
    if last_digit == 1 and last_two != 11:
        ending = "альбом"
    elif last_digit in [2, 3, 4] and not (last_two in [12, 13, 14]):
        ending = "альбома"
    else:
        ending = "альбомов"
    return str(n) + " " + ending

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)