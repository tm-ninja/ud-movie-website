import media  #import class media
import fresh_tomatoes  #import fresh_tomatoes module


#Create instance of class movie, Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Create instance of calss movie, Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Create instance of class movie, Ghost in the Shell
ghost_in_the_shell = media.Movie("Ghost in the shell",
                                 "A story of a cyber-woman",
                                 "http://www.impawards.com/2017/posters/ghost_in_the_shell_xlg.jpg",
                                 "https://www.youtube.com/watch?v=tRkb1X9ovI4")

#Create instance of class movie, Hunger Games
hunger_games = media.Movie("Hunger Games",
                           "A serious reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

#Create instance of class movie, Beaty and the Beast
beauty_beast = media.Movie("Beauty and the Beast",
                          "A new classic Disney adaption",
                          "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                          "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

#Create instance of class movie, Lord of the Ring
lord_rings = media.Movie("Lord of the Rings | The Fellowship of the Ring",
                         "An adventure across middle earth",
                         "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=V75dMMIW2B4")
                                                

#create array for fresh_tomatoes.py to work it's magic                          
movies = [toy_story, avatar, ghost_in_the_shell, hunger_games, beauty_beast, lord_rings]
fresh_tomatoes.open_movies_page(movies)  
