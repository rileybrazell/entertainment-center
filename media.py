# requests module: https://github.com/kennethreitz/requests
import requests

tmdb_api = '361bdc203344014cb98d70f50cdceca1'

# Creates a Video object containing an id number for an entry on TheMovieDB
class Video():
	def __init__(self, tmdb_id):
		self.tmdb_id = tmdb_id

class Movie(Video):
	# Inherits Video class, requests information on specific id number
	# Only for movies on TheMovieDB
	def __init__(self, tmdb_id):
		Video.__init__(self, tmdb_id)
		# Uses requests module to get information on movie in JSON object
		r_details = requests.get('https://api.themoviedb.org/3/movie/' + tmdb_id + '?api_key=' + tmdb_api + '&language=en-US')
		# Parses JSON object to make values accessible to class
		parsed_details = r_details.json()

		# Requests YouTube video ID for movie trailer
		r_video = requests.get('https://api.themoviedb.org/3/movie/' + tmdb_id
		+ '/videos?api_key=' + tmdb_api + '&language=en-US')
		parsed_video = r_video.json()

		# Creates variables for fresh_tomatoes.py to use while making webpage
		self.title = parsed_details['title']
		self.plot = parsed_details['overview']
		self.poster_image_url = 'http://image.tmdb.org/t/p/w1280' + parsed_details['poster_path']
		self.trailer_youtube_url = parsed_video['results'][0]['key']
