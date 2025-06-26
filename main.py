import cv2
from hand_counter import HandCounter

def main():
    cap = cv2.VideoCapture(0)
    detector = HandCounter(max_num_hands=2)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = detector.detect_hands(frame)

        total_fingers = 0

        if results.multi_hand_landmarks and results.multi_handedness:
            for i in range(len(results.multi_hand_landmarks)):
                hand_landmarks = results.multi_hand_landmarks[i]
                hand_label = results.multi_handedness[i].classification[0].label

                count = detector.count_fingers(hand_landmarks, hand_label)
                total_fingers += count

                if hand_label == "Right":
                    color = (49, 65, 255)  
                else:
                    color = (0, 255, 255)  

                detector.mp_draw.draw_landmarks(
                    frame, hand_landmarks, detector.hands_module.HAND_CONNECTIONS)

                h, w, _ = frame.shape
                cx = int(hand_landmarks.landmark[0].x * w)
                cy = int(hand_landmarks.landmark[0].y * h)

                cv2.putText(frame, f'{hand_label} Hand: {count}', (cx - 60, cy - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('Finger Detection (Double Hand)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
