import media
import fresh_tomatoes

# Add all new movies as a media.Movie objects below this line
# movie_title = media.Movie(TMDB ID)
lost_in_translation = media.Movie('153')
song_of_the_sea = media.Movie('110416')
troll_hunter = media.Movie('46146')
ponyo = media.Movie('12429')
moana = media.Movie('277834')
bee_movie = media.Movie('5559')

# Put all added movies into single list
movies = [lost_in_translation, song_of_the_sea, troll_hunter, ponyo, moana,
    bee_movie]

# Pass list of movies over to fresh_tomatoes to create webpage
fresh_tomatoes.open_movies_page(movies)
