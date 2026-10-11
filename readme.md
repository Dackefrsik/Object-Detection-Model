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

## Use

### Start the user interface

Start the applications graphical user interface with:

```bash
python interface/interface.py
```

### Split the dataset

Run the following commando to devide the dataset into training-, validation-, and testdata:

```bash
python trainModel/splitDataset.py
```

The dataset is devided as following:

| Dataset | Share |
|---------|-------|
| Training | 70 % |
| Validation | 15 % |
| Test | 15 % |

## Projectstructure

```text
Object-Detection-Model/
├── interface/
│   └── interface.py
├── trainModel/
│   └── splitDataset.py
├── splittedDataset/
│   ├── train/
│   ├── validate/
│   └── test/
└── readme.md
```
