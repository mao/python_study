def make_album(artist, album_name, track_num=10):
    album_info = {'artist': artist,
                  'album_name': album_name,
                  'tracks': track_num}
    return album_info

active = True

albums = []

while active:
    album_name = input('Please input album name: \t')
    artist = input('Please input artist of ' + album_name +': \t')
    tracks = input('Please input tracks of ' + album_name + '(default 10): \t')
    if tracks:
        current_album = make_album(artist, album_name, int(tracks))
    else:
        current_album = make_album(artist, album_name)
        
    print(current_album)
    albums.append(current_album)
    i = input('Do you want to continue(y/n)? \t')
    if i != 'y':
        active = False

print(albums)
