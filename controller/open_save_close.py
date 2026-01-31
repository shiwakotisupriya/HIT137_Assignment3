from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function for opening the image from the local file
def open_image(app):
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.bmp")]
    )
    if not path:
        return

    try:
        app.model.image = Image.open(path)
        app.model.original_image = app.model.image.copy()
        app.model.image_path = path
        app.model.undo_stack.clear()
        app.model.redo_stack.clear()
        show_image(app)
        update_status(app)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to save the image after changes
def save_image(app):
    if app.model.image is None:
        messagebox.showwarning("Warning", "No image to save")
        return
    app.model.image.save(app.model.image_path)
    messagebox.showinfo("Saved", "Image saved successfully")

# function for saving the image to new location after making changes
def save_as_image(app):
    if app.model.image is None:
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("BMP", "*.bmp")]
    )
    if path:
        app.model.image.save(path)
        messagebox.showinfo("Saved", "Image saved successfully")


# function for displaying a image
def show_image(app):
    if app.model.image is None:
        return

   
    app.canvas.delete("all")

 
    canvas_width = app.canvas.winfo_width()
    canvas_height = app.canvas.winfo_height()


    img_w, img_h = app.model.image.size
    ratio = min(canvas_width / img_w, canvas_height / img_h)
    new_w = int(img_w * ratio)
    new_h = int(img_h * ratio)

  
    resized = app.model.image.resize((new_w, new_h), Image.Resampling.LANCZOS)
    app.tk_image = ImageTk.PhotoImage(resized)

  
    app.canvas.create_image(canvas_width // 2, canvas_height // 2, image=app.tk_image)
 

# functiion for updating the image status such as path
def update_status(app):
    name = os.path.basename(app.model.image_path)
    w, h = app.model.image.size
    app.status.config(text=f"{name} | {w} x {h}")