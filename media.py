import webbrowser


class Movie():
    '''
    Sets the data structure for a single movie, which includes the title,
    a link to the poster image, and the link to the trailer on YouTube.
    '''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        ''' Initial function of the class '''
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        ''' Opens the trailer of the movie in a new window '''
        webbrowser.open(self.trailer_youtube_url)
