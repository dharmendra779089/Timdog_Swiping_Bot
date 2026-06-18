# Import the main tool that allows Python to control a web browser like a robot.
from selenium import webdriver

# Import 'By', which gives us different ways to search for elements on the webpage (like ID, XPATH, or CLASS_NAME).
from selenium.webdriver.common.by import By

# Import 'Keys', which lets us simulate pressing keys on a keyboard (like the Enter key or Spacebar).
from selenium.webdriver.common.keys import Keys

# Import specific error types. We use these later as safety nets so our code doesn't crash if it can't find a button or if a button is blocked.
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# Import 'sleep' so we can tell our script to pause for a few seconds to let web pages load.
from time import sleep

# --- VARIABLES ---
# Store the website address we want our robot to visit.
TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/W5cnmn3crNjVMLmHgAQFmogbA1TsjUg-"

# Store the fake Facebark email address.
FACEBARK_EMAIL = "sumankumarmehta82@gmail.com"

# Store the fake Facebark password.
FACEBARK_PASSWORD = "Ds@9576857353"

# --- BROWSER SETUP ---
# Launch a new Google Chrome browser window that is controlled by our code.
driver = webdriver.Chrome()

# Tell the browser to navigate to the Tindog website URL we saved earlier.
driver.get(TINDOG_URL)

# --- STEP 1: OPEN THE LOGIN MODAL ---
# Pause for 2 seconds to ensure the main page has fully loaded on the screen.
sleep(2)

# Search the page using XPATH for any element containing the exact text "Log in", and click it.
driver.find_element(By.XPATH, value='//*[text()="Log in"]').click()

# Pause for 1 second to let the login popup menu slide into view.
sleep(1)

# Search for the specific button that has the class name 'btn-facebark' and click it to trigger the Facebook-style login.
driver.find_element(By.CLASS_NAME, value='btn-facebark').click()

# --- STEP 2: FACEBARK LOGIN IN POPUP ---
# Pause for 2 seconds to give the new Facebark popup window time to open and load.
sleep(2)

# 'driver.window_handles' is a list of all currently open windows/tabs. Index [0] is the original Tindog window. We save it as 'base_window'.
base_window = driver.window_handles[0]

# Index [1] is the newly opened Facebark popup window. We save it as 'facebark_window'.
facebark_window = driver.window_handles[1]

# Tell Selenium to move its focus from the main page to the new Facebark popup window so we can interact with it.
driver.switch_to.window(facebark_window)

# Print the title of the current window to the console just to verify we are actually in the "Facebark" window.
print(driver.title)

# Find the input box for the email by its HTML ID ('email').
email = driver.find_element(By.ID, value='email')

# Find the input box for the password by its HTML ID ('pass').
password = driver.find_element(By.ID, value='pass')

# Type the fake email address into the email input box.
email.send_keys(FACEBARK_EMAIL)

# Type the fake password into the password input box.
password.send_keys(FACEBARK_PASSWORD)

# Simulate pressing the "ENTER" key on the keyboard to submit the login form.
password.send_keys(Keys.ENTER)

# Now that we are logged in, the popup closes. Tell Selenium to switch its focus back to the original Tindog window.
driver.switch_to.window(base_window)

# Print the title of the current window to verify we are back on "Tindog".
print(driver.title)

# --- STEP 3: DISMISS THE THREE POPUPS ---
# Pause for 3 seconds to give the Tindog app time to log us in and load the first set of popups.
sleep(3)

# Find the button containing the exact text "Allow" (usually for location permissions) and click it.
driver.find_element(By.XPATH, value='//button[text()="Allow"]').click()

# Pause for 1 second before the next popup.
sleep(1)

# Find the button containing the exact text "Not interested" (usually for notifications) and click it.
driver.find_element(By.XPATH, value='//button[text()="Not interested"]').click()

# Pause for 1 second before the final popup.
sleep(1)

# Find the button containing the exact text "I Accept" (usually for cookies/terms) and click it.
driver.find_element(By.XPATH, value='//button[text()="I Accept"]').click()


# --- STEP 4: LIKE ALL 20 DOGS ---
# Start a loop that will run exactly 20 times (from 0 to 19).
for n in range(20):
    # Pause for 1 second to let the dog's picture and profile fully slide onto the screen.
    sleep(1)
    
    # 'try' means Python will attempt the code below. If it crashes, it drops to the 'except' blocks instead of breaking the script.
    try:
        # Find the heart/like button using its class name 'btn-like'.
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        
        # Click the like button.
        like_button.click()
        
    # If the click fails because another element is covering the button (like a "You got a Match!" popup)...
    except ElementClickInterceptedException:
        
        # We try another block of code specifically to handle the annoying match popup.
        try:
            # Find the "Keep Swiping" or "Close" link inside the match popup using its CSS selector and click it.
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
            
        # If we can't find that close button inside the popup for some reason...
        except NoSuchElementException:
            # Just pause for 2 seconds to let things settle, then the loop will try again.
            sleep(2)
            
    # If the original 'like_button' couldn't be found at all (maybe the page is lagging or we ran out of dogs)...
    except NoSuchElementException:
        # Pause for 2 seconds to give it a chance to load before the loop starts its next cycle.
        sleep(2)

# Once the loop has run 20 times, close the entire Chrome browser and end the program.
driver.quit()