from __future__ import annotations
from typing import Protocol, List, runtime_checkable, Optional


@runtime_checkable
class Observer(Protocol):
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        ...


@runtime_checkable
class Subject(Protocol):
    def register(self, obs: Observer) -> None: ...
    def remove(self, obs: Observer) -> None: ...
    def notify(self) -> None: ...


class WeatherData(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temp: Optional[float] = None
        self._humidity: Optional[float] = None
        self._pressure: Optional[float] = None

    # Subject API
    def register(self, obs: Observer) -> None:
        if obs not in self._observers:
            self._observers.append(obs)

    def remove(self, obs: Observer) -> None:
        try:
            self._observers.remove(obs)
        except ValueError:
            pass  # already gone

    def notify(self) -> None:
        # push model: send current values to observers
        for obs in list(self._observers):  # iterate over a snapshot to allow removal during notify
            obs.update(self._temp, self._humidity, self._pressure)  # type: ignore[arg-type]

    # WeatherData behavior
    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        self._temp, self._humidity, self._pressure = temp, humidity, pressure
        self._measurements_changed()

    def _measurements_changed(self) -> None:
        self.notify()

    # Optional getters for a pull model
    @property
    def temperature(self) -> Optional[float]:
        return self._temp

    @property
    def humidity(self) -> Optional[float]:
        return self._humidity

    @property
    def pressure(self) -> Optional[float]:
        return self._pressure


# --- Observers (displays) ---
class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data: Subject) -> None:
        self._temp = 0.0
        self._humidity = 0.0
        weather_data.register(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temp, self._humidity = temp, humidity
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self._temp:.1f}°C and {self._humidity:.1f}% humidity")


class StatisticsDisplay(Observer):
    def __init__(self, weather_data: Subject) -> None:
        self._temps: List[float] = []
        weather_data.register(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temps.append(temp)
        self.display()

    def display(self) -> None:
        avg = sum(self._temps) / len(self._temps)
        print(f"Temp stats → min: {min(self._temps):.1f}, max: {max(self._temps):.1f}, avg: {avg:.1f}")


class HeatIndexDisplay(Observer):
    """A tiny ‘feels like’ example—approximation for demo."""
    def __init__(self, weather_data: Subject) -> None:
        self._index = 0.0
        weather_data.register(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        # simple fake formula: heat index rises with temp and humidity
        self._index = temp + 0.1 * humidity
        self.display()

    def display(self) -> None:
        print(f"Heat Index: {self._index:.1f}")


# --- Demo ---
if __name__ == "__main__":
    wd = WeatherData()
    current = CurrentConditionsDisplay(wd)
    stats = StatisticsDisplay(wd)
    heat = HeatIndexDisplay(wd)

    wd.set_measurements(26.0, 65.0, 1013.0)
    wd.set_measurements(28.5, 70.0, 1012.0)
    wd.set_measurements(25.2, 60.0, 1015.0)

    # Observers can unsubscribe at runtime
    wd.remove(heat)
    wd.set_measurements(30.0, 55.0, 1011.0)
