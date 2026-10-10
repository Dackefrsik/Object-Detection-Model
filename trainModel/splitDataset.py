import os
import shutil
import random

# Paths for images and labels in dataset
images = os.listdir("../Rock paper scissor dataset.v2/train/images")
labels = os.listdir("../Rock paper scissor dataset.v2/train/labels")

classes = {0: [], 1: [], 2: []}

for image in images:
    labelName = os.path.splitext(image)[0] + ".txt"
    labelPath = os.path.join(
        "../Rock paper scissor dataset.v2/train/labels",
        labelName
    )

    with open(labelPath, "r") as file:
        classID = int(file.readline().split()[0])

    classes[classID].append(image)


# Finding images indexes to split data in 70%, 15% and 15%
startVal = int(len(images) * 0.7)
endVal = int(len(images) * 0.85)


# Function to split dataset into test, train and validation 
def splitData(startVal, endVal):

    # Testimages
    testPathImages = "../splittedDataset/test/images"
    testPathLabels = "../splittedDataset/test/labels"

    # Clear paths befor adding the new immages 
    shutil.rmtree(testPathImages)
    shutil.rmtree(testPathLabels)
    
    os.makedirs(testPathImages, exist_ok=True)
    os.makedirs(testPathLabels, exist_ok=True)

    # Trainimages
    trainPathImages = "../splittedDataset/train/images"
    trainPathLabels = "../splittedDataset/train/labels"

    shutil.rmtree(trainPathImages)
    shutil.rmtree(trainPathLabels)
    
    os.makedirs(trainPathImages, exist_ok=True)
    os.makedirs(trainPathLabels, exist_ok=True)

    # Validateimages
    validPathImages = "../splittedDataset/valid/images"
    validPathLabels = "../splittedDataset/valid/labels"

    shutil.rmtree(validPathImages)
    shutil.rmtree(validPathLabels)
    
    os.makedirs(validPathImages, exist_ok=True)
    os.makedirs(validPathLabels, exist_ok=True)

    trainImages = []
    testImages = []
    validImages = []

    for classID, classImages in classes.items():

        random.shuffle(classImages)

        startVal = int(len(classImages) * 0.7)
        endVal = int(len(classImages) * 0.85)

        trainImages.extend(classImages[:startVal])
        testImages.extend(classImages[startVal:endVal])
        validImages.extend(classImages[endVal:])

    print(f"Train: {len(trainImages)}")
    print(f"Test: {len(testImages)}")
    print(f"Validation: {len(validImages)}")

    # Training data
    for i in trainImages:
        
        image = os.path.join(
        "../Rock paper scissor dataset.v2/train/images",
        i
        )

        labelName = os.path.splitext(i)[0] + ".txt"
        
        label = os.path.join(
        "../Rock paper scissor dataset.v2/train/labels",
        labelName
        )

        shutil.copy(image, trainPathImages)
        shutil.copy(label, trainPathLabels)

    # Test data
    for i in testImages:
        image = os.path.join(
        "../Rock paper scissor dataset.v2/train/images",
        i
        )

        labelName = os.path.splitext(i)[0] + ".txt"

        
        label = os.path.join(
        "../Rock paper scissor dataset.v2/train/labels",
        labelName
        )

        shutil.copy(image, testPathImages)
        shutil.copy(label, testPathLabels)

    # Valaidation data
    for i in validImages:
        image = os.path.join(
        "../Rock paper scissor dataset.v2/train/images",
        i
        )

        labelName = os.path.splitext(i)[0] + ".txt"
        
        label = os.path.join(
        "../Rock paper scissor dataset.v2/train/labels",
        labelName
        )

        shutil.copy(image, validPathImages)
        shutil.copy(label, validPathLabels)

if __name__ == "__main__":
    print("Start splitting...")

    splitData(startVal, endVal)

    print("Splitting done...")
