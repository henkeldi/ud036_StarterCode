"""
Represents a Movie
"""


class Movie(object):
    """Represents a Movie
    
    Args:
        title (str): The title of the movie
        poster_image_url (str): An URL which points to a poster of the movie
        trailer_youtube_url (str): A Youtube URL which points to the movies trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
