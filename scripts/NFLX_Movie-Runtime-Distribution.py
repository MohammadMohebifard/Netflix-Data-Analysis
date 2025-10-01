import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("outputs/netflix.csv")

movies_df = df[df['type'] == 'MOVIE']

plt.figure(figsize=(10, 6))
plt.hist(movies_df['runtime'], bins=40, color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Runtimes on Netflix')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.show()
