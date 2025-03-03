
# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Read the CSV file
df = pd.read_csv('alquransurahayatcount.csv')

# %%
# Create figure with larger size
plt.figure(figsize=(20, 10))

# Create bar plot
bars = plt.bar(range(len(df)), df['Ayat'])

# Customize the plot
plt.ylim(0, 300)  # Set y-axis limit to 300
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels vertically and position them
plt.xticks(range(len(df)), df['Surah'], rotation=90, ha='center')

# Flip the x-axis to show data from right to left
plt.gca().invert_xaxis()

# Add labels and title
plt.xlabel('Surah Names')
plt.ylabel('Number of Ayat')
plt.title('Number of Ayat in Each Surah of the Quran')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# %%
# Display the plot
plt.show()
