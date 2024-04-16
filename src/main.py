import cv2
from face_detection import detect_faces
from face_tracking import track_face
from gaze_detection import detect_gaze

video_path = 'data/input_video.mp4'
output_file = 'data/output_report.txt'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

face_tracker = None
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_faces(frame)
    if len(faces) > 0:
        face = faces[0]  # Assume there is only one face
        face_tracker = track_face(frame, face, face_tracker)
        detect_gaze(frame, [face], {face: face_tracker}, output_file, frame_number)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1


cap.release()
cv2.destroyAllWindows()
