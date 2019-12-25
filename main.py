from walkman import Walkman


def main():
    songs= ["Mama", "its my life", "counting stars"]
    playlist = Walkman(songs)
    songs=playlist.convert_lower()
    playlist.play("Mama")
    playlist.next()
    playlist.next()
    playlist.next()
    playlist.pause()
    playlist.pause()
    playlist.add_song(("Rose Tatto","All  fall down", "Morning"))
    print (songs)
    #playlist.remove_song("All  fall down")
    #print (songs)
    #playlist.remove_song("All  fall down")
    #print (songs)




if __name__  == '__main__':
    main()
