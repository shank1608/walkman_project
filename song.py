import yaml


INFO_FILE = "song_info.yaml"

class Song:
    def __init__(self, song_name):
        self.name = song_name.lower()
        self.artist = self.lookup_artist(self.name)
        self.album = self.lookup_album(self.name)

    def __repr__(self):
        return (
            "Song: {song} from album: "
            "{album} by artist: {artist}".format(
                song=self.name,
                album=self.album,
                artist=self.artist)
        )


    def lookup_album(self, song_name):
        with open(INFO_FILE, "r") as info_file:
            song_info = yaml.safe_load(info_file)
        return song_info[song_name]["album"]

    def lookup_artist(self, song_name):
        with open(INFO_FILE, "r") as info_file:
            song_info = yaml.safe_load(info_file)
        return song_info[song_name]["artist"]

if __name__ == "__main__":
    s = Song("counting stars")
    print(s)
