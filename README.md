SmartSort: AI-Powered Recycling Bot
SmartSort is an AI-driven recycling assistant that automatically detects recyclable items like plastic bottles and aluminum cans, helping promote smarter and cleaner recycling.

📚 Inspiration
Walking around campus, we noticed many recyclable items being tossed into the trash. We wanted to create a system that uses AI to recognize recyclable materials and sort them correctly, making recycling easier for everyone.

🚀 What It Does
Uses a camera and a trained YOLOv8 model to detect objects.

Classifies items as:

Plastic Bottle

Aluminum Can

General Waste

Activates a servo mechanism to direct items into the recyclable bin.

Lights up an LED indicator when a recyclable item is detected.

🛠️ How We Built It
Dataset: Collected custom images + used online datasets.

Model Training: Trained a YOLOv8 model on the Mason Hopper Cluster.

Deployment: Deployed the model to a Raspberry Pi connected to a camera.

Hardware: Used servos and an Arduino to display a welcome message.


🧠 Challenges We Ran Into
Difficulties in reliable communication between Raspberry Pi and Arduino (sending signals).

Mechanical challenges: initial design with a rotating platform using a stepper motor failed due to torque issues; had to redesign for stability and simplicity.

🏆 Accomplishments
Successfully trained and deployed an accurate object detection model.

Built a real-world AI-powered sorting mechanism.

Integrated real-time LED feedback for users.

Overcame major technical and mechanical obstacles to deliver a working prototype.

📖 What We Learned
Persistence matters — things rarely go exactly as planned.

Adaptability is crucial — sometimes redesigning is the best path forward.

Team collaboration — combining AI, hardware, and mechanical design required strong cross-functional teamwork.

🔮 What's Next
Add multiple servo mechanisms to sort into three separate bins (bottles, cans, waste).

Refine the design for better durability and aesthetics.

Further fine-tune the model for real-world conditions.

Deploy SmartSort in public spaces like universities, airports, and parks.

🛠️ Built With
Python

Raspberry Pi

Arduino

Roboflow

YOLOv8

🎯 Try It Out
Want to build your own SmartSort? Here's how you can get started:

Requirements
Raspberry Pi (any 4GB+ model recommended)
Raspberry Pi Camera Module (or compatible USB camera)
Arduino (Uno, Nano, or similar)
Servo motors 
LED (optional for feedback)
Jumper wires, breadboard, power supply
3D printed or cardboard frame (for building the sorting mechanism)

Installation

1. Clone the Repository

git clone https://github.com/cheyennebejj123/smartsort.git

2. Install Required Python Libraries

pip install -r requirements.txt

3. Set Up the Camera

4. Enable camera support on Raspberry Pi (raspi-config).

5. Test the camera using raspistill or a simple OpenCV script.

6. Upload Arduino Code and rasbperry PI

7. Run SmartSort
   
python smartsort.py

8. Place an Item

Hold a plastic bottle, can, or trash item in front of the camera.

Watch SmartSort detect the item and automatically sort it into the correct bin
