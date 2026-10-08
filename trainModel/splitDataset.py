import os
import shutil

# Paths for images and labels in dataset
images = os.listdir("../Rock paper scissor dataset.v1/train/images")
labels = os.listdir("../Rock paper scissor dataset.v1/train/labels")

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
    validPathImages = "../splittedDataset/validate/images"
    validPathLabels = "../splittedDataset/validate/labels"

    shutil.rmtree(validPathImages)
    shutil.rmtree(validPathLabels)
    
    os.makedirs(validPathImages, exist_ok=True)
    os.makedirs(validPathLabels, exist_ok=True)

    # Training data
    for i in range(startVal):
        
        image = os.path.join(
        "../Rock paper scissor dataset.v1/train/images",
        images[i]
        )
        
        label = os.path.join(
        "../Rock paper scissor dataset.v1/train/labels",
        labels[i]
        )

        shutil.copy(image, trainPathImages)
        shutil.copy(label, trainPathLabels)

    # Test data
    for i in range(startVal, endVal):
        image = os.path.join(
        "../Rock paper scissor dataset.v1/train/images",
        images[i]
        )
        
        label = os.path.join(
        "../Rock paper scissor dataset.v1/train/labels",
        labels[i]
        )

        shutil.copy(image, testPathImages)
        shutil.copy(label, testPathLabels)

    # Valaidation data
    for i in range(endVal, len(images)):
        image = os.path.join(
        "../Rock paper scissor dataset.v1/train/images",
        images[i]
        )
        
        label = os.path.join(
        "../Rock paper scissor dataset.v1/train/labels",
        labels[i]
        )

        shutil.copy(image, validPathImages)
        shutil.copy(label, validPathLabels)

if __name__ == "__main__":
    print("Start training...")

    splitData(startVal, endVal)
