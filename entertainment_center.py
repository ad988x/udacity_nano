import fresh_tomatoes
import media

"""This file is where the favorite movie variables are determined with the"
" movie title, story line, poster image and youtube trailer"""

ca_first_avenger = media.Movie("Captain America - First Avenger",
                               "Where Steve Rogers becomes the first Avenger",
                               "https://upload.wikimedia.org/wikipedia/en/"
                               "3/37/Captain_America_The_First_Avenger_poster"
                               ".jpg", "https://www.youtube.com/watch?v="
                               "JerVrbLldXw")
avengers = media.Movie("Avengers", "Group of extraordinary people come"
                       "together to fight the worlds battle",
                       "https://upload.wikimedia.org/wikipedia/"
                       "en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

ca_civil_war = media.Movie("Captain America - Civil War", "Cap and"
                           " Iron Man develop teams and fight it out",
                           "https://upload.wikimedia.org/wikipedia/en"
                           "/5/53/Captain_America_Civil_War_poster.jpg",
                           "https://www.youtube.com/watch?v=xnv__ogkt0M")

thor_ragnarok = media.Movie("Thor - Ragnarok", "Thor's world is taken over"
                            " and must come together to defeat the queen",
                            "https://upload.wikimedia.org/wikipedia/en/7/"
                            "7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=TTgNlfAht4I")

guardians_2 = media.Movie("Guardians of the Galaxy Vol.2", "Guardians come"
                          " back to face Peters Dad",
                          "https://upload.wikimedia.org/wikipedia/en/9/95"
                          "/GotG_Vol2_poster.jpg",
                          "https://www.youtube.com/watch?v=2cv2ueYnKjg")

movies = [ca_first_avenger, avengers, ca_civil_war, thor_ragnarok, guardians_2]

"""Create a variable list with all the movie names"""

fresh_tomatoes.open_movies_page(movies)
