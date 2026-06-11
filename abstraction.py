# Abstraction: the Movie class highlights main features and sets a common blueprint.
# The mandatory play() method is declared, but its specific implementation is hidden in the subclasses.
from abc import ABC, abstractmethod

class Movie(ABC):  # Abstract class
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre

    @abstractmethod
    def play(self):  # Abstract method without implementation
        pass

    def get_basic_info(self):
        return f"{self.title} ({self.release_year}) - {self.genre}"

class DigitalMovie(Movie):
    def play(self):  # Implementation of playback logic for streaming
        print(f"Streaming: {self.get_basic_info()}")

class PhysicalMovie(Movie):
    def play(self):  # Implementation of playback logic for a physical disc
        print(f"Spinning disc: {self.get_basic_info()}")

my_movie = DigitalMovie("Dune: Part Two", 2024, "Sci-Fi")
my_movie.play()