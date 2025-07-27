# Author: William Spinella
# GitHub username: wcspinella
# Date: 4/15/2025
# Description: A program that will return the streaming services that a movie can be found on, if any.

class Movie:
    """Represents a movie with its title, genre, director and release year."""

    def __init__(self, title, genre, director, year):
        """Creates a new movie with a title, genre, director, and year."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def get_title(self):
        """Returns the title of the movie."""
        return self._title

    def get_genre(self):
        """Returns the genre of the movie."""
        return self._genre

    def get_director(self):
        """Returns the director of the movie."""
        return self._director

    def get_year(self):
        """Returns the year of the movie."""
        return self._year

class StreamingService:
    """Represents a streaming service and includes the name of the streaming service and its catalog of movies."""

    def __init__(self, name):
        """Creates a streaming service with a name and creates a catalog to add movies to."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Returns streaming service name."""
        return self._name

    def get_catalog(self):
        """Returns streaming service movie catalog."""
        return self._catalog

    def add_movie(self, movie_object):
        """Adds movie to the streaming service catalog."""
        self._catalog[movie_object.get_title()] = movie_object

    def delete_movie(self, movie_title):
        """Removes a movie from the streaming service catalog."""
        if movie_title in self._catalog:
            del self._catalog[movie_title]

class StreamingGuide:
    """Represents a guide to streaming services, tracking which services offer a specific movie."""

    def __init__(self):
        """Creates a streaming guide and initiates a list for streaming service to be added to if the movie is on the streaming service."""
        self._streaming_services = []

    def add_streaming_service(self, streaming_service_object):
        """Adds a streaming service to the guide."""
        self._streaming_services.append(streaming_service_object)

    def delete_streaming_service(self, streaming_service_name):
        """Removes a streaming service from the guide."""
        for service in self._streaming_services:
            if service.get_name() == streaming_service_name:
                self._streaming_services.remove(service)

    def who_streams_this_movie(self, movie_title):
        """Lists which streaming services the movie can be found on."""
        services_streaming = []
        movie_year = None

        for service in self._streaming_services:
            catalog = service.get_catalog()
            if movie_title in catalog:
                movie = catalog[movie_title]
                services_streaming.append(service.get_name())
                movie_year = movie.get_year()

        if services_streaming:
            return {"title": movie_title, "year": movie_year, "services": services_streaming}
        else:
            return None
