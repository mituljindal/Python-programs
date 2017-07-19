import webbrowser

#define the movie class
class Movie():
    """This class provides a way to store information about Movies"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #list of ratings possible

    #Constructor for Movie Class
    def __init__(self, movieTitle, movieStoryline, posterImage, trailerYoutube):
        self.title = movieTitle #Title of the Movie
        self.storyline = movieStoryline #Storyline of the Movie
        self.poster_image_url = posterImage #Link to the Poster
        self.trailer_youtube_url = trailerYoutube #Link to the trailer

    #Function to watch the trailer
    def watch_trailer(self):
        webbrowser.open(self.trailer_youtube_url) #open the trailer in browser

cd ..
