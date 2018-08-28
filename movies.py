# This class contains the methods to search the movies

import urllib.request, urllib.parse, urllib.error
import json
from utils import Utils

class Movies:
    def __init__(self, movie, option):
        self._movie = movie
        self._option = option
        self._omdbapi = '3d8762a6'
        self._serviceurl = 'http://www.omdbapi.com/?'
        self._apikey = '&apikey='+self._omdbapi
    
    def search_movie(self):
        try:
            url = self._serviceurl + urllib.parse.urlencode({self._option: self._movie})+self._apikey
            print(f'Retrieving the data of "{self._movie}" now... ')
            uh = urllib.request.urlopen(url)
            data = uh.read()
            json_data=json.loads(data)
        
            if json_data['Response']=='True':
                movie_details = Utils(json_data);
                movie_details.print_json()            
            else:
                print("Error encountered: ",json_data['Error'])
        except urllib.error.URLError as e:
            print(f"ERROR: {e.reason}")
 