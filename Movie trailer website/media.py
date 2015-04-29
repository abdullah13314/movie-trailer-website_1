# importing webbrowser from python standard library
import webbrowser

class Movie():
    """A class of Movies
    Movie class which store information regarding the movie and then call a method
    for showing its trailer

    Attributes:
        title = Title of the movie
        storyline = Brief storyline for the movie
        poster_image_url = URL for a poster image for the movie
        trailer_youtube_url = URL for a youtube trailer for the movie
        rating = IMDB rating for the movie
        """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rating):
        """Inits Movie with variables movie title, movie storyline, poster image,
        trailer youtube and imdb rating"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = imdb_rating

    def show_trailer(self):
        """Opens a movies trailer in web browser when is passed the an instance Movie
        Args:
            Self: The Movie instance foe which to open the movie trailer
        Returns:
            Opens a movie trailer in web browser
            """
        webbrowser.open(self.trailer_youtube_url)
    
