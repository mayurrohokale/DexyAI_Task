<div align="center">
  <h1>Wellfound Message Automation</h1>
  <h4>This project demonstrates the automation of sending messages to Wellfound using a combination of Vite+React for the frontend and Flask with Selenium for the backend. The application allows users to send messages to specific Wellfound threads programmatically.</h4>
</div>

---

## Key Features

- **User-friendly interface** built with Vite+React.
- **Backend automation** using Flask and Selenium.
- **Human-like typing simulation** for enhanced user experience.
- **Secure authentication** with cookies.

---

## How It Works

1. **Frontend**: A React app where users can enter a message and send it to Wellfound.
2. **Backend**: Flask processes the message and uses Selenium to log in to Wellfound and send the message to a specific thread.
3. **Styling**: Basic styling implemented with CSS for a clean and professional look.

---

## Prerequisites

- Node.js and npm installed.
- Python 3.x installed.
- Chrome browser and the corresponding ChromeDriver.

---

## Installation

### Frontend Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd frontend
2. Install dependencies:
   ```bash
   npm install
3. Create a .env file in the root of the frontend folder and add the following:
   ```bash
   VITE_API_URL=http://127.0.0.1:5000
4. Start the Frontend:
   ```bash
   npm run dev

### Backend Setup

1. Navigate to the backend folder:
   ```bash
   cd backend
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
3. Create a .env file in the root of the backend folder and add the following:
   ```bash
   email=xyz@gmail.com
   password=12345xyz
3. Save your Wellfound cookies in a file named cookies.json in the backend folder.
4. Update the CHROMEDRIVER_PATH variable in the backend code with the path to your ChromeDriver.
5. Start the backend:
6. ```bash
   python app.py

### Demonstration Video
https://youtu.be/tEWNLA5mfNw

### Usage
1. Open the frontend application in your browser.
2. Enter a message in the input field.
3. Click the "Send Message" button.
4. View the response below the form, indicating whether the message was successfully sent.

### Additional Notes
1. Ensure that the Wellfound login credentials and cookies are accurate.
2. The application uses Selenium to simulate login and message sending. If CAPTCHA blocks automation, manual intervention may be required.
3. Use the provided .env file to configure the backend URL for seamless integration.

### Troubleshooting
1. CORS Issues: Ensure the Flask-CORS library is configured correctly in app.py.
2. Selenium Errors: Verify the ChromeDriver path and compatibility with your Chrome version.
3. Cookies Error: Ensure that cookies.json contains valid Wellfound cookies.
