import os
import shutil
import random

# Paths for images and labels in dataset
images = os.listdir("../Rock paper scissor dataset.v3/train/images")
labels = os.listdir("../Rock paper scissor dataset.v3/train/labels")

# Index for each class
classes = {0: [], 1: [], 2: []}

# Adding each images to its respective 
# This process makes shure that the images are devided evenly accross each set of images 
# and not based on when they where added to the dataset
for image in images:

    # The name of the image lable
    labelName = os.path.splitext(image)[0] + ".txt"

    # Pathway to the image
    labelPath = os.path.join(
        "../Rock paper scissor dataset.v3/train/labels",
        labelName
    )

    # classID reads the first value of the lina in the labelfile
    with open(labelPath, "r") as file:
        classID = int(file.readline().split()[0])

    # Apends the image based on the id of its calss
    classes[classID].append(image)

# Function to split dataset into test, train and validation 
def splitData(startVal, endVal):

    # Testimages
    testPathImages = "../splittedDataset/test/images"
    testPathLabels = "../splittedDataset/test/labels"

    # Clear paths befor adding the new immages 
    shutil.rmtree(testPathImages)
    shutil.rmtree(testPathLabels)

    # Creates the teo paths if it dosen't exists
    os.makedirs(testPathImages, exist_ok=True)
    os.makedirs(testPathLabels, exist_ok=True)

    # Repeat the same process for the path for the train- and validationsets folders
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

    # Arrays for each set of images
    trainImages = []
    testImages = []
    validImages = []

    # Checking each class of images and append al of them in 70/15/15 split to repektive set of images
    for classImages in classes.items():

        # Shuffle the images for each class so it dosen't choos images in a specific order base on 
        # when they been added to the dataset
        random.shuffle(classImages)

        # Calulate the start and end values for the 70% 15% and 15% split
        startVal = int(len(classImages) * 0.7)
        endVal = int(len(classImages) * 0.85)

        # Adding the data to each dataset, .extend adds multiple data. 
        # It ads every image within the value range to each dataset
        trainImages.extend(classImages[:startVal])
        testImages.extend(classImages[startVal:endVal])
        validImages.extend(classImages[endVal:])

    # Training data
    for i in trainImages:

        # Image path
        image = os.path.join(
        "../Rock paper scissor dataset.v3/train/images",
        i
        )

        # Retrieving the label for each image and  
        labelName = os.path.splitext(i)[0] + ".txt"

        # Label path 
        label = os.path.join(
        "../Rock paper scissor dataset.v3/train/labels",
        labelName
        )

        # Copies and label in to the correct folder
        shutil.copy(image, trainPathImages)
        shutil.copy(label, trainPathLabels)

    # Repeating the process for the test and validation images
    # Test data
    for i in testImages:
        image = os.path.join(
        "../Rock paper scissor dataset.v3/train/images",
        i
        )

        labelName = os.path.splitext(i)[0] + ".txt"

        
        label = os.path.join(
        "../Rock paper scissor dataset.v3/train/labels",
        labelName
        )

        shutil.copy(image, testPathImages)
        shutil.copy(label, testPathLabels)

    # Valaidation data
    for i in validImages:
        image = os.path.join(
        "../Rock paper scissor dataset.v3/train/images",
        i
        )

        labelName = os.path.splitext(i)[0] + ".txt"
        
        label = os.path.join(
        "../Rock paper scissor dataset.v3/train/labels",
        labelName
        )

        shutil.copy(image, validPathImages)
        shutil.copy(label, validPathLabels)

# Main fucntion that initiate the splitting of the data
if __name__ == "__main__":
    print("Start splitting...")

    splitData()

    print("Splitting done...")
