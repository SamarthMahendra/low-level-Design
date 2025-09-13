from abc import ABC, abstractmethod

class EqStrategy(ABC):
    @abstractmethod
    def apply(self):
        pass


class NormalEQ(EqStrategy):
    def apply(self):
        print("Applying Normal EQ")


class BassBoostEQ(EqStrategy):
    def apply(self):
        print("Applying Bass Boost EQ")


class TrebleBoostEQ(EqStrategy):
    def apply(self):
        print("Applying Treble Boost EQ")


class VocalEQ(EqStrategy):
    def apply(self):
        print("Applying Vocal EQ")


# ---- Music Player Interface ----
class MusicPlayerInterface(ABC):
    @abstractmethod
    def play(self, song: str):
        pass

    @abstractmethod
    def set_equalizer_mode(self, strategy: EqStrategy):
        pass


class MusicPlayer:
    def __init__(self, equalizer_strategy: EqStrategy):
        self._equalizer_strategy = equalizer_strategy

    def play(self, song: str):
        print(f"🎵 Playing {song}")
        self._equalizer_strategy.apply()

    def set_equalizer_mode(self, strategy: EqStrategy):
        self._equalizer_strategy = strategy
        print("Equalizer mode changed!")


# --- Demo ---
player = MusicPlayer(NormalEQ())
player.play("Shape of You")

player.set_equalizer_mode(BassBoostEQ())
player.play("Shape of You")

player.set_equalizer_mode(VocalEQ())
player.play("Shape of You")
