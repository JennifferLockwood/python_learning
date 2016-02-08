def make_album(artist_name, album_title, number_tracks=''):
    '''Return a dictionary of information about an artist or band.'''
    artist_album = {'artist': artist_name, 'album': album_title}
    return artist_album

while True:
    print("\nPlease tell me the album's artist and title:")
    print("(enter 'q' at any time to quit)")

    albums_artist = input("Album's artist: ")
    if albums_artist == 'q':
        break

    album_title = input("Album's title: ")
    if album_title == 'q':
        break

    album_info = make_album(albums_artist, album_title)
    print(album_info)