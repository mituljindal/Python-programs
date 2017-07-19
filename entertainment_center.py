import media
import fresh_tomatos

#Initialize class instance variables
#Each variable must have 4 properties
# 1. Movie Title
# 2. Bried Movie Description
# 3. Link to the poster
# 4. Link to the trailer
theDarkKnight = media.Movie("The Dark Knight",
                       "Most epic battle between The Batman and The Joker",
                       "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                       "https://www.youtube.com/watch?v=EXeTwQWrcwY")

theShawshankRedemption = media.Movie("The Shawshank Redemption",
                                     "Story of a man in prison",
                                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                     "https://www.youtube.com/watch?v=NmzuHjWmXOc")

fullMetalJacket = media.Movie("Full Metal Jacket",
                              "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                              "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
                              "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

theBigLebowski = media.Movie("The Big Lebowski",
                             "\"The Dude\" Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",
                             "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                             "https://www.youtube.com/watch?v=ngV0RBhGZmE")

theHatefulEight = media.Movie("The Hateful Eight",
                              "In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters.",
                              "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Hateful_Eight.jpg",
                              "https://www.youtube.com/watch?v=69UwVX6Riv8")

theSilenceOfTheLambs = media.Movie("The Silence of the Lambs",
                                   "A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer who skins his victims.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",
                                   "https://www.youtube.com/watch?v=W6Mm8Sbe__o")

#Initialize a list of movies
movies = [theDarkKnight, theShawshankRedemption, fullMetalJacket, theBigLebowski, theHatefulEight, theSilenceOfTheLambs]
fresh_tomatos.open_movies_page(movies) #Create webpage using fresh_tomatos module
