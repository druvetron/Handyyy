"Handyyyy"

A real-time, gesture-based volume control application that uses computer vision to adjust system audio based on hand movements.


INTRODUCTION

This project leverages the power of OpenCV and MediaPipe to create an intuitive way to control your computer's volume. By simply moving your hand in front of a webcam, you can dynamically increase or decrease the volume without needing to use your keyboard or mouse. The application detects the distance between your thumb and index finger, mapping this distance to a corresponding volume level on your system.
FEATURES

    Real-Time Hand Tracking: Uses MediaPipe to accurately detect and track hand landmarks in real-time.

    Gesture-Based Volume Control: Maps the distance between the thumb and index finger to the system volume.

    Visual Feedback: Displays a bounding box around the detected hand and lines between landmarks for a clear visual experience.

    Portable Code: Designed with a separate detector.py module for easy integration into other computer vision projects.

REQUIREMENTS

This project requires Python 3.10 and the packages listed in the environment.yml file.
Installation

Follow these steps to set up the project locally.

    Clone the repository:

    git clone https://github.com/druvetron/Handyyy.git
    cd Handyyy

    Create and activate a Conda environment:

    conda create --name handyyyy python=3.10
    conda activate handyyyy

    Install the required packages:
    The project relies on packages listed in the requirements.txt file. You can install them with the following command:

    pip install -r requirements.txt

USAGE

To run the volume control application, simply execute the volume.py script from your terminal after activating your Conda environment:

python volume.py

A window will appear displaying your webcam feed. To control the volume, move your hand so it's in a comfortable viewing range. The volume will increase as you extend your thumb and index finger apart and decrease as you bring them closer together. To exit the application, press q.

LISENCE

This project is licensed under the MIT License. See the LICENSE file for details.