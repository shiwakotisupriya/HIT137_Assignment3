"""
Uses openCV for file operations such as save,display
"""
import cv2
import numpy as np
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# opeaning an image in an model using openCV
def open_img(app):
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not path:
        return

    try:
        success = app.model.load_img(path)   # cv2.imread is inside the model
        if not success:
            messagebox.showerror("Error", "Could not load image. Check the file.")
            return
        img_display(app)
        update_status(app)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# saves and image to new path
def save_img(app):
    if app.model.image is None:
        messagebox.showwarning("Warning", "No image to save.")
        return

    cv2.imwrite(app.model.image_path, app.model.image)
    messagebox.showinfo("Saved", "Image saved successfully.")

# Saves an image to a new location choosed by user
def save_as_img(app):
    if app.model.image is None:
        messagebox.showwarning("Warning", "No image to save.")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("BMP", "*.bmp")]
    )
    if path:
        cv2.imwrite(path, app.model.image)
        app.model.image_path = path          # update stored path
        messagebox.showinfo("Saved", "Image saved successfully.")



# displays image choosen by suer using canvas
def img_display(app):
    if app.model.image is None:
        return

    app.canvas.delete("all")

    canvas_w = app.canvas.winfo_width()
    canvas_h = app.canvas.winfo_height()

    img = app.model.image

    # Get height or width regardless
    if len(img.shape) == 2:
        img_h, img_w = img.shape
    else:
        img_h, img_w = img.shape[:2]

    # Scale the image to fit in canvas by keeping the aspected ratio
    ratio = min(canvas_w / img_w, canvas_h / img_h)
    new_w, new_h = int(img_w * ratio), int(img_h * ratio)
    resized = cv2.resize(img, (new_w, new_h))

    # converting the PTL image for making photo image
    if len(resized.shape) == 2:
        # Grayscale (single channel)
        pil_img = Image.fromarray(resized, mode="L")
    else:
        # Colour- open cv and tinkle
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb, mode="RGB")

    # keeping refrence to tinkle
    app.tk_image = ImageTk.PhotoImage(pil_img)
    app.canvas.create_image(canvas_w // 2, canvas_h // 2, image=app.tk_image)


# function for updating the changes made in an image
def update_status(app):
    info = app.model.get_img_info()
    app.status.config(
        text=f"  {info['filename']}  |  {info['width']} x {info['height']}  |  Channels: {info['channels']}"
    )