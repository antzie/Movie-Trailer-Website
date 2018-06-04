#!/usr/bin/env python2
# Version 04-06-2018

import fresh_tomatoes_rev
import media

# Instances of Class Movie
cinderella = media.Movie("Cinderella",
                         "The classic fairytale told as it should be told",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Cinderella_2015_official_poster.jpg/220px-Cinderella_2015_official_poster.jpg",  # NOQA
                         'https://www.youtube.com/watch?v=20DF6U1HcGQ',  # NOQA
                         '84%',
                         'Kenneth Branagh',
                         'Cate Blanchett, Lily James, Richard Madden',
                         2015
                         )

black_hawk_down = media.Movie("Black Hawk Down",
                              ("The Battle of Mogadishu, fought between US "
                                "Special Forces and Somali militia fighters"),
                              'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Black_hawk_down_ver1.jpg/220px-Black_hawk_down_ver1.jpg',  # NOQA
                              "https://www.youtube.com/watch?v=5Y1ju8QwpQM",  # NOQA
                              '76%',
                              'Ridley Scott',
                              'Josh Hartnett, Ewan McGregor, Eric Bana',
                              2001
                              )

thor_ragnarok = media.Movie("Thor: Ragnarok",
                            ("Thor loses his hammer and has yet more "
                             "family problems"),
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ue80QwXMRHg",   # NOQA
                            '92%',
                            'Taika Waititi',
                            'Chris Hemsworth, Cate Blanchett',
                            2017
                            )

darkest_hour = media.Movie("The Darkest Hour",
                           ("The story of Britain's leaders during the "
                            "retreat to Dunkirk and the decisions they faced"),
                           "https://upload.wikimedia.org/wikipedia/en/3/38/Darkest_Hour_poster.png",   # NOQA
                           "https://www.youtube.com/watch?v=LtJ60u7SUSw",   # NOQA
                           '86%',
                           'Joe Wright',
                           'Gary Oldman, Kristin Scott Thomas, Lily James',
                           2017
                           )

star_wars = media.Movie("Star Wars: A New Hope",
                        "'You're classic when you start it all'",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",   # NOQA
                        "https://www.youtube.com/watch?v=MpkrMqmmy5k",   # NOQA
                        '93%',
                        'George Lucas',
                        'Mark Hamill, Harrison Ford, Carrie Fisher',
                        1977
                        )

the_man_from_nowhere = media.Movie("The Man From Nowhere",
                                   ("When a little girl is kidnapped by gangs,"
                                    " a mysterious pawn shop owner goes after"
                                    " her"),
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/The_Man_from_Nowhere_poster.jpg/220px-The_Man_from_Nowhere_poster.jpg",   # NOQA
                                   "https://www.youtube.com/watch?v=38rPoGSr19U",   # NOQA
                                   '100%',
                                   'Lee Jeong-beom',
                                   'Won Bin, Kim Sae-ron, Kim Tae-hoon',
                                   2010
                                   )

# List of movie instances
movies = [cinderella, black_hawk_down, the_man_from_nowhere,
          darkest_hour, star_wars,  thor_ragnarok, ]

# Create the movie-trailers web-page
fresh_tomatoes_rev.open_movies_page(movies)
