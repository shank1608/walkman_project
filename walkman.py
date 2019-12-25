class Walkman():
    def __init__(self,songs):
        self.songs= [x.lower() for x in songs]
        self.status = False # shows walkman status
    def play(self,song):
        if song.lower() in self.songs:
            print ("playing  song ", song)
            self.current_song= song.lower()
            self.status = True
        else:
            print ("song is not in the list")
    def next(self):
        newplaylist = self.songs
        current_index= newplaylist.index(self.current_song)
        try:
            next_index= current_index+1
            next_song = newplaylist[next_index]
            print("playing next song ..", next_song)
            self.current_song= next_song
        except IndexError:
            next_index =0
            next_song = newplaylist[next_index]
            print("playing next song ..", next_song)
            self.current_song= next_song

    def pause(self):
        if self.status:
            print("pausing current song", self.current_song)
            self.status =False
        else:
            print("Walkman is already paused")


    def add_song(self,*addedsongs):
         self.songs.extend(*addedsongs)

    def remove_song(self, song):
        try:
             self.songs.remove(song.lower())
        except ValueError:
            print("song is not in the list")

    def convert_lower(self):
        #self.lower_song=map(lambda x:x.lower(),self.songs))
        return [x.lower() for x in self.songs]
