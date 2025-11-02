# YOLO Fire Detector

A real-time fire detection system using YOLOv8 object detection model with webcam input.

## Project Overview

This project implements a fire detection system that uses computer vision to identify fire in real-time video streams from a webcam. It leverages the Ultralytics YOLOv8 framework for object detection.

## Features

- Real-time fire detection using webcam
- YOLOv8 model integration
- Live video processing with confidence thresholding
- Visual results display in window

## Files Structure

```
Fire_project/
├── fair.py                 # Main detection script
├── best.pt                 # Trained YOLO model weights
├── yolov8s.pt             # YOLOv8 small pre-trained model
├── yolovenv/              # Python virtual environment
├── requirements.txt       # Python dependencies and dataset source
├── .vscode/
│   └── settings.json      # VS Code configuration
└── README.md              # This file
```

## Dataset Source

The fire detection model was trained on a dataset available at:
https://app.roboflow.com/said-qn15w/continuous_fire-2jwjw/models

## Requirements

- Python 3.11+
- Webcam
- Dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YusupovSaid/YOLO-Fire-Detector.git
cd YOLO-Fire-Detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or activate the included virtual environment:
```bash
source yolovenv/bin/activate  # On macOS/Linux
# or
yolovenv\Scripts\activate     # On Windows
```

## Usage

Run the fire detection:
```bash
python fair.py
```

The script will:
- Load the trained YOLO model (`best.pt`)
- Start webcam capture
- Process frames in real-time
- Display detection results with bounding boxes
- Show confidence scores above 0.6 threshold

## Model Details

- **Model**: YOLOv8 (Ultralytics)
- **Input**: Webcam video stream (640x640 resolution)
- **Confidence Threshold**: 0.6
- **Target**: Fire detection

## Dependencies

The project includes a complete virtual environment (`yolovenv/`) with all required packages:
- ultralytics (YOLOv8)
- opencv-python
- torch
- numpy
- And other dependencies listed in requirements.txt

## Configuration

- **Model Path**: Currently hardcoded to `best.pt`
- **Webcam Source**: Default camera (source=0)
- **Resolution**: 640x640 pixels
- **Confidence**: 0.6 minimum threshold


## License

This project is provided for educational and security research purposes.

## Contributing

For security research and vulnerability analysis purposes.
