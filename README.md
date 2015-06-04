# Website: movie favorites.
A simple movie trailer website to exercise some programming foundations with python.

**Note:** This is a solution to project 1 of the [Udacity Full Stack Web Developer Nanodegree][1] based on the course [Programming Foundations with Python (ud036)][2]. The solution is graded with "Exceeds Specifications".

## Detailed Description
The website shows nine of my favorite movies with additional infos pulled from the [OMDb API][3]:
- Poster image
- Title
- Year
- List of genres separated by dashes
- Plot with maximum of 150 characters (if longer, truncated with '...').
- imdb-Rating

Additionally to the OMDb-Infos, an English trailer from [YouTube][4] is added for each of the movies.

## Requirements
[Python 2.7][5] installed

## Running Instructions
Generate the file `fresh_tomatoes.html`by running

    python entertainment_center.py
from the command prompt. By clicking on the movies, a modal opens up and the trailer is played.

[1]: https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004 "Udacity Nanodegree: Full Stack Web Developer"
[2]: https://www.udacity.com/course/programming-foundations-with-python--ud036-nd "Udacity Course: Programming Foundations with Python"
[3]: http://www.omdbapi.com/ "OMDb API - The Open Movie Database"
[4]: https://www.youtube.com/ "YouTube Website"
[5]: https://www.python.org/downloads/ "Download Python"
