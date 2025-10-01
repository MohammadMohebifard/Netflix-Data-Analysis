import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("outputs/netflix.csv")


age_counts = df['age_certification'].value_counts().sort_values(ascending=False)


plt.figure(figsize=(8, 6))
plt.bar(age_counts.index, age_counts.values, color='orange', edgecolor='black')
plt.title('Distribution of Age Certifications on Netflix')
plt.xlabel('Age Certification')
plt.ylabel('Number of Titles')
plt.grid(axis='y')
plt.tight_layout()
plt.show()