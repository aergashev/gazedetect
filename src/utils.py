def calculate_gaze_direction(frame, face):
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    center_x, center_y = x + w // 2, y + h // 2
    is_looking_away = center_x < 0.3 * frame.shape[1] or center_x > 0.7 * frame.shape[1] or center_y < 0.3 * frame.shape[0] or center_y > 0.7 * frame.shape[0]
    return is_looking_away
