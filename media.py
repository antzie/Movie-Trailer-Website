#!/usr/bin/env python2
# Version 04-06-2018

import webbrowser


class Movie():
    """Stores Movie Related Information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, tomato_meter, movie_director,
                 movie_actors, year_released):
        """Constructs a new instance of class Movie.

        Args:
                movie_title: the title of the relevant movie (String)
                movie_storyline: the movie's storyline (String)
                poster_image: the movie's poster (Url)
                trailer_youtube: the movie's trailer (Url) taken from Youtube.
                tomato_meter: Rotten Tomatoes Ratings (String)
                movie_director: the movie's director (String)
                movie_actors: the movie's actors (String)
                year_released: the year movie was released (Integer)
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = tomato_meter
        self.director = movie_director
        self.actors = movie_actors
        self.year = year_released

    def show_trailer(self):
        """Opens the trailer for the relevant instance.

        Opens in either a new window or a new tab.
        Args:
                self: an instance of class Movie
        Returns:
                the relevant trailer
        """
        return webbrowser.open(self.trailer_youtube_url)
