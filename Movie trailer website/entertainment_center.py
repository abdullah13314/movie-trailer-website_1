# impoting files
import media
import fresh_tomatoes

#Create movie class instances
toy_story = media.Movie("Toy Story", "A story of a boy and his toys as if comes to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4","8.3/10")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY","7.9/10")

lord_of_rings_the_two_towers = media.Movie("Lord of the Rings The Two Towers", "Fordo, a hobbit contiues his quest in destroying the evil being and his ring","http://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg","www.youtube.com/watch?v=2dlRvAjU_RI","8.8/10") 

matrix = media.Movie( "Matrix","Story of a person find out his true identy and starts fighting AI","http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg","www.youtube.com/watch?v=m8e-FF8MsqU","8.7/10")

#Create a list of movie instances
movies = [toy_story, avatar, lord_of_rings_the_two_towers,matrix]

#Calling fresh_tomatoes open_movie page method and passing movie list to it
fresh_tomatoes.open_movies_page(movies)
