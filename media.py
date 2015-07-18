__author__ = 'ali786'


class Movie():
    """
    This class describes various attributes
    for a movie.
    """

    def __init__(self, title, storyline, poster, trailer, genre):
        self.title = title
        self.story_line = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.genre = genre
