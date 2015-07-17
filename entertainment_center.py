__author__ = 'ali786'

import media
import website_generator

# Creating instances of Movie class and these movies will show up on the web page
virgin_snow = media.Movie("Virgin Snow", "Returning to Japan, a man tries to find the beautiful woman who captured his heart.", "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Virgin_Snow_%28film%29.jpg/220px-Virgin_Snow_%28film%29.jpg", "https://www.youtube.com/watch?v=P2mRL3ZBfp0", "Romance")
paradise_kiss = media.Movie("Paradise Kiss", "A heartwarming love story.", "https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Paradise_Kiss_Movie_Poster.jpg/220px-Paradise_Kiss_Movie_Poster.jpg", "https://www.youtube.com/watch?v=zkH_4nDmOTM", "Romance")
laundry = media.Movie("Laundry", "Sensitive, romantic and heart-touching tale of a pure soul.", "http://asianwiki.com/images/a/aa/Laundryposter.jpg", "https://www.youtube.com/watch?v=1At_7Y3rNIE", "Slice of Life")
a_millionaires_first_love = media.Movie("A Millionaire's First Love", "A story showcasing that Nothing is more important than the true love of one's heart.", "https://upload.wikimedia.org/wikipedia/en/thumb/d/da/A_Millionaire%27s_First_Love.jpg/220px-A_Millionaire%27s_First_Love.jpg", "https://www.youtube.com/watch?v=k-JQ797aBwc", "Romance")
a_moment_to_remember = media.Movie("A Moment to Remember", "A tale of discovery in a relationship and the burdens of loss caused by Alzheimer's disease.", "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/A_Moment_to_Remember_Poster.jpg/220px-A_Moment_to_Remember_Poster.jpg", "https://www.youtube.com/watch?v=LFLSwFEiANg", "Romance")
the_wings_of_the_bird = media.Movie("The Wings of the Kirin", "A thriller detective story with subtle philosophical moments", "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/The_Wings_of_the_Kirin_film_poster.jpg/220px-The_Wings_of_the_Kirin_film_poster.jpg", "https://www.youtube.com/watch?v=IMvnC2GjbGs", "Thriller")

# Creating a list of the movie objects
favourite_movies = [virgin_snow, paradise_kiss, laundry, a_millionaires_first_love, a_moment_to_remember, the_wings_of_the_bird]

# Calling the generator for the web page
website_generator.open_movies_page(favourite_movies)