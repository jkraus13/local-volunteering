import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('volunteer_opportunities.csv')

# Filter for Madison opportunities
madison_opportunities = df[df['Location'].str.contains('Madison', na=False)]
num_madison_opportunities = len(madison_opportunities)

# Create the figure and axis
plt.figure(figsize=(6, 4))

# Plot a bar chart
plt.barh('Madison', num_madison_opportunities, color='green')

# Add the exact number of opportunities as text on the bar
plt.text(num_madison_opportunities/2, 'Madison', f"{num_madison_opportunities}",
         va='center', ha='center', fontsize=14, color='white')

# Set the title and labels
plt.title("Volunteer Opportunities in Madison, WI", fontsize=16)
plt.xlabel("Number of Volunteer Opportunities")

# Show the plot
plt.show()
