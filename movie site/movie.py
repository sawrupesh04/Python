import webbrowser
class Movie():
    """ this is the movie site programming """
    RATING_MOVIE = ["G", "G+", "GP", "GP+"]
    def __init__(self,movie_title,movie_story_line, poster_image_url, youtube_url_link):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url_link

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        


