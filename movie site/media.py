import movie
import fresh_tomatoes

ddlj = movie.Movie("ddlj" ,"love story from London to India",
                        "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                        "https://www.youtube.com/watch?v=c25GKl5VNeY")


dtph = movie.Movie("Dil To Pagal Hai", "Love story",
                   "https://upload.wikimedia.org/wikipedia/en/9/9d/Dil_To_Pagal_Hai.jpg",
                   "https://www.youtube.com/watch?v=BdhPleFcEJ0")


bandtb = movie.Movie("Beauty and the Beast", "love story between beaty girl and beast animal",
                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=OvW_L8sTu5E")
#print(bandtb.storyline)
# bandtb.play_trailer()
moon_light = movie.Movie("Moon Light", "Three stages of life",
                         "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",
                         "https://www.youtube.com/watch?v=9NJj12tJzqc")

midnight_in_paris = movie.Movie("Midnight in Paris","story of movie",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")
avatar = movie.Movie("Avatar", "Love story",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

movies = [ddlj, dtph, bandtb, moon_light, midnight_in_paris, avatar]
fresh_tomatoes.open_movies_page(movies)
#print(movie.Movie.RATING_MOVIE)
#print(movie.Movie.__doc__)
#print(bandtb.title)
