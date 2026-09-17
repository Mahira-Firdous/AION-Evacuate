# 🔥 AI Fire Evacuation System — AION Evacuate

An AI-powered fire detection and smart evacuation system designed to detect fire in real time and guide people toward safer evacuation routes.

## 🚀 Overview

**AION Evacuate** combines computer vision, AI assistance, and a building floor plan to provide intelligent emergency guidance.

The system detects fire from different camera inputs, identifies the affected area, maps it onto a building blueprint, and generates an evacuation route while avoiding the detected danger zone.

---

## 🎯 Problem Statement

During a fire emergency, people may panic and struggle to identify the safest exit.

Traditional alarm systems mainly provide warnings but do not offer **location-based evacuation guidance**.

---

## 💡 Our Solution

AION Evacuate provides an integrated emergency response system that:

* 🔥 Detects fire using computer vision
* 📍 Identifies and maps the fire location
* 🗺️ Generates a safer evacuation route
* 🔊 Provides real-time voice alerts
* 🤖 Offers AI-based emergency assistance

---

## ✨ Key Features

### 🔥 Fire Detection

The system supports multiple input sources for fire detection:

* Live webcam
* Uploaded images
* Video files
* YouTube videos
* Screen capture

### 🗺️ Smart Evacuation Map

The system uses a building blueprint to visualize the emergency situation.

It displays:

* 🔴 Fire location
* 🔵 User location
* 🟢 Recommended evacuation path
* 🟡 Available exits

The evacuation route is generated while considering hazardous areas.

### 🎥 Camera & Detection System

* Real-time webcam detection
* Image and video-based detection
* CCTV-like simulation using uploaded media
* Detection overlays for identified fire areas

### 🔊 Voice Alert System

Provides immediate voice-based warnings during an emergency.

Example:

> "Fire detected. Please follow the evacuation route immediately."

### 🤖 AI Emergency Assistant

An AI assistant allows users to interact through text or voice and receive emergency-related guidance and instructions.

---

## 🧠 Tech Stack

* **Python** — Core logic and detection module
* **OpenCV** — Computer vision and video processing
* **YOLO** — Fire detection
* **NumPy** — Numerical processing
* **Gemini API** — AI emergency assistant
* **gTTS** — Voice alerts
* **Base44** — Application interface and integration

---

## ⚙️ How It Works

```text
Camera / Image / Video
          ↓
   Fire Detection
          ↓
   Fire Location
          ↓
   Building Blueprint
          ↓
 Safe Route Generation
          ↓
 Voice Alert + AI Guidance
```

### Workflow

1. Upload or load the building blueprint.
2. Select a detection source such as webcam, image, or video.
3. The computer vision module detects fire.
4. The detected location is mapped onto the building blueprint.
5. A safer evacuation route is generated.
6. Voice alerts notify the user.
7. The AI assistant provides additional emergency guidance.

---

## 🔥 Fire Detection Module

The fire detection module is implemented using **OpenCV and YOLO** and has been demonstrated separately in the project demo.

Due to current platform limitations, the detection module is presented as a separate component, but the architecture is designed to allow it to be integrated seamlessly with the main evacuation system.

---

## 🌟 Project Goal

AION Evacuate aims to go beyond simply **detecting a fire** by combining detection, location awareness, route planning, and AI assistance into a single emergency-response system.
