from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

# Load phone numbers from CSV file
df = pd.read_csv('test.csv')  # Make sure your CSV has a "Phone Number" column

# Set up Chrome options for Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=./User_Data')  # Save session for WhatsApp login persistence

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for user to scan the QR code manually
input("Press Enter after you have scanned the QR code in WhatsApp Web...")

# Loop through all the phone numbers in the CSV
for index, row in df.iterrows():
    phone_number = row['phone_number']
    full_name = row['full_name']
    message = f"Hello {full_name}, I'm Saher Mohamed, the president of the 🤎 *Ryzen IT Club* 🤍. I invite you to join our *announcement group* to keep updated with the next check-in date. Our group: https://chat.whatsapp.com/EHfYvGLjbTm4bR6rlimhdZ"  # Customize your message

    # Construct WhatsApp URL for messaging
    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"

    # Open the WhatsApp chat for the phone number
    driver.get(url)

    # Wait for the page to load
    sleep(10)  # Adjust this time based on your internet speed
    try:
        # Find the send button and click it
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}. Error: {e}")

    # Wait a little before sending the next message
    sleep(5)

# Close the browser once done
driver.quit()
