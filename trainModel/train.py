# Source https://docs.ultralytics.com/models/yolov8
from ultralytics import YOLO
import os


def train():
    # Absolut path to the yaml-file in the dataset
    path = os.path.abspath("../Datasets/Rock Paper Scissors SXSW.v14i.yolov8/data.yaml")

    # The predefined CNN-model that will be trained on the custom dataset
    model = YOLO("yolov8n.pt")

    # Te acctiuall training of the model
    result = model.train(
        data = path, 
        epochs = 50, 
        imgsz = 640,
        patience = 15,
        plots = True, 
        project = os.path.abspath("trainingResult"), # Need a correct path in the project (repository) to store the resault
        name = "rockPaperScissors",
        device = 0,
        batch = 8
        )

if __name__ == "__main__":
    train()
