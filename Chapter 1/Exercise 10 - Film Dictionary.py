#create a dictionary representing a movie
movie = {
    "Title": "Avengers",
    "Director": "Joe Johnston",
    "Year": "2011",
    "Genre": "Action",
}
#iterate throught the dictionary and print each key value
print("\nThe Avengers: ")
for key, value in movie.items():
    print(f"{key}: {value}")