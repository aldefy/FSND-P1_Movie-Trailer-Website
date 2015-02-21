import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_data, trailer_youtube):
        """Initiates the Movie class with all available attributes"""

        self.title = movie_data[0]
        self.year = movie_data[1]
        self.poster_image_url = movie_data[2]
        self.genres = movie_data[3]
        self.storyline = movie_data[4]
        self.rating = movie_data[5]
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays the movie trailer in a modal"""

        webbrowser.open(self.trailer_youtube_url)
