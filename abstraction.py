from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre

    @abstractmethod
    def play(self):
        pass

    def get_basic_info(self):
        return f"{self.title} ({self.release_year}) - {self.genre}"

class DigitalMovie(Movie):
    def play(self):
        print(f"Streaming: {self.get_basic_info()}")

class PhysicalMovie(Movie):
    def play(self):
        print(f"Spinning disc: {self.get_basic_info()}")

my_movie = DigitalMovie("Dune: Part Two", 2024, "Sci-Fi")
my_movie.play()