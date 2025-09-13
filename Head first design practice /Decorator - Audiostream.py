from abc import ABC, abstractmethod




class AudioStream(ABC):
    @abstractmethod
    def process(self) -> str:
        pass




# --- Concrete Component ---
class RawAudioStream(AudioStream):
    def process(self) -> str:
        return "Raw audio data"



# -- decorator Component --
class AudioFilter(AudioStream, ABC):
    def __init__(self, stream: AudioStream):
        self._stream = stream

    @abstractmethod
    def process(self) -> str:
        pass


# --- Concrete Decorators ---
class ReverbFilter(AudioFilter):
    def process(self) -> str:
        return self._stream.process() + " + Reverb"


class EchoFilter(AudioFilter):
    def process(self) -> str:
        return self._stream.process() + " + Echo"


class BassBoostFilter(AudioFilter):
    def process(self) -> str:
        return self._stream.process() + " + Bass Boost"


class NoiseSuppressionFilter(AudioFilter):
    def process(self) -> str:
        return self._stream.process() + " + Noise Suppression"

# --- Demo ---
if __name__ == "__main__":
    # Just raw audio
    stream1 = RawAudioStream()
    print(stream1.process())
    # Output: Raw audio data

    # Add Reverb, then Echo
    stream2 = EchoFilter(ReverbFilter(RawAudioStream()))
    print(stream2.process())
    # Output: Raw audio data + Reverb + Echo

    # Add Noise Suppression, then Bass Boost
    stream3 = BassBoostFilter(NoiseSuppressionFilter(RawAudioStream()))
    print(stream3.process())
    # Output: Raw audio data + Noise Suppression + Bass Boost

    # Stack multiple effects
    stream4 = BassBoostFilter(EchoFilter(ReverbFilter(RawAudioStream())))
    print(stream4.process())
    # Output: Raw audio data + Reverb + Echo + Bass Boost
