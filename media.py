import webbrowseclass Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """Defines an procedure that demonstrates the movie title,"
    " storyline, poster and trailer, defined in the entertainment_center.py"""

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    """Opens youtube trailer associated with movie on fresh_tomatoes"""