from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv

# Set up Selenium WebDriver (replace with the path to your ChromeDriver)
chrome_driver_path = '/Users/jennakraus/Downloads/chromedriver-mac-x64/chromedriver'  # Your actual ChromeDriver path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage (search results page)
url = 'https://www.volunteermatch.org/search?l=Madison%2C+WI%2C+USA'
driver.get(url)

# Wait for the page to fully load
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser after scraping
driver.quit()

# Find all volunteer opportunities on the main page (use the 'li' elements with the correct class)
opportunity_items = soup.find_all('li', class_='pub-srp-opps__opp')

# Save data to CSV
with open('volunteer_opportunities.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Volunteer Type', 'Organization', 'Location'])  # Headers for volunteer type, organization, and location

    # Loop through the opportunity details and extract information
    for opportunity in opportunity_items:
        # Extracting the volunteer type (title)
        title_element = opportunity.find('a', class_='pub-srp-opps__title')
        volunteer_type = title_element.find('span').text.strip() if title_element and title_element.find('span') else 'N/A'
        
        # Extracting the organization name
        organization_element = opportunity.find('a', class_='blue-drk ga-track-to-org-profile')
        organization = organization_element.text.strip() if organization_element else 'N/A'
        
        # Extracting the location
        location_element = opportunity.find('div', class_='pub-srp-opps__loc')
        location = location_element.text.strip() if location_element else 'N/A'

        # Write the row to CSV
        writer.writerow([volunteer_type, organization, location])

print("Data saved to volunteer_opportunities.csv")
