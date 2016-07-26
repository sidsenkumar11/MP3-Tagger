from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3



def write_metadata(filename, metadict):


# Example which shows how to automatically add tags to an MP3 using EasyID3

	mp3file = MP3(filename, ID3=EasyID3)


	mp3file['Title'] = metadict["Title"]
	mp3file['Artist']= metadict["Artist"]
	mp3file['Album']= metadict["Album"]

	mp3file.save()

