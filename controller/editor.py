"""
Editor class which handels all the editing logics such as filters, display, 
undo and redo,transformation and file input output
 __init__ is the controller for this class
"""
import cv2
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk


class Editor:
    # This function stores reference for the app so we can use model, canvas and status bar
    def __init__(self, app):
        self._app = app
        # Shortcut for class interaction
        self._model = app.model

    # This function converts  BGR array of the model
    def show_img(self):
        if self._model.image is None:
            return

        self._app.canvas.delete("all")
        canvas_w = self._app.canvas.winfo_width()
        canvas_h = self._app.canvas.winfo_height()

        img = self._model.image

        if len(img.shape) == 2:
            img_h, img_w = img.shape
        else:
            img_h, img_w = img.shape[:2]

        ratio = min(canvas_w / img_w, canvas_h / img_h)
        new_w, new_h = int(img_w * ratio), int(img_h * ratio)
        resized = cv2.resize(img, (new_w, new_h))

        if len(resized.shape) == 2:
            pil_img = Image.fromarray(resized, mode="L")
        else:
            rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb, mode="RGB")

        self._app.tk_image = ImageTk.PhotoImage(pil_img)
        self._app.canvas.create_image(canvas_w // 2, canvas_h // 2, image=self._app.tk_image)

# function for updating the status of image
    def status_update(self):
        info = self._model.get_img_info()
        self._app.status.config(
            text=f"  {info['filename']}  |  {info['width']} x {info['height']}  |  Channels: {info['channels']}"
        )

# function for opening and loading the image from the choosen path
    def open_img(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if not path:
            return
        try:
            success = self._model.load_img(path)
            if not success:
                messagebox.showerror("Error", "Could not load image.")
                return
            self.show_img()
            self.status_update()
        except Exception as e:
            messagebox.showerror("Error", str(e))

# function for saving an image
    def save_img(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return
        cv2.imwrite(self._model.image_path, self._model.image)
        messagebox.showinfo("Saved", "Image saved successfully.")
# function for saving new image by clicking save as
    def save_as_img(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("BMP", "*.bmp")]
        )
        if path:
            cv2.imwrite(path, self._model.image)
            self._model.image_path = path
            messagebox.showinfo("Saved", "Image saved successfully.")

    # function for undoing all the changes made
    def undo(self):
        if self._model.undo():
            self.show_img()
            self.status_update()
        else:
            messagebox.showinfo("Undo", "Nothing to undo.")
# function for redo all the changes
    def redo(self):
        if self._model.redo():
            self.show_img()
            self.status_update()
        else:
            messagebox.showinfo("Redo", "Nothing to redo.")

# function for increasing and decreasing the brightness of the image
    def adjust_brightness(self, value):
        if self._model.image is None:
            return
        self._model.adjust_brightness(float(value))
        self.show_img()
        self.status_update()
# function for adjusting the contrast of the image
    def adjust_contrast(self, value):
        if self._model.image is None:
            return
        self._model.adjust_contrast(float(value))
        self.show_img()
        self.status_update()
# function for applying grey scale to the image
    def apply_grayscale(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.convert_gray()
        self.show_img()
        self.status_update()

# function for applying blur effect to the image
    def blur_effect_application(self, intensity=5):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.blur_effect_application(intensity)
        self.show_img()
        self.status_update()

# function for  edge detection
    def apply_edge_dector(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.edge_dector()
        self.show_img()
        self.status_update()

# function for rotating the images 
    def img_rotate(self, degrees=90):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.rotate(degrees)
        self.show_img()
        self.status_update()
# function for applying horizontal flip
    def horizontal_flip_img(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.flip("horizontal")
        self.show_img()
        self.status_update()

# function for applying vertical flip
    def vertical_flip_img(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        self._model.flip("vertical")
        self.show_img()
        self.status_update()

# function for resizing the image
    def img_resize(self):
        if self._model.image is None:
            messagebox.showwarning("Warning", "Open an image first.")
            return
        info = self._model.get_img_info()
        new_w = simpledialog.askinteger(
            "Resize", "Enter new width (px):",
            initialvalue=info["width"], minvalue=1, maxvalue=10000
        )
        if new_w is None:
            return
        new_h = simpledialog.askinteger(
            "Resize", "Enter new height (px):",
            initialvalue=info["height"], minvalue=1, maxvalue=10000
        )
        if new_h is None:
            return
        self._model.resize(new_w, new_h)
        self.show_img()
        self.status_update()

# function for removing all the edits done and reseting the image
    def img_reset(self):
        if self._model.image is None:
            return
        self._model.reverse_changes()
        self.show_img()
        self.status_update()