# This class contains the methods to print the results

import urllib.request, urllib.parse, urllib.error
import json

class Utils:
    def __init__(self, json_data):
        self._json_data = json_data

    def print_json(self):
        list_keys=['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 
                'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Ratings', 
                'Metascore', 'imdbRating', 'imdbVotes', 'imdbID']
        print("-"*50)
        for k in list_keys:
            if k in list(self._json_data.keys()):
                print(f"{k}: {self._json_data[k]}")
        print("-"*50)