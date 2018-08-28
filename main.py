# This is the main class

from movies import Movies

def userMenu():
    print("Enter '1' to search all of the movies by title.\nEnter '2' to search a movie by id.\nEnter '3' to search a movie by title.\nEnter 'q' to quit.")
    userinput = input("Select an option: ")

    while userinput != 'q':

        if userinput == '1':
            title = input('\nEnter the title of a movie (enter \'quit\' or hit ENTER to quit): ')
            ob = Movies(title,'s')
            if len(title) < 1 or title=='quit': 
                print("Goodbye now...")
            else:
                ob.search_movie()
        elif userinput == '2':
            title = input('\nEnter the id of a movie (enter \'quit\' or hit ENTER to quit): ')
            ob = Movies(title,'i')
            if len(title) < 1 or title=='quit': 
                print("Goodbye now...")
            else:
                ob.search_movie()
        elif userinput == '3':
            title = input('\nEnter the title of a movie (enter \'quit\' or hit ENTER to quit): ')
            ob = Movies(title,'t')
            if len(title) < 1 or title=='quit': 
                print("Goodbye now...")
            else:
                ob.search_movie()
        else:
            print("Invalid option")

        userinput = input("\nSelect an option: ")
        
userMenu()
