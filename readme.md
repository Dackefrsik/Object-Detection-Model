# Object Detection Model

A Python-project for object detection with a graphical user interface (GUI) and functionality for collect and manage datasets.

## Installation

Install the projecta mandatory Python-packages:

```bash
pip install opencv-python pillow ultralytics
```

### Dependencies

The project utilize the following external libraries:

| Library | Area of application|
|-----------|-------------------|
| `opencv-python` (cv2) | Camera and immage management |
| `pillow` (PIL) | Image handeling and display in the GUI |
| `ultralytics` | YOLO-objectdetection |

The following libraries is included in pythons standarslibrary and don't need to be installed seperately:

| Library | Area of application |
|-----------|-------------------|
| `tkinter` | Graphical user interface (GUI) |
| `os` | File and directory management |
| `shutil` | Copy and move files |
| `datetime` | Generation of timestamps |
| `random` | Random sorting of dataset |

> **Note:** Tkinter is included in most of the common installations of Python, but could need to bee installed on certain operativ systems

## Config 

config.py includes system specific variables in the form of WIDTH and HEIGHT 

## Train model 

The model is trained by using the following command:

```bash
python trainModel/train.py
```

## Use

### Start the user interface

Start the applications graphical user interface with:

```bash
python interface/interface.py
```

### Split the dataset

The dataset comes with the following split:

| Dataset | Share |
|---------|-------|
| Training | 88 % |
| Validation | 8 % |
| Test | 4 % |

## Projectstructure

```text
Object-Detection-Model/
├── Datasets/
│   └── Rock Paper Scissors SXSW.v14i.yolov8/
│       ├── test/
│       ├── train/
│       ├── valid/
│       ├── data.yaml
│       ├── README.dataset.txt/
│       └── README.robodflow.txt
├── interface/
│   ├── config.py/
│   └── interface.py
├── trainModel/
│   ├── trainingResult/
│   └── train.py
├── splittedDataset/
│   ├── train/
│   ├── valid/
│   └── test/
└── readme.md
```
