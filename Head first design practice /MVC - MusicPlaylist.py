

class PlaylistModel:

    def __init__(self, name="My Playlist"):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            return False
           

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            return False


    def get_songs(self):
        return self.songs


class PlaylistView:

    @staticmethod
    def display_playlist(playlist: PlaylistModel):
        print(f'Playlist: {playlist.name}')
        if not playlist.get_songs():
            print("  (empty)")
        else:
            for idx, song in enumerate(playlist.get_songs(), start=1):
                print(f"  {idx}. {song}")
        print()


class PlaylistController:

    def __init__(self, model: PlaylistModel, view: PlaylistView):
        self.model = model
        self.view = view

    def add_song(self, song):
        if self.model.add_song(song) is False:
            print(f'"{song}" already exists.')
        self.view.display_playlist(self.model)

    def remove_song(self, song):
        if self.model.remove_song(song) is False:
            print(f'"{song}" not found.')
        self.view.display_playlist(self.model)

    def show_playlist(self):
        self.view.display_playlist(self.model)


# --- Usage ---
if __name__ == "__main__":
    model = PlaylistModel()
    view = PlaylistView()
    controller = PlaylistController(model, view)

    controller.add_song("Song A")
    controller.add_song("Song B")
    controller.show_playlist()

    controller.remove_song("Song A")
    controller.show_playlist()
