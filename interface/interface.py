from tkinter import *
import cv2
from PIL import Image, ImageTk 
import os
from datetime import datetime
from ultralytics import YOLO

from config import WIDTH, HEIGHT

# Source https://www.geeksforgeeks.org/python/how-to-show-webcam-in-tkinter-window-python/
camera = cv2.VideoCapture(0)
current_frame = None
camera_running = True
camera_button_name = "Open camera"

# The best version of the trained model
model = YOLO(
        "../trainModel/trainingResult/rockPaperScissors/weights/best.pt"
        )

# Function that runs the interface
def interface():
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    # Setting up a tak inter applikation
    # Source https://docs.python.org/3/library/tkinter.html?
    app = Tk()
    app.focus_force() # Gives the application keyboard focus
    app.title("Oject detection model")

    # Keyboard inputs
    # Lambda form creating an anonymus function
    app.bind('<Escape>', lambda e: app.quit())
    app.bind("<l>", lambda e: save_image())

    # Creating a label_widget for the applications mainwindow 
    label_widget = Label(app)

    # Positioning the label in row 1, column 0 using TKinter's grid geometry manager
    label_widget.grid(row=1, column=0)

    # Source for frame https://www.geeksforgeeks.org/python/python-tkinter-frame-widget/
    frame= Frame(app, bg=app.cget("bg"), width=200, height=10, bd=3, relief=RIDGE, border=0)
    frame.grid(column=0, row=0, sticky="w")

    # Creating some menu buttons
    button1 = Button(
        frame, 
        text="Open camera", 
        # Lambda makes sure the function only executes when the button i clicked
        command=lambda: open_camera(label_widget, button1),
        bd=0
    )
    button2 = Button(
        frame,
        text='Save image',
        command=lambda:save_image(),
        bd=0
    )
    button3 = Button(
        frame,
        text='Close application',
        command=lambda:close_application(app),
        bd=0
    )

    # Adding each button to UI 
    button1.grid(row=0, column=0, sticky="w", padx=(0,10))
    button2.grid(row=0, column=1, sticky="w", padx=(0,10))
    button3.grid(row=0, column=2, sticky="w")

    # Running the application
    app.mainloop()

# Function for opening the camera
# Source: https://docs.opencv.org/4.12.0/dd/d43/tutorial_py_video_display.html
def open_camera(label_widget, button1):
    ret, frame = camera.read()

    # Checking if the camera could read the image frame
    if not ret:
        print("Could not read from camera")
        return

    # Allowing modifying global variables
    global current_frame, camera_running

    # Indicates that the camera is runnig
    camera_running = True

    # Updating the UI and shows trhe camera
    button1.config(text="Close camera", command=lambda:close_camera(label_widget, button1))

    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(current_frame)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)

    # Updating the frame each time 10 miliseconds have passed by
    label_widget.after(10, update_camera, label_widget, button1)

# Function that runs when the user closes the application through the menu buttons
def close_application(app):
    camera.release()
    app.destroy()
    print("Closing model...")

# Function that is running when the user press the "Save image" buton
def save_image():
    print("Try to save image...")

    # Check if there is an active frame to same images from
    if current_frame is not None:

        # Set filname that let users take multipel images in arrow without ovcerwriting them
        date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f") # Source https://www.geeksforgeeks.org/python/python-strftime-function/

        # Check if the folder images exists 
        os.makedirs("images", exist_ok=True)

        # The image needs to be in BGR format before it is saved
        frameToSave = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
        cv2.imwrite("images/frame" + date_time + ".jpg", frameToSave)
        print("Images saved")
    else:
        print("No active frame to save an image from")

# Uppadaterar the camera frame if it is running
def update_camera(label_widget, button1):
    global current_frame

    if not camera_running:
        return

    ret, frame = camera.read()

    if not ret:
        print("Could not read from camera")
        return

    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Source https://roboflow.com/blog/how-to-train-yolov8-on-a-custom-dataset
    results = model.predict(
        source= frame,
        # A confidence score of 0.75 makes sure that modele more or less can't detect my face or other 
        # object rather than the on that have been anotated to be classified after the model have 
        # been trained
        conf = 0.5,
        verbose=False
    )

    # Plottinh the lable around the identified object 
    annotated_frame = results[0].plot()
    captured_image = Image.fromarray(
        cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    )

    # Upadte the presented imaged 
    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)

    label_widget.after(
        10,
        update_camera,
        label_widget,
        button1
    )

# Funcntion for closing the camera 
def close_camera(label_widget, button1):

    global camera_running, current_frame

    camera_running = False
    current_frame = None
    label_widget.photo_image = None
    label_widget.configure(image="")
    button1.config(text="Open camera", command=lambda:open_camera(label_widget, button1))


# Main function that creates the interface
if __name__ == "__main__":
    print("Starting model...")
    interface()