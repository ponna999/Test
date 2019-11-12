import media
import fresh_tomatoes

love_movie = media.Movies("Geetha Govindam",
                         "Geetha Govindam is an INDIAN classical Love story",
                         "https://moviegalleri.net/2018/06/vijay-devarakonda-rashmika-mandanna-geetha-govindam-first-look-poster-hd.html",
                         "https://www.youtube.com/watch?v=OYK2eJ0oeg8")

comedy_movie = media.Movies("Express Raja",
                            "Express raja is a decent love story with full of comedy",
                            "https://www.indiaglitz.com/express-raja-photos-telugu-movies-2553987-20291",
                            "https://www.youtube.com/watch?v=vtnKfhqEumk")


movie = [love_movie,comedy_movie]
fresh_tomatoes.open_movies_page(movie)