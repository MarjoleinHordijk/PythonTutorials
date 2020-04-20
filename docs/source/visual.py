import matplotlib.pyplot as plt
from statistics import mean

# Create the figure.
fig = plt.figure()

# Specify the raw data.
old_scores = [0.30, 0.29, 0.49, 0.48, 0.10, 0.48, 0.38, 0.45, 0.20, 0.30]
new_scores = [0.89, 0.90, 0.70, 0.89, 0.10, 0.80, 0.90, 0.100, 0.80, 0.34]

# Calculate the average insulation scores for both categories.
old_ave = mean(old_scores)
new_ave = mean(new_scores)

# Specify the data for plotting.
categories = ['Old Buildings', 'New Buildings']
scores_ave = [old_ave, new_ave]

# Specify the title and labels.
plt.title("Insulation Score Comparison")
plt.xlabel("Category")
plt.ylabel("Insulation Score")

# Create the bar chart.
plt.bar(categories, scores_ave)

plt.show()