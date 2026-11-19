# Face Tracker

A Simple Python Face-Tracking program using OpenCV.

## Requirements

- Python 3.8+
- A webcam
- [OpenCV](https://pypi.org/project/opencv-python/)

## How It Works

1. The webcam is opened with `cv2.VideoCapture(0)`.
2. Each frame is converted to grayscale, which is what the detector works on.
3. `detectMultiScale` from the Haar Cascade classifier finds faces in the frame.
4. A rectangle is drawn around each face, and the frame is shown in a window.

## Troubleshooting

- **Black screen or the camera won't open:** another app may be using the webcam, or your camera may not be device `0`. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`.
- **Too many false detections:** raise `minNeighbors`.
- **Faces not detected:** make sure your face is well lit and facing the camera. Haar Cascades work best on frontal faces.
