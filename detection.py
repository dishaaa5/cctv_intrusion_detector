import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")

source = 0
cap = cv2.VideoCapture(source)

while cap.isOpened():
    ret, frame= cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Live CCTV Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()