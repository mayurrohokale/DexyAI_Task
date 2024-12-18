import json
import random
from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask_cors import CORS
from dotenv import load_dotenv
import os 

from time import sleep
app = Flask(__name__)
CORS(app)

load_dotenv()
email=os.getenv("email",None)
password=os.getenv("password",None)

print(email,password)

# Selenium configuration 
CHROMEDRIVER_PATH = 'C:/Users/mayur/OneDrive/Desktop/Dexy_Assignment/chromedriver-win64/chromedriver-win64/chromedriver.exe'

thread_url = 'https://wellfound.com/jobs/messages/966450047'


def human_like_typing(element, text):
    for char in text:
        element.send_keys(char)
        sleep(random.uniform(0.1, 0.3))

def send_message(message: str = None):

    try:

        if not message:
            return {"status": "error", "message": "Message cannot be empty"}
        # init
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        sleep(2)
        
        driver.get("https://wellfound.com/")
        sleep(2) 
        driver.delete_all_cookies()

        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        sleep(5)
        driver.refresh()
        driver.get("https://wellfound.com/login")



        email_input = driver.find_element(By.ID, "user_email")
        password_input = driver.find_element(By.ID, "user_password")
        login_button = driver.find_element(By.NAME, "commit")
        


        print("Typing email...")
        human_like_typing(email_input, email)
        sleep(1)  # Small pause before typing password

        print("Typing password...")
        human_like_typing(password_input, password)
        sleep(1)

       
        print("Clicking login button...")
        login_button.click()
        sleep(5)
        driver.get(thread_url)
        sleep(1)
        message_input_box = None


        try:
            message_input_box = driver.find_element(By.NAME, "response")
        except Exception as error:
            print(error)
            try:
                message_input_box = driver.find_element(By.NAME, "body")
            except Exception as error:
                return {"status": "error", "message": "input box not found "}
        print("Typing message....")
        human_like_typing(message_input_box,message)
        sleep(1)
        send_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        send_button.click()
        sleep(10)
        driver.quit()
        print(f"Message sent successfully, message was {message}, sent to thread url: {thread_url}")
        return {"status": "success", "message": "Message sent successfully"}
    
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Failed to send message"}
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send-message", methods=["GET"])
def runSend_Message():
    message = request.args.get("message")
    if not message:
        return "Please provide a message", 400
    res = send_message(message = message)
    return res,200 if res['status'] == 'success' else 400

if __name__ == "__main__":
    app.run(debug=True)
