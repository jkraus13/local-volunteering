import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('volunteer_opportunities.csv')

# Set the headers for the table columns (you can adjust these as needed)
df.columns = ['Volunteer Type', 'Organization', 'Location']

# Display the table in a nicely formatted way
print(df)

# If you want to display the table in a GUI or save it as a file
df.to_html('volunteer_opportunities_table.html')

# This would save the table to an Excel file
df.to_excel('volunteer_opportunities_table.xlsx', index=False)

print("Table created and saved to HTML and Excel.")
