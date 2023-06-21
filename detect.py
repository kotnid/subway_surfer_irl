from ultralytics import YOLO

class detect:
    def __init__(self):
        self.model = YOLO("yolov8n-pose.pt")
        self.model.to("cuda")

    def get(self,frame):
        results = self.model(source=frame, conf=0.7, save=False, verbose=False, device="cuda:0", max_det=200, half=True)
        return results