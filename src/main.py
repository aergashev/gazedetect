import cv2
from face_detection import detect_faces
from face_tracking import track_faces
from gaze_detection import detect_gaze

video_path = 'data/input_video.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

face_trackers = {}
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_faces(frame)
    track_faces(frame, faces, face_trackers)
    detect_gaze(frame, faces, face_trackers)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1

cap.release()
cv2.destroyAllWindows()