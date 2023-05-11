# Web Scraping Automation for extracting table data from a paginated website

This Python code uses the Selenium library to perform web scraping of a table on a paginated website. It extracts data from the search results table on the website using the login credentials provided by the user (if necessary). Then, it saves the extracted data to an Excel file.



## How the code works

1. Importing the necessary libraries:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
```

These are the necessary libraries for automating web scraping. The `webdriver` library is the one that allows the script to control the web browser. The `keys` and `by` are submodules of `webdriver` that assist in interacting with the page. `Pandas` is a library for data manipulation and analysis in Python. `Time` is used to pause between requests.



2. Definition of the WebDriver:

```python
driver = webdriver.Chrome()
```

Here, the WebDriver that will be used to control the Google Chrome browser is defined.



3. Definition of the website and login credentials. Change the "YOUR USERNAME" and "YOUR PASSWORD" fields to the necessary credentials if the website requests them:

```python
site = "https://www.scrapethissite.com/pages/forms/"
#username = "YOUR USERNAME"
#password = "YOUR PASSWORD"
```

In this part, the website to be accessed and the login credentials to be used are defined. In this case, the credentials are commented out because they were not used in the example.



4. Opening the browser and accessing the site for login:

```python
#driver.get(site)
```

This line of code is commented out because it is not necessary to log in to the site in question.



5. Identification of the login and password fields of the website and insertion of the credentials declared above:

```python
#driver.find_element(By.NAME, "login").send_keys(username)
#driver.find_element(By.NAME, "password").send_keys(password, Keys.ENTER)
```

These lines of code are also commented out because they are not necessary in the example.



6. Wait for the page to load:

```python
#time.sleep(1)
```

This line of code causes the script to wait for 1 second before continuing execution.



7. Definition of the number of pages. Change the value of X to the number of pages you want to go through:

```python
num_pages = X
```

This variable defines the number of pages that will be traversed.



8. Initialization of the list to store the data:

```python
data = []
```

This list will be used to store the data extracted from the table.



9. Initialization of the timer:

```python
start_time = time.time()
```

This line of code records the start time of the script's execution.



10. Loop to access each page and extract data:

```python
for pagina in range(1, num_pages + 1):
```

This loop traverses each page of the table and extracts the data.



11. Error handling:

```python
try:
	...
except Exception as e: 
    print(f"Erro on page {pagina}: {str(e)}")
    break
```



12. Next, a loop is started to access each page and extract the data. The number of pages to be accessed is defined previously in the `num_pages` variable. The loop iterates through each page, accessing the corresponding URL, and then locates the table rows using the `driver.find_elements()` function, which finds all elements that match the specified xpath. The rows are iterated one by one, and the information contained in each column is extracted with the `cell.text` function, which returns the text contained in the cell.

```python
for page in range(1, num_pages + 1):
    try:
        # Access the page
        url = f"{site}?page_num={page}"
        driver.get(url)

        # Wait for the page to load
        time.sleep(1)

        # Locate rows
        rows = driver.find_elements(By.XPATH, '/html/body/div/section/div/table/tbody/tr')

        # Loop through each row extracting its data
        for num_pages in range(2, len(rows) + 1):
            row_xpath = f'/html/body/div/section/div/table/tbody/tr[{num_pages}]'
            cells = driver.find_elements(By.XPATH, row_xpath + '/td')
            
            # Save extracted data to respective variables
            team_name, year, wins, losses, ot_losses, win_perc, goals_for, goals_against, more_less = [cell.text for cell in cells]

            # Add data to the list
            data.append([team_name, year, wins, losses, ot_losses, win_perc, goals_for, goals_against, more_less])
    
    # Finish error handling, save collected data and print the last extracted page
    except Exception as e: 
        print(f"Error on page {page}: {str(e)}")
        break
```



13. After the data is collected, the total execution time of the script and the average time per loop are calculated. This information is printed on the screen using the `print()` function.

```python
# Calculate total execution time
total_time = time.time() - start_time

# Calculate average time per loop
average_loop_time = total_time / num_pages

# Print information
print(f"Total execution time: {total_time:.2f} seconds")
print(f"Average loop time: {average_loop_time:.2f} seconds")
```



14. Finally, the collected data is saved to an Excel file using the Pandas library's `to_excel()` function. The `DataFrame()` function is used to create a DataFrame object from the `data` list with named columns corresponding to the information extracted from the table. The file is saved with the name `data.xlsx` in the folder where the script is being executed.

```python
# Save data to an Excel file
df = pd.DataFrame(data, columns=["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For (GF)", "Goals Against (GA)", "+ / -"])
df.to_excel("data.xlsx", index=False)
```



15. Finally, the browser is closed with the `driver.quit()` function.

```python
# Close the browser
driver.quit()
```
