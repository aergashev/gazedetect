import cv2
from utils import calculate_gaze_direction

def detect_gaze(frame, faces, face_trackers, output_file, frame_number):
    with open(output_file, 'a') as f:
        for face in faces:
            gaze_direction = calculate_gaze_direction(frame, face)
            f.write(f"Frame: {frame_number}, Face ID: {face.id()}, Looking Away: {gaze_direction}\n")
            print(f"Gaze direction: {gaze_direction}")
