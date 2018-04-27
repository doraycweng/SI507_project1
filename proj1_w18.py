import json
import requests
import webbrowser


class Media:

	def __init__(self, title="No Title", author="No Author", year="No Release Year", diction=None, url="No url"):
		self.diction = diction
		if diction == None:
			self.title = title
			self.author = author
			self.year = year
		else:
			if "trackName" in diction.keys():
				self.title = self.diction["trackName"]
			else:
				self.title = self.diction["collectionName"]
			if "trackViewUrl" in diction.keys():
				self.url = self.diction["trackViewUrl"]
			else:
				self.url = self.diction["collectionViewUrl"]
			self.author = self.diction["artistName"]
			self.year = self.diction["releaseDate"][:4]

	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.year)

	def __len__(self):
		return 0


class Song(Media):

	def __init__(self, title="No Title", author="No Author", year="No Release Year", album="No Album", genre="No Genre", length=0, diction=None, url="No url"):
		super().__init__(title, author, year, diction, url)
		if diction == None:
			self.album = album
			self.length = length
			self.genre = genre
		else:
			self.album = self.diction["collectionName"]
			self.length = self.diction["trackTimeMillis"]
			self.genre = self.diction["primaryGenreName"]


	def __str__(self):
		return super().__str__() + "[{}]".format(self.genre)

	def __len__(self):
		return int(self.length / 1000)
		

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", year="No Release Year", rating ="No Rating", length=0, diction=None, url="No url"):
		super().__init__(title, author, year, diction, url)
		if diction == None:
			self.rating = rating
			self.length = length
		else:
			self.rating = self.diction["contentAdvisoryRating"]
			self.length = self.diction["trackTimeMillis"]

	def __str__(self):
		return super().__str__() + "[{}]".format(self.rating)

	def __len__(self):
		return int(round((self.length / 60000),0))

## Other classes, functions, etc. should go here

def get_from_itunes(search_term=""):
	song_list = []
	movie_list = []
	media_list = []
	baseurl = "https://itunes.apple.com/search" 
	parameters = {}
	parameters["term"] = search_term
	parameters["limit"] = 10
	results = requests.get(baseurl, params = parameters)
	results_diction = json.loads(results.text)
	for result in results_diction["results"]:
		if "kind" in result.keys():
			if result["kind"] == "song":
				song_list.append(Song(diction=result))
			elif result["kind"] == "feature-movie":
				movie_list.append(Movie(diction=result))
			else:
				media_list.append(Media(diction=result))
		else:
			media_list.append(Media(diction=result))

	return (song_list, movie_list, media_list)

#print(len(get_from_itunes()[0])+len(get_from_itunes()[1])+len(get_from_itunes()[2]))


if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	exit = False 

	while(True):
		search_term = input('Enter a search term, or "exit" to quit: ')
		if len(search_term) == 0:
			continue
		elif search_term == "exit": 
			print("Bye!")
			exit = True
			break
		else:
			break

	while(not exit):

		results = get_from_itunes(search_term)
		song_list = results[0]
		movie_list = results[1]
		media_list = results[2]
		index = 1 
		result_diction = {}

		if (len(song_list)+len(movie_list)+len(media_list))==0:
			print("No search result")
		else: 
			print ("\n\nSONGS")
			if len(song_list) == 0:
				print("No result for song")
			else:
				for song in song_list:
					print(str(index) + " " + str(song))
					result_diction[index] = song.url
					index += 1

			print("\nMOVIES")
			if len(movie_list) == 0:
				print("No result for movie")
			else:
				for movie in movie_list:
					print(str(index) + " " + str(movie))
					result_diction[index] = movie.url
					index += 1

			print("\nOTHER MEDIA")
			if len(media_list) == 0:
				print("No result for other media")
			else:
				for media in media_list:
					print(str(index) + " " + str(media))
					result_diction[index] = media.url
					index += 1

		while(True):
			answer = input("\n\nEnter a number for more info, or another search term, or exit: ")
			try:
				number_input = int(answer)
				if number_input > len(result_diction) or number_input <= 0:
					print("Please input a valid answer. Try it again.")
					continue
				else:
					print("Launching" + "\n" + result_diction[number_input] + "\n" + "in web browser...")
					webbrowser.open(result_diction[number_input])
					continue
			except:
				if answer == "exit":
					print("Bye!")
					exit = True
					break
				else:
					search_term = answer 
					break











