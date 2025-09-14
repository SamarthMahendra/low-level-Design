
import threading

class GameSetting:
    _instance = None
    _lock = threading.Lock()
    _initialized = False  # to prevent re-initialization

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, volume=100, difficulty="easy", resolution="1080p"):
        if not self._initialized:  # initialize only once
            self.volume = volume
            self.difficulty = difficulty
            self.resolution = resolution
            GameSetting._initialized = True

    def display(self):
        print(f"Volume: {self.volume}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Resolution: {self.resolution}")

    def reset(self):
        """Restore default values"""
        self.volume = 100
        self.difficulty = "easy"
        self.resolution = "1080p"
        print("⚙️ Settings reset to defaults.")



s1 = GameSetting()
s2 = GameSetting()
print("\nIDs prove Singleton:")
print(f"id(s1) = {id(s1)}, id(s2) = {id(s2)}")

s1.volume = 50
print("\nModified through s1 → reflected in s2:")
s2.display()

# --- Reset demo ---
print("\nResetting settings...")
s1.reset()
s2.display()

