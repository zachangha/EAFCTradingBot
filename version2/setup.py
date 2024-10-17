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
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--remote-debugging-port=9222")

# chrome_profile_path = "C:/Users/zsang/AppData/Local/Google/Chrome/User Data"  # Adjust this path
# chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
# chrome_options.add_argument("profile-directory=Default")

print("Starting Bot")

# Initialize Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open a webpage (e.g., EA Sports Web App)
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

# Wait for the login button to be present before interacting
login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn-standard"))
)

# Click the login button
login.click()

while True:
    if keyboard.is_pressed('q'):
        print("Stopping bot")
        break

# Close the browser
driver.quit()
