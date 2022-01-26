import webbrowser
from albums import artist_album_list
from album_dtls import artist_album_list_link
import os



while True:
	try:

		for index,artist_album in enumerate(artist_album_list):
			print (index+1,artist_album[0])
		
		index_chosen1 = input("Please choose your favourite artist: ")

		if 1<= int(index_chosen1) <= len(artist_album):
			print("You have provided valid artist selection !!")
			
			
			for index,album in enumerate(artist_album_list[int(index_chosen1)-1][1]):
				print (index+1,album[0])
			
			index_chosen2 = input("Please choose your favourite album: ")
			
			if 1<= int(index_chosen2) <= len(album):
				print("You have provided valid album selection !!")
	
				songlist = artist_album_list[int(index_chosen1)-1][1][int(index_chosen2)-1][1]
				
				for index,songs in enumerate(artist_album_list[int(index_chosen1)-1][1][int(index_chosen2)-1][1]):
					print (index + 1, songs)
				
				index_chosen3 = input("Please choose your favourite song: ")
	
			if 1<= int(index_chosen3) <= len(songlist):
				print("You have provided valid song selection !!")
	
				song_name = artist_album_list[int(index_chosen1)-1][1][int(index_chosen2)-1][1][int(index_chosen3) -1 ]
				print ("Now playing :{}".format(song_name))
				webbrowser.open_new(artist_album_list_link[int(index_chosen1)-1][1][int(index_chosen2)-1][1][int(index_chosen3) -1 ][1])
				
				input_val = input("Please hit enter to close browser and select next song: ")
				if input_val == '':
					os.system("killall -9 'Google Chrome'")
	
			else:
				print("Invalid album selection, Terminating !!")
				exit(1)
			
		else:
			print("Invalid artist selection, Terminating !!")
			exit(1)
	except ValueError:
			print("What the hell are you typing , Terminating !!")
			raise