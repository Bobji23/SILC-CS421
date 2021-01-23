class FAV_MOVIES:
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies

    def __repr__(self):
        return 'MOVIE(list_of_movies=%s)' % (self.list_of_movies)

    def __str__(self):
        return 'FAV_MOVIES(list_of_movies=%s)' % (self.list_of_movies)






class MOVIE_CLASS:
    def __init__(self, MOVIE_CLASS):
        self.MOVIE_CLASS = MOVIE_CLASS

    def __repr__(self):
        return 'MOVIE_CLASS(list_of_movies=%s)' % (self.MOVIE_CLASS)

    def __str__(self):
        return 'MOVE_CLASS(movies=%s)' % (self.MOVIE_CLASS)



class Movie:
    def __init__(self, name, release_date, length):
        self.name = name
        self.release_date = release_date
        self.length = length

    def __repr__(self):
        return 'Movie(name=%s, release_date=%s, time=%s)' % (self.name, self.release_date, self.length)

    def __str__(self):
        return 'Movie(name=%s, release_date=%s, time=%s)' % (self.name, self.release_date, self.length)



class Director:
    def __init__(self, name, age, birthdate):
        self.name = name
        self.age = age
        self.birthdate = birthdate

    def __repr__(self):
        return 'Director(name=%s, release_date=%s, time=%s)' % (self.name, self.age, self.birthdate)

    def __str__(self):
        return 'Director(name=%s, release_date=%s)' % (self.name, self.age)





movie1 = Movie("Jumanji", "12/13/2019", "1h 59m")



movie2= Movie("Black Panther", "1/29/2019", "2h 15m")



movie3 = Movie("Avengers Endgame", "4/26/2019", "3h 2m")




director1 = Director("Jake Kasdan", 46, "8/28/1974")



director2 = Director("Ryan Coogler", 34, "5/23/1986")




director3 = Director("Anthony Russo", 50, "2,3,1950")




director_list = [director1, director2, director3]
movie_class = MOVIE_CLASS(director_list)




more_movie = [movie1, movie2]
more_class = MOVIE_CLASS(more_movie)



list_of_classes = [more_class, more_class]
my_fav_movies = FAV_MOVIES(list_of_classes)





print("Favorite Movies --> ", my_fav_movies)
