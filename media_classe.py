# encoding=utf-8
"""Modulo de classe"""


class Movie():
    """Esta classe define o modelo para o objeto Movie"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image_url = poster_image
        self.youtube_url = trailer_youtube
