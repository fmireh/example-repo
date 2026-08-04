class Album:

    def __init__(self, album_name, album_artist,number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs      
      
    def __str__(self):
        return str(f"{self.album_name}, {self.album_artist}, {self.number_of_songs}")


def show_albums(albums):
    """Shows the contents of a list of albums.

    Args:
        albums (list): The list of Album objects to display.
    """
    for album in albums:
        print(album)

def sort_number_of_songs(albums):
    """Sort a list of albums by number of songs in ascending order
    and display it.

    Args:
        albums (list): The list of Album objects to sort by number of songs.
    """
    albums.sort(key=lambda album: album.number_of_songs)
    print("\nAlbums sorted by number of songs:")
    show_albums(albums)

def index_swap(albums, index0, index1):
    """Swap the element at position 1 (index 0)"""
    albums[index0- 1], albums[index1 - 1] = (
            albums[index1 - 1],
            albums[index0 - 1],
        )
    print(f"\nAlbums after swapping positions {index0} and {index1}:")
    show_albums(albums)


albums1 = [Album("Thriller", "Michael Jackson", 9),
           Album("Abbey Road", "The Beatles", 17),
           Album("Back in Black", "AC/DC", 10),
           Album("Random Access Memories", "Daft Punk", 13),
           Album("When We All Fall Asleep, Where Do We Go?", "Billie Eilish", 14)
]
show_albums(albums1)
sort_number_of_songs(albums1)
index_swap(albums1,1,2)

albums2 =  [Album("Rumours", "Fleetwood Mac", 11),
           Album("Nevermind", "Nirvana", 12),
           Album("1989", "Taylor Swift", 13),
           Album("The Eminem Show", "Eminem", 20),
           Album("Future Nostalgia", "Dua Lipa", 11)
]

print(albums2)

albums2.extend(albums1)

print(albums2)

albums2.extend([
        Album("Dark Side of the Moon", "Pink Floyd", 9),
        Album("Oops!... I Did It Again", "Britney Spears", 16)
])

for index, album2 in enumerate(albums2):
    if album2.album_name == "Dark Side of the Moon":
        print(f"\nIndex of '{album2.album_name}' in the list: {index}")