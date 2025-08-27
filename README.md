# CCTV Intrusion Detector

## Description

A real-time **CCTV Intrusion Detection System** that detects unauthorized people entering a restricted area using a webcam or CCTV feed.

---

## Features

* Real-time object detection using **YOLOv8**
* Detects people (intruders) entering a restricted area
* Visual alerts on the screen
* Option to add sound/email alerts

---

## Requirements

* Python 3.x
* Libraries:

  * OpenCV (`opencv-python`)
  * YOLOv8 / Ultralytics (`ultralytics`)
  * Streamlit (optional, for web interface)
  * playsound (optional, for audio alert)

Install using:

```bash
pip install opencv-python ultralytics streamlit playsound
```

---

## How to Run

1. Clone the repository.
2. Ensure all required libraries are installed.
3. Run the main script:

```bash
python main.py
```

4. A window will open showing the live camera feed.
5. If a person enters the restricted area, it will show an alert.

---

## Optional Enhancements

* Send email or SMS notifications using SMTP/Twilio.
* Record video when intrusion is detected.
* Store logs of intrusions with timestamps.
* Customize restricted area coordinates.

---

## License

This project is open-source and free to use for personal and educational purposes.
