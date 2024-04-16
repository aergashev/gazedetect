import cv2

def track_face(frame, face, face_tracker):
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    center_x, center_y = x + w // 2, y + h // 2

    if face_tracker is None:
        face_tracker = cv2.TrackerKCF_create()
        face_tracker.init(frame, (x, y, w, h))
    else:
        success, new_box = face_tracker.update(frame)
        if success:
            new_x, new_y, new_w, new_h = map(int, new_box)
            face.left(new_x)
            face.top(new_y)
            face.right(new_x + new_w)
            face.bottom(new_y + new_h)
        else:
            face_tracker = None

    return face_tracker
