


from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def play(self, player: 'MusicPlayer'):
        pass

    @abstractmethod
    def pause(self, player: 'MusicPlayer'):
        pass

    @abstractmethod
    def stop(self, player: 'MusicPlayer'):
        pass



class PlayingState(State):
    def play(self, player: 'MusicPlayer'):
        print("Already playing.")

    def pause(self, player: 'MusicPlayer'):
        print("Pausing playback.")
        player.state = PausedState()

    def stop(self, player: 'MusicPlayer'):
        print("Stopping playback.")
        player.state = StoppedState()

class PausedState(State):
    def play(self, player: 'MusicPlayer'):
        print("Resuming playback.")
        player.state = PlayingState()

    def pause(self, player: 'MusicPlayer'):
        print("Already paused.")

    def stop(self, player: 'MusicPlayer'):
        print("Stopping playback from paused state.")
        player.state = StoppedState()

class StoppedState(State):
    def play(self, player: 'MusicPlayer'):
        print("Starting playback.")
        player.state = PlayingState()

    def pause(self, player: 'MusicPlayer'):
        print("Can't pause. Player is stopped.")

    def stop(self, player: 'MusicPlayer'):
        print("Already stopped.")

class MusicPlayer:
    def __init__(self):
        self.state: State = StoppedState()

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)

# --- Demo ---
if __name__ == "__main__":
    player = MusicPlayer()

    player.play()   # Starting playback.
    player.play()   # Already playing.
    player.pause()  # Pausing playback.
    player.pause()  # Already paused.
    player.play()   # Resuming playback.
    player.stop()   # Stopping playback.
    player.stop()   # Already stopped.
    player.pause()  # Can't pause. Player is stopped.

