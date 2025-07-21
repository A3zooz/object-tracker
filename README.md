# Object Tracker

Real-time object tracking using OpenCV's CSRT tracker. Select an object from your webcam and track it live with visual feedback.

## Features

- Real-time object tracking using CSRT algorithm
- Interactive ROI selection with mouse
- Live webcam processing
- Visual bounding box overlay
- Tracking failure detection

## Installation

```bash
# Clone the repository
git clone https://github.com/A3zooz/object-tracker.git
cd object-tracker

# Install dependencies
pip install -r requirements.txt

# Run the tracker
python tracker.py
```

## Usage

1. **Start**: Run the script - camera initializes in 1 second
2. **Select**: Click and drag to draw a bounding box around your target object
3. **Confirm**: Press `ENTER` or `SPACE` to start tracking
4. **Track**: Watch the blue bounding box follow your object
5. **Exit**: Press `q` to quit

## Implementation Details

- Uses OpenCV's `VideoCapture` to access the webcam.
- Initializes the CSRT tracker with the selected ROI.
- Uses OpenCV's `TrackerCSRT_create` for accurate tracking.
- ROI selection uses `cv2.selectROI()`.
- Displays real-time bounding box on live webcam feed.

## Controls

- **ENTER/SPACE**: Confirm selection
- **C**: Cancel selection
- **q**: Quit application

