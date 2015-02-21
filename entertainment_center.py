import fresh_tomatoes
import media

import urllib2  # library for opening urls
import json  # json encoder and decoder


def get_movie_data(imdb_id):
    """Gets movie data from OMDb-API & returns only needed, formatted data."""

    def comma_separated_string_to_list(comma_separated_string):
        """Converts a comma separated string in a list."""

        list = comma_separated_string.split(",")
        return list

    def truncate_plot(plot):
        """Truncates plot length to max. 150 characters"""

        truncated_plot = (plot[:147] + '...') if len(plot) > 150 else plot
        return truncated_plot

    # funcion urlib2.urlopen(URL).read() writes the content of an URL to a
    # variable. As the OMDb-API returns the data in a json-structure,
    # function json.loads(STRING) converts the URL-content is to json.

    imdb_movie_data = json.loads(
        urllib2.urlopen(
            "http://www.omdbapi.com/?i=" +
            imdb_id +
            "&plot=short&r=json").read()
        )

    # only needed data attributes are returned. Thereby, genre should be
    # outputted as a list and the plot shouldn't be too long.

    custom_movie_data = [imdb_movie_data["Title"],
                         imdb_movie_data["Year"],
                         imdb_movie_data['Poster'],
                         comma_separated_string_to_list(
                            imdb_movie_data['Genre']),
                         truncate_plot(
                            imdb_movie_data['Plot']),
                         imdb_movie_data["imdbRating"]]

    return custom_movie_data

# With the imdb id, new movie instances can easily be created. Only the URL to
# the trailer musst be added separately.

district_9 = media.Movie(
    get_movie_data('tt1136608'),
    'https://www.youtube.com/watch?v=DyLUwOcR5pk')

hanna = media.Movie(
    get_movie_data('tt0993842'),
    'https://www.youtube.com/watch?v=u73CLdHpbNk')

happiness = media.Movie(
    get_movie_data('tt0147612'),
    'https://www.youtube.com/watch?v=_1bgBZJSnNU')

jagten = media.Movie(
    get_movie_data('tt2106476'),
    'https://www.youtube.com/watch?v=9Umv4CyxTdg')

life_in_a_day = media.Movie(
    get_movie_data('tt1687247'),
    'https://www.youtube.com/watch?v=bT_UmBHMYzg')

once_upon_a_time_in_the_west = media.Movie(
    get_movie_data('tt0064116'),
    'https://www.youtube.com/watch?v=MNGQ1hUyx-k')

sin_nombre = media.Movie(
    get_movie_data('tt1127715'),
    'https://www.youtube.com/watch?v=VTSi0pKjC5g')

spaceballs = media.Movie(
    get_movie_data('tt0094012'),
    'https://www.youtube.com/watch?v=0uzEgsHypgM')

rebelle = media.Movie(
    get_movie_data('tt1820488'),
    'https://www.youtube.com/watch?v=5TQnpTIMe5w')

movies = [district_9, hanna, happiness, jagten, life_in_a_day,
          once_upon_a_time_in_the_west, sin_nombre, spaceballs, rebelle]

fresh_tomatoes.open_movies_page(movies)  # Creates the html website
