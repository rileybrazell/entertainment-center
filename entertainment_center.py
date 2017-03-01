import media
import fresh_tomatoes


# Add all new movies as a media.Movie objects below this line
# movie_title = media.Movie(rating, title, year, plot, poster image, trailer url)
lost_in_translation = media.Movie("R", "Lost in Translation", "2003",
						"A faded movie star and a neglected young woman form an unlikely bond \
						 after crossing paths in Tokyo.",
						"http://bit.ly/2k8KwLh",
						"https://www.youtube.com/watch?v=W6iVPCRflQM")

song_of_the_sea = media.Movie("PG", "Song of the Sea", "2014",
					 "Ben, a young Irish boy, and his little sister Saoirse, a girl \
					 	who can turn into a seal, go on an adventure to free the faeries \
					 	and save the spirit world.",
					 "http://bit.ly/2lq4VNb",
					 "https://www.youtube.com/watch?v=HgbXWt8kM5Q")

trollhunter = media.Movie("PG-13", "Troll Hunter", "2010",
						  "University students track trolls",
						  "http://bit.ly/2mEO9ab",
						  "https://www.youtube.com/watch?v=vy2nAOdBUlw")

ponyo = media.Movie("G", "Ponyo", "2008",
					"A five year-old boy develops a relationship with Ponyo, a goldfish \
						princess who longs to become a human after falling in love with him.",
					"http://bit.ly/2lUmv9Y",
					"https://www.youtube.com/watch?v=bskgNOXbdiE")

moana = media.Movie("PG", "Moana", "2016",
					"In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui \
						reaches an impetuous Chieftain's daughter's island, she answers the \
						Ocean's call to seek out the Demigod to set things right.",
					"http://bit.ly/2kwgxyV",
					"https://www.youtube.com/watch?v=LKFuXETZUsI")

bee_movie = media.Movie("PG", "The Bee Movie", "2007",
						"Bee movie but everytime you watch it, it gets worse",
						"http://bit.ly/2kPYuzC",
						"https://www.youtube.com/watch?v=VONRQMx78YI")

# Put all movies into a list
movies = [lost_in_translation, song_of_the_sea, trollhunter, ponyo, moana,
			bee_movie]

# Pass list of movies over to fresh_tomatoes to create webpage
fresh_tomatoes.open_movies_page(movies)
