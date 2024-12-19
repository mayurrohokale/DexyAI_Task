import json
import random
from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask_cors import CORS


from time import sleep
app = Flask(__name__)
CORS(app)



# Selenium configuration 
CHROMEDRIVER_PATH = 'C:/Users/mayur/OneDrive/Desktop/Dexy_Assignment/Backend/chromedriver-win64/chromedriver-win64/chromedriver.exe'

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

        cookie_fields = ["name","value","expiry"]

        with open('cookies.json','r')as f:
            cookies = json.load(f)
            for cookie in cookies:

                updated = {
                    k: v
                    for k, v in cookie.items()
                    if v is not None
                    and k
                    in cookie_fields
                }
                if "expirationDate" in cookie:
                    updated["expiry"] = int(cookie["expirationDate"])

                print(f"Adding cookies for: {updated['name']}")
                try:
                    driver.add_cookie(updated)
                except Exception as e:
                    print(f"Error adding cookie {updated['name']}: {str(e)}")
                
        

        sleep(5)
        driver.refresh()
      
        sleep(1)
        driver.execute_script("window.scrollTo(0, Math.random() * 0.4 * window.innerHeight + 0.5 * window.innerHeight);")
        
        sleep(2)
        
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
        sleep(2)
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

@app.route("/send-message", methods=["GET"])
def runSend_Message():
    message = request.args.get("message")
    if not message:
        return "Please provide a message", 400
    res = send_message(message = message)
    return res,200 if res['status'] == 'success' else 400

if __name__ == "__main__":
    app.run(debug=True)
