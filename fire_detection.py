import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # Convert to HSV - This is the "Eyes" of the AI
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # -----------------------------
    # 🔥 1. REFINED FIRE DETECTION
    # -----------------------------
    # Lower range: Very bright yellow/orange | Upper range: Deep red
    fire_lower = np.array([0, 100, 120])
    fire_upper = np.array([25, 255, 255])
    fire_mask = cv2.inRange(hsv, fire_lower, fire_upper)

    # -----------------------------
    # 🌫️ 2. REFINED SMOKE DETECTION
    # -----------------------------
    # Smoke has VERY low saturation (gray). We use a tight S range (0-40)
    # and a medium Brightness (V) range (80-200) to ignore white walls.
    smoke_lower = np.array([0, 0, 80])
    smoke_upper = np.array([180, 40, 200])
    smoke_mask = cv2.inRange(hsv, smoke_lower, smoke_upper)

    # -----------------------------
    # 🧹 3. CLEANING & LOGIC
    # -----------------------------
    kernel = np.ones((5, 5), np.uint8)
    
    def process_and_draw(mask, label, color, min_area):
        # Remove small dots (noise)
        m = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts:
            area = cv2.contourArea(c)
            if area > min_area: # Only show large patches
                x, y, w, h = cv2.boundingRect(c)
                # Logic: Fire/Smoke is usually taller than it is wide or irregular
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Apply detection: Smoke needs a larger area to trigger than Fire
    process_and_draw(fire_mask, "FIRE!", (0, 0, 255), 2000)
    process_and_draw(smoke_mask, "SMOKE", (150, 150, 150), 5000)

    cv2.imwrite("Final Project: Fire & Smoke Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
