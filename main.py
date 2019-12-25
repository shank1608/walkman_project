from walkman import Walkman
from song import Song


def main():
    songs = [Song("Mama"), Song("Its My Life"), Song("Counting Stars")]
    playlist = Walkman(songs)
    playlist.play("Mama")
    playlist.next()
    playlist.next()
    playlist.next()
    playlist.pause()
    playlist.pause()
    playlist.add_song("Rose Tattoo", "All  fall down", "Morning")
    print(playlist.songs)
    #playlist.remove_song("All  fall down")
    #print (songs)
    #playlist.remove_song("All  fall down")
    #print (songs)


if __name__  == '__main__':
    main()