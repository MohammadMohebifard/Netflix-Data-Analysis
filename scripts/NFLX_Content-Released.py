import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("outputs/netflix.csv")

year_counts = df['release_year'].value_counts().sort_index()


plt.figure(figsize=(14, 5))
plt.plot(year_counts.index, year_counts.values, color='green', marker='o')
plt.title('Content Released per Year', fontsize=14)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.grid()
plt.show()
