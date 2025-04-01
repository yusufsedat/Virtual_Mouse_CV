# Virtual Mouse Using Hand Gestures with OpenCV, Mediapipe, and PyAutoGUI

This project implements a virtual mouse using hand gestures through a webcam. It utilizes OpenCV for video capturing, Mediapipe for hand landmark detection, and PyAutoGUI for controlling the mouse. The virtual mouse supports:

- Moving the cursor
- Left-click and right-click
- Scrolling
### Installation
To run this project, you need to install the following libraries:
```
pip install opencv-python mediapipe pyautogui
```

### Features
- **Move Cursor**: Move your index finger to control the mouse pointer.
- **Left Click**: Touch your thumb and index finger together.
- **Right Click**: Touch your thumb and ring finger together.
- **Scrolling**: Move your middle finger up or down to scroll.

### How It Works  

1. **Hand Detection**: Uses Mediapipe's hand tracking to detect hand landmarks.
2. **Gesture Recognition**:
     - **Moving Cursor**: Uses the position of the index finger to move the mouse smoothly.
     - **Left Click**: Detects when the distance between the thumb and index finger is below a threshold.
     - **Right Click**: Detects when the thumb and ring finger come close.
     - **Scrolling**: Uses the relative position between the index and middle fingers to calculate the scroll amount.
       
3. **Mouse Control**: Uses PyAutoGUI to perform mouse actions such as clicking, dragging, and scrolling.

### Known Issues
1. **Sensitivity**: Adjust `distance` and `scroll_speed` thresholds to fine-tune your system.
2. **Performance**: High CPU usage due to continuous video processing.

## Future Improvements
1. **Gesture Customization:** Allow users to define custom gestures.
2. **Multi-hand Support:** Detect gestures with both hands.
3. **Gesture Calibration:** Dynamically adjust sensitivity based on hand size and distance from the camera.
