import media
import fresh_tomatoes

# Creation of the instances of the 'Movie' class. 
a_beatiful_mind = media.Movie('A Beautiful Mind', 
                              'http://www.egobene.com/wp-content/uploads/'
                              '2017/04/COPERTINA-e1489050980422.jpg', 
                              'https://youtu.be/WFJgUm7iOKw')

source_code = media.Movie('Source Code', 
                          'https://pre00.deviantart.net/3756/th/pre/i/2011'
                          '/162/d/a/source_code_poster_by_alecx8-'
                          'd3ime86.jpg', 
                          'https://youtu.be/zDMXC0nLaxI')

immitation_game = media.Movie('The Immitation Game', 
                          	  'http://www.impawards.com/2014/posters/imitation'
                          	  '_game_ver6.jpg', 
                              'https://youtu.be/sdMIi6bwWVk')

underground = media.Movie('Underground',
                          'http://img.moviepostershop.com/underground-movie-'
                          'poster-1995-1010200919.jpg', 
                          'https://youtu.be/iKdl5r7_ZPc')

dead_poets = media.Movie('Dead Poets Society', 
                         'https://pics.filmaffinity.com/Dead_Poets_Society-'
                         '830145615-large.jpg', 
                         'https://youtu.be/aQwVQzs9pHk')

interstellar = media.Movie("Interstellar", 
                           "https://pre00.deviantart.net/a570/th/pre/f/"
                           "2014/213/3/b/interstellar__2014____poster___2_by_"
                           "camw1n-d7t74io.png", 
                           "https://youtu.be/z_1mjTV1gLw")

# All the instances are collected in the list
movies = [a_beatiful_mind, source_code, immitation_game, underground, 
          dead_poets, interstellar]

# Calls the function that generates and opens a webpage with movies from the list
fresh_tomatoes.open_movies_page(movies)