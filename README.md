# Crime Scene Capture Application

This project is a Flask-based web application designed to capture images at specific angles for crime scene documentation. The user is guided to take 9 photos at various angles, including flipping the phone. The images are captured via a camera, and the correct angles are validated by the application. Once all images are captured, the user can proceed to the next step.

## Features

- Load and preprocess image datasets.
- Resize images and perform normalization.
- Easy integration into existing machine learning pipelines.
- Flexible configuration for different imaging tasks.

## Requirements

- Python 3.8 or higher
- Required Python packages (can be installed via `requirements.txt`):
  - numpy
  - pandas
  - pillow
  - scikit-learn
  - opencv-python
  - pymongo

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Harshuthoke/API.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd Pre_Imaging_API
   ```

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