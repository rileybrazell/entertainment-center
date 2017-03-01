import webbrowser


# Creates a Video object to be accessed by fresh_tomatoes.py to build webpage
class Video():
	# List of valid ratings, can be used for parental controls
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, rating, title, year):
		self.rating = rating
		self.title = title
		self.year = year

class Movie(Video):
	# Inherits Video class with unique variables for plot, poster, and trailer
	def __init__(self, rating, title, year, movie_plot, poster_image,
				trailer_youtube):
		Video.__init__(self, rating, title, year)
		self.movie_plot = movie_plot
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# Opens a link to the movie's trailer on youtube, used for pop-up frame
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
