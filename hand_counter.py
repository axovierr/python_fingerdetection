import mediapipe as mp
import cv2

class HandCounter:
    def __init__(self, max_num_hands=2, detection_confidence=0.75):
        self.hands_module = mp.solutions.hands
        self.hands = self.hands_module.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=0.75
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = self.hands.process(image_rgb)
        return result 

    def count_fingers(self, hand_landmarks, hand_label):
        fingers = []

        landmarks = hand_landmarks.landmark

        if hand_label == "Right":
            if landmarks[4].x > landmarks[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
        else: 
            if landmarks[4].x < landmarks[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

        tips = [8, 12, 16, 20]
        pip = [6, 10, 14, 18]
        for tip, p in zip(tips, pip):
            if landmarks[tip].y < landmarks[p].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return sum(fingers)