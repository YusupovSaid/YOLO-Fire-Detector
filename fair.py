
# test_yolo.py
#from ultralytics import YOLO



#model = YOLO('best.pt')
#model.predict(source=0, imgsz=640, conf=0.6, show=True)


from ultralytics import YOLO

# Load your trained model
model = YOLO('/Users/mikeross/Desktop/python files/Fire_project/best.pt')  # Make sure best.pt is in the same folder OR use full path

# Run prediction on webcam (source=0)
model.predict(
    source=0,       # 0 = default webcam
    imgsz=640,      # image size
    conf=0.6,       # confidence threshold
    show=True       # show live results in a window
)
