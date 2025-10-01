import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("outputs/netflix.csv")

type_counts = df['type'].value_counts()


plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color=['#FF6347', '#4682B4'])
plt.title('Number of Movies and TV Shows on Netflix', fontsize=14)
plt.xlabel('Content Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()
