class Amplifier:
    def on(self): print("Amplifier on")
    def set_volume(self, level): print(f"Amplifier volume {level}")

class DVDPlayer:
    def on(self): print("DVD Player on")
    def play(self, movie): print(f"Playing '{movie}'")

class Projector:
    def on(self): print("Projector on")
    def wide_screen_mode(self): print("Projector in widescreen mode")

class TheaterLights:
    def dim(self, level): print(f"Lights dimming to {level}%")



class HomeTheaterFacade:
    def __init__(self, amp, dvd, proj, lights):
        self.amp = amp
        self.dvd = dvd
        self.proj = proj
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(30)
        self.proj.on()
        self.proj.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.lights.dim(100)
        print("Amplifier off, DVD stopped, Projector off")


# Subsystems
amp = Amplifier()
dvd = DVDPlayer()
proj = Projector()
lights = TheaterLights()

# Facade
home_theater = HomeTheaterFacade(amp, dvd, proj, lights)
home_theater.watch_movie("Inception")
home_theater.end_movie()

