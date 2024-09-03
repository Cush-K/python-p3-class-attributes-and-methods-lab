class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    songs = []
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)
        Song.add_songs(self.name)
        
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
        
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
        
        
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
            
    @classmethod
    def add_songs(cls, name):
        cls.songs.append(name)
   
