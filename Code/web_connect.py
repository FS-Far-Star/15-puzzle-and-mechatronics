from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import autoit

def send_instructions(): 

    # Initialize the web driver (make sure you have the driver installed and in PATH)
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get("http://192.168.1.88/")

    # Wait for 10 seconds for the website to load
    time.sleep(10)

    # Find and click the Upload button
    upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Upload')]")
    upload_button.click()

    # Wait for the file explorer to open
    time.sleep(2)

    # Use AutoIt to handle the file upload dialog
    autoit.send("C:\\Users\\Wraith\\Desktop\\Project\\Code\\output.gcode")
    autoit.send("{ENTER}")
    print('Found document and uploaded')

    # Wait for a few seconds to ensure the file is uploaded
    time.sleep(10)

    # Find the button based on class name and onclick behavior
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-xs btn-default' and contains(@onclick, 'files_print(0)')]")

    # Click the button if found
    if button:
        button.click()
    else:
        print("Button not found.")

    # Ask for an input to prevent closing the website
    input("Press Enter to exit...")

    # Keep the browser window open
    return None

if __name__ == '__main__':
    send_instructions()