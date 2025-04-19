import cv2
from ultralytics import YOLO
import RPi.GPIO as GPIO
import time

led1 = 15
GPIO.setmode(GPIO.BOARD)      # Use BCM pin numbering
GPIO.setup(led1, GPIO.OUT) 
servopin = 12
GPIO.setup(servopin, GPIO.OUT)
p = GPIO.PWM(servopin,50)
p.start(0)
time.sleep(1)
closed = 180
opened = 0
def changeAngle(angle):
    p.ChangeDutyCycle(2.5 + 10 * angle / 180)
# Load the trained YOLOv8 model
model = YOLO("best.onnx")
print(model.names)  # Prints a dictionary mapping class IDs to class names
# Open the video file
cap = cv2.VideoCapture(0)
thres = 0.5
# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
GPIO.output(led1, GPIO.LOW)
changeAngle(closed)
position = closed
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (640, 640))
    # Perform object detection
    results = model(frame)

    # Iterate through the results and draw bounding boxes
    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()
        confidences = r.boxes.conf.cpu().numpy()
        class_ids = r.boxes.cls.cpu().numpy()

        for box, conf, class_id in zip(boxes, confidences, class_ids):  # Assuming 0 is the ball class
            if class_id ==0 or class_id == 2:
                if conf > thres:
                    GPIO.output(led1, GPIO.HIGH)
                    changeAngle(opened)
                    x1, y1, x2, y2 = map(int, box)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{model.names[class_id]}: {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    time.sleep(5)
                    position = opened
    GPIO.output(led1, GPIO.LOW)
    if(not(position)):
        changeAngle(closed)
        postion = closed
    time.sleep(0.5)
    # Show the frame with detections
    cv2.imshow("Trash Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        p.stop()
        GPIO.cleanup()
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
