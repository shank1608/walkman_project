from walkman import Walkman


def main():
    songs = ["Mama", "its my life", "counting stars"]
    playlist = Walkman(songs)
    playlist.play("Mama")
    playlist.next()
    playlist.next()
    playlist.next()
    playlist.pause()
    playlist.pause()
    playlist.add_song("Rose Tattoo", "All  fall down", "Morning")
    print(playlist.songs)
    playlist.remove_song("All  fall down")
    print (playlist.songs)
    playlist.remove_song("All  fall down")
    print (playlist.songs)


if __name__  == '__main__':
    main()
