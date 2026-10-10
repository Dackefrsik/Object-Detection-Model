from tkinter import *
import cv2
from PIL import Image, ImageTk 
import os
from datetime import datetime
from ultralytics import YOLO

# Source https://www.geeksforgeeks.org/python/how-to-show-webcam-in-tkinter-window-python/
camera = cv2.VideoCapture(0)
current_frame = None
camera_running = True
camera_button_name = "Open camera"

def interface():
    width, height = 800, 600

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    app = Tk()
    app.focus_force() # Gives the application keyboard focus

    app.bind('<Escape>', lambda e: app.quit())
    app.bind("<a>", lambda e: save_image())
    app.title("Oject detection model")

    label_widget = Label(app)
    label_widget.grid(row=1, column=0)

    # Source for frame https://www.geeksforgeeks.org/python/python-tkinter-frame-widget/
    frame= Frame(app, bg=app.cget("bg"), width=200, height=10, bd=3, relief=RIDGE, border=0)
    frame.grid(column=0, row=0, sticky="w")

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

    button1.grid(row=0, column=0, sticky="w", padx=(0,10))
    button2.grid(row=0, column=1, sticky="w", padx=(0,10))
    button3.grid(row=0, column=2, sticky="w")

    app.mainloop()

def open_camera(label_widget, button1):
    ret, frame = camera.read()

    if not ret:
        print("Could not read from camera")

    global current_frame, camera_running

    camera_running = True

    button1.config(text="Close camera", command=lambda:close_camera(label_widget, button1))

    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(current_frame)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)

    label_widget.after(10, update_camera, label_widget, button1)


def close_application(app):
    camera.release()
    app.destroy()
    print("Closing model...")

def save_image():
    print("Try to save image...")
    if current_frame is not None:
        date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f") # Source https://www.geeksforgeeks.org/python/python-strftime-function/
        os.makedirs("images", exist_ok=True)
        cv2.imwrite("images/frame" + date_time + ".jpg", current_frame)
        print("Images saved")
    else:
        print("No active frame ton save image from")

model = YOLO(
        "../trainModel/trainingResult/rockPaperScissors-6/weights/best.pt"
        )

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
        conf=0.25,
        verbose=False
    )

    annotated_frame = results[0].plot()

    captured_image = Image.fromarray(
        cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    )
    """ captured_image = Image.fromarray(current_frame) """
    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)

    label_widget.after(
        10,
        update_camera,
        label_widget,
        button1
    )

def close_camera(label_widget, button1):

    global camera_running, current_frame

    camera_running = False
    current_frame = None
    label_widget.photo_image = None
    label_widget.configure(image="")
    button1.config(text="Open camera", command=lambda:open_camera(label_widget, button1))

if __name__ == "__main__":
    print("Starting model...")
    interface()