import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv", index_col=0)

# Movies released in the 1990s

print("Movies released in the 1990s:")
movies = netflix_df.iloc[:, 0] == "Movie"
is_1990s = np.logical_and(netflix_df.iloc[:, 6] >= 1990, netflix_df.iloc[:, 6] < 2000)  

movies_released_1990s = netflix_df[movies & is_1990s]
print(movies_released_1990s)

duration = int(movies_released_1990s.iloc[:, 7].mode().iloc[0])
print("Most frequent movie duration in the 1990s: ", duration)

# Short action movies released in the 1990s

print("\nShort action movies released in the 1990s:")
duration_col = (netflix_df.iloc[:, 7] < 90)
genre = netflix_df.iloc[:, -1] == "Action"

short_movies_released_1990s = netflix_df[movies & is_1990s & duration_col & genre]
print(short_movies_released_1990s)

short_movie_count = int(len(short_movies_released_1990s))
print("Number of short action movies released in the 1990s: ", short_movie_count)

# Histogram movies duration in the 1990s

plt.hist(movies_released_1990s.iloc[:, 7], bins=20, color='blue', edgecolor='black')
plt.title('Histogram Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()