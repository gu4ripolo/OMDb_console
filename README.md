# OMDb_console

## Steps to run the app.

1. Run the file main.py in the console

2.- The following menu will display:

```
Enter '1' to search all of the movies by title.
Enter '2' to search a movie by id.
Enter '3' to search a movie by title.
Enter 'q' to quit.
Select an option: 
```
3. Once the option is selected enter the movie name or the movie id. For Example:

```
Select an option: 3

Enter the title of a movie (enter 'quit' or hit ENTER to quit): Activision: STEM - in the Videogame Industry
```

4.- The output for this example would be the following

```
Enter the title of a movie (enter 'quit' or hit ENTER to quit): Activision: STEM - in the Videogame Industry
Retrieving the data of "Activision: STEM - in the Videogame Industry" now... 
--------------------------------------------------
Title: Activision: STEM - in the Videogame Industry
Year: 2010
Rated: N/A
Released: 23 Nov 2010
Runtime: 3 min
Genre: Short
Director: Mike Feurstein
Writer: N/A
Actors: Max Gaba, Josh Kahn, Chad J. Miller, Lukas Morgan
Plot: N/A
Language: English
Country: USA
Awards: N/A
Ratings: []
Metascore: N/A
imdbRating: N/A
imdbVotes: N/A
imdbID: tt1810525
--------------------------------------------------
```

5. Enter an option to search for another movie or enter 'q' to quit:

```
Select an option: q
```

## Files description

Main.py - contains the user menu.
Utils.py - contains the method used to print the data.
Movies.py - contains the method to use api.
