def make_album(artist_name, album_title, number_tracks=''):
    '''Return a dictionary of information about a person.'''
    artist_album = {'artist': artist_name, 'album': album_title}
    if number_tracks:
        artist_album['number_tracks'] = number_tracks
    return artist_album

singer = make_album('jimi', 'hendrix')
print(singer)
band = make_album('aerosmith','get your wings', number_tracks=8)
print(band)