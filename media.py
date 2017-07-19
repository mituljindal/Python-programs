import webbrowser

class Movie():
    def __init__(self, movieTitle, movieStoryline, posterImage, trailerYoutube):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube

    def watch_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

