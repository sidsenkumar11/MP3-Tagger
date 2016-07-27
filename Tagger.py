# Python system libraries
import sys
import os
import urllib.request
import pprint as pp
from shutil import move

# Music database API
import pygn

# Metadata read/write library
from mutagen.id3 import ID3, APIC, error, TRCK, TIT2, TPE1, TALB, TDRC, TCON
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# API keys
clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

def read_files_in_current_directory():

    # Return list of MP3 Files in current directory
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".mp3")]

def get_song_metadata(song_name, artist_name):

    # Query database and get song metadata as a dict
    return pygn.search(clientID=clientID, userID=userID, artist=artist_name, track=song_name)

def write_metadata_to_file(metadict, filename):

    # Write tags to MP3 file
    mp3file = MP3(filename, ID3=EasyID3)
    mp3file['Title'] = metadict["track_title"]
    mp3file['Artist']= metadict["album_artist_name"]
    mp3file['Album']= metadict["album_title"]
    mp3file['TrackNumber'] = metadict["track_number"]
    mp3file['Genre'] = metadict['genre']['1']['TEXT'] # TODO: Write multiple genres
    mp3file['Date'] = metadict["album_year"]
    mp3file.save(filename, v2_version=3, v1=2)

    # Grab Album Art Image from online
    urllib.request.urlretrieve(metadict["album_art_url"], "cover.jpg")
    imagedata = open("cover.jpg", 'rb').read()
    pic = APIC(3, 'image/jpeg', 3, 'Front Cover', imagedata)

    # Save the artwork to the file
    audio = MP3(filename)
    audio.tags.add(pic)
    audio.save(filename, v2_version=3, v1=2)

    # Remove the image from the directory
    os.remove("cover.jpg")

def change_file_name(metadata, song):
    os.rename(song, metadata['track_title'] + " - " + metadata['album_artist_name'] + ".mp3")

def generate_playlists(playlist_specifier):

    # Read in MP3 files in current directory
    songs = read_files_in_current_directory()

    for filename in songs:
        audio = MP3(filename, ID3=EasyID3)

        # Read proper metadata
        try:
            specifier = audio[playlist_specifier][0] # audio is a dict of lists
        except:
            specifier = "Unknown"

        # Create directory if it doesn't exist
        if not os.path.exists(specifier):
            os.makedirs(specifier)

        # The folder exists in the current directory.
        # Move the MP3 file into that folder.
        source = os.path.abspath(filename)
        destination = os.getcwd() + "/" + specifier + "/" + filename
        move(source, destination)

def read_metadata_from_file(filename):
    audio = MP3(filename, ID3=EasyID3)
    pp.pprint(audio)

if __name__=='__main__':

    # Main Functionality
    songs = read_files_in_current_directory()
    for song in songs:
        print("================================")
        print("         METADATA BEFORE        ")
        print("================================")
        read_metadata_from_file(song)

        track_name = input(song + ": Name - ")
        artist_name = input(song + ": Artist - ")
        song_metadata = get_song_metadata(track_name, artist_name)

        pp.pprint(song_metadata)
        ok = input("Is this metadata ok? ")

        if (ok == 'Y'):
            write_metadata_to_file(song_metadata, song)

            print("================================")
            print("         METADATA AFTER         ")
            print("================================")
            read_metadata_from_file(song)
            change_file_name(song_metadata, song)

    # Sort into playlists
    # Possible options: 'Genre', 'Artist', 'Album', 'Date'
    # playlist_option = input("How would you like to sort your music into playlists?\nEnter Genre, Artist, Album, or Date: ")
    # generate_playlists(playlist_option)