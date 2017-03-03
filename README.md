# Media Center site

Builds a page to be opened in a browser that displays information on movies.
Includes the name and movie poster for the movie, if the user clicks
on the movie poster a pop-up frame will play the movie's trailer from YouTube.

Getting Started
---------------
**Requires requests module, not found in Python Standard Library**
Run 'pip install requests' from the command line before starting

Add any new movies to entertainment_center.py using the following convention:
name_of_movie = media.Movie('TMDB_ID_NUMBER')

ex: moana = media.Movie('277834')

ID numbers can be found on TheMovieDB.org as part of the URL for the movie
ex: themoviedb.org/movie/**277834**-moana

Files
------
entertainment_center.py: Holds list of movies, packages in a list, and sends
  to fresh_tomatoes.py to build fresh_tomatoes.html
fresh_tomatoes.py: Builds fresh_tomatoes.html from information in
  entertainment_center.py  
media.py: Contains classes for Video and Movies objects, requests information
  from TheMovieDB to use in fresh_tomatoes.py

Credit
------
Requests module: https://github.com/kennethreitz/requests
