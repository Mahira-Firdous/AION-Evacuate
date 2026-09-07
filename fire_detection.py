import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

def process_fire(frame, mask):
    m = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    m = cv2.dilate(m, kernel, iterations=2)

    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 4000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(frame, "FIRE!", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.GaussianBlur(frame, (7,7), 0)

    # ----------------------------
    # 🧠 YOLO PERSON DETECTION
    # ----------------------------
    results = model(frame)

    mask_person = np.zeros(frame.shape[:2], dtype=np.uint8)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # class 0 = person
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(mask_person, (x1, y1), (x2, y2), 255, -1)

    # Remove person region
    frame_no_person = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask_person))

    # ----------------------------
    # 🔥 FIRE DETECTION (HSV)
    # ----------------------------
    hsv = cv2.cvtColor(frame_no_person, cv2.COLOR_BGR2HSV)

    fire_lower = np.array([0, 100, 120])
    fire_upper = np.array([25, 255, 255])
    fire_mask = cv2.inRange(hsv, fire_lower, fire_upper)

    process_fire(frame, fire_mask)

    # ----------------------------
    # DISPLAY
    # ----------------------------
    cv2.imshow("Final Output", frame)
    cv2.imshow("Fire Mask", fire_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()