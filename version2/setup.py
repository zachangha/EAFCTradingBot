import keyboard

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
# Uncomment the next line if you want to run Chrome in headless mode
# chrome_options.add_argument("--headless")

print("Starting Bot")

# Initialize Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open a webpage (e.g., Google)
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

# Wait for the search box to be present before interacting
# search_box = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "q"))
# )

# # Type a query into the search box
# search_box.send_keys("Selenium WebDriver")

# Submit the search form
# search_box.submit()

while True:
    if keyboard.is_pressed('q'):
        print("Stopping bot")
        break

# Close the browser
driver.quit()
