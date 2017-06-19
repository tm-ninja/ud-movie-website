import webbrowser  #Used to show movie trailers


class Movie():  #Build class movie

    #Docstring, contains information about class Movie.
    #Can be called using print(media.Movie.__doc__)
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  #Test Class variables 

    #Class movie constructor                 
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        #Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  #Instance method
        webbrowser.open(self.trailer_youtube_url)
        
        
    
    
