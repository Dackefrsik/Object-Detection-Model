# Source https://docs.ultralytics.com/models/yolov8?utm_source=chatgpt.com
from ultralytics import YOLO
import os

# Absolut path to the yaml-file in the dataset
path = os.path.abspath("../Rock paper scissor dataset.v3/data.yaml")

# The predefined CNN-model that will be trained on the custom dataset
model = YOLO("yolov8n.pt")

# Te acctiuall training of the model
result = model.train(
    data=path, 
    epochs=50, 
    imgsz=640, 
    project=os.path.abspath("trainingResult"), # Need a correct path in the project (repository) to store the resault
    name="rockPaperScissors"
    )
