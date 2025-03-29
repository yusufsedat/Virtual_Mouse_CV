import cv2
import mediapipe as mp
import pyautogui
import threading

def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def scroll_page(amount):
    pyautogui.scroll(amount)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cv2.setUseOptimized(True)

hand_detector = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y, index_x = 0, 0
prev_x, prev_y = 0, 0
smoothing_factor = 0.2
thumb_y, middle_y = 0, 0
scroll_lock = False


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=2)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                    smooth_x = prev_x + (index_x - prev_x) * smoothing_factor
                    smooth_y = prev_y + (index_y - prev_y) * smoothing_factor
                    prev_x, prev_y = smooth_x, smooth_y

                    threading.Thread(target=move_mouse, args=(smooth_x, smooth_y)).start()


                if id == 12:

                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0), thickness=2)
                    middle_y = screen_height / frame_height * y

                    scroll_speed = int(index_y - middle_y)
                    if abs(scroll_speed) > 50:
                        threading.Thread(target=scroll_page, args=(scroll_speed,)).start()


                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0), thickness=2)
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    if abs(index_y - thumb_y) < 50:
                        pyautogui.click()
                        pyautogui.sleep(0.1)
                        print("Left Click")

                if id == 16:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 255, 0), thickness=2)
                    ring_y = screen_height / frame_height * y


                    if(abs(thumb_y-ring_y)) <50:
                        pyautogui.rightClick()
                        pyautogui.sleep(0.1)
                        print("Right Click")


    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()