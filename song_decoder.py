def song_decoder(song):
    song_list = song.split("WUB")
    song_list = ' '.join(song_list)
    song_list = song_list.strip()
    song_list = ' '.join(song_list.split())
    return song_list
