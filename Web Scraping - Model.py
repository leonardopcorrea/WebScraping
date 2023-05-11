
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Defining the WebDriver
driver = webdriver.Chrome()

# Defining the site and login credentials
site = "https://www.scrapethissite.com/pages/forms/"
# username = "YOUR USERNAME"
# password = "YOUR PASSWORD"

# Open the browser and access the site for login
# driver.get(site)

# Insert login credentials
# driver.find_element(By.NAME, "login").send_keys(username)
# driver.find_element(By.NAME, "password").send_keys(password, Keys.ENTER)

# Wait for the page to load
# time.sleep(1)

# Define number of pages
num_pages = 4

# Initialize list to store data
data = []

# Initialize timer
start_time = time.time()

# Loop to access each page and extract data
for page in range(1, num_pages + 1):
    
    # Method for error handling
    try:

        # Access the page
        url = f"{site}?page_num={page}"
        driver.get(url)

        # Wait for the page to load
        time.sleep(1)

        # Locate rows
        rows = driver.find_elements(By.XPATH, '/html/body/div/section/div/table/tbody/tr')

        # Loop through each row extracting its data
        for row_num in range(2, len(rows) + 1):
            row_xpath = f'/html/body/div/section/div/table/tbody/tr[{row_num}]'
            cells = driver.find_elements(By.XPATH, row_xpath + '/td')
            
            # Save extracted data to respective variables
            team_name, year, wins, losses, ot_losses, win_perc, goals_for, goals_against, more_less = [cell.text for cell in cells]

            # Add data to the list
            data.append([team_name, year, wins, losses, ot_losses, win_perc, goals_for, goals_against, more_less])
    
    # Finish error handling, save collected data and print the last extracted page
    except Exception as e: 
        print(f"Error on page {page}: {str(e)}")
        break

# Calculate total execution time
total_time = time.time() - start_time

# Calculate average time per loop
average_loop_time = total_time / num_pages

# Print information
print(f"Total execution time: {total_time:.2f} seconds")
print(f"Average loop time: {average_loop_time:.2f} seconds")

# Save data to an Excel file
df = pd.DataFrame(data, columns=["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For (GF)", "Goals Against (GA)", "+ / -"])
df.to_excel("data.xlsx", index=False)

# Close the browser
driver.quit()