# Crime Scene Capture Application

This project is a Flask-based web application designed to capture images at specific angles for crime scene documentation. The user is guided to take 9 photos at various angles, including flipping the phone. The images are captured via a camera, and the correct angles are validated by the application. Once all images are captured, the user can proceed to the next step.

## Features

- Capture images at specific angles (0°, 30°, 60°, 90°, and after flipping the phone).
- Angle detection with a tolerance of 10°.
- Images are stored in MongoDB using GridFS.
- Visual feedback on the camera screen, including a red guiding line for angle reference.
- A progress tracker showing how many images have been captured.
- Once all images are captured, a "Next" button allows the user to proceed to the next step.

## Technology Stack

- **Backend**: Flask, Flask-PyMongo
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB with GridFS for image storage
- **Dependencies**: OpenCV for angle detection

## Prerequisites

To run this application, you need the following:

1. Python 3.x installed on your system.
2. MongoDB Atlas account and connection details.
3. Camera access enabled on the browser/device.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/crime-scene-capture.git
   cd crime-scene-capture
Install dependencies:

Install the required Python libraries by running:

bash
Copy code
pip install -r requirements.txt
Set up MongoDB Atlas:

Create a MongoDB Atlas account at mongodb.com.
Create a new cluster and database named Image_db.
Replace the MONGO_URI in the app.py file with your own connection string.
Run the application:

Run the Flask app using the following command:

bash
Copy code
python app.py
Access the application:

Open your browser and go to http://127.0.0.1:5000/.

How to Use
When you open the application, you will see a prompt to capture an image at a specific angle (e.g., 0°).
Align your camera according to the angle, and click the "Capture" button.
The app will validate the angle and guide you through the next angles.
After capturing all images, click the "Next" button to proceed to the next step.
Files
app.py: Main Flask application code, handling the backend logic, angle detection, and image uploads.
templates/index.html: Frontend for the camera capture interface, progress tracker, and feedback.
static/css/style.css: Styling for the user interface.
requirements.txt: List of required Python libraries.
Next Steps
After capturing all images, the user is redirected to the following URL: https://api-bcft.vercel.app/. You can modify the logic in app.py for handling the next steps.

Dependencies
Make sure to install the dependencies listed in the requirements.txt file.

License
This project is licensed under the MIT License - see the LICENSE file for details.