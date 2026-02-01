"""
Class ImageModel manages undo and redo along with storing the image data and running all open CV process
"""
import cv2
import numpy as np
import os


class ImageModel:
    def __init__(self):
        self._image = None
        self._original_image = None
        self._image_path = None
        self._undo_stack = []
        self._redo_stack = []

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, img):
        self._image = img

    @property
    def original_image(self):
        return self._original_image

    @original_image.setter
    def original_image(self, img):
        self._original_image = img

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, path):
        self._image_path = path

    def save_undo(self):
        if self._image is not None:
            self._undo_stack.append(self._image.copy())
            self._redo_stack.clear()

    def undo(self):
        if self._undo_stack:
            self._redo_stack.append(self._image.copy())
            self._image = self._undo_stack.pop()
            return True
        return False

    def redo(self):
        if self._redo_stack:
            self._undo_stack.append(self._image.copy())
            self._image = self._redo_stack.pop()
            return True
        return False

# clearing undo and redo
    def history_reset(self):
        self._undo_stack.clear()
        self._redo_stack.clear()

    # image loading
    def load_img(self, path):
        img = cv2.imread(path)
        if img is None:
            return False
        self._image_path = path
        self._original_image = img.copy()
        self._image = img.copy()
        self.history_reset()
        return True

    # getting the image info such as height, width, image type
    def get_img_info(self):
        if self._image is None:
            return {"filename": "None", "width": 0, "height": 0, "channels": 0}
        filename = os.path.basename(self._image_path) if self._image_path else "None"
        if len(self._image.shape) == 3:
            h, w, c = self._image.shape
        else:
            h, w = self._image.shape
            c = 1
        return {"filename": filename, "width": w, "height": h, "channels": c}

    # convert to grey
    def convert_gray(self):
        if self._image is None:
            return False
        self.save_undo()
        if len(self._image.shape) == 3:
            self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        return True

# applying blur effect to the image
    def blur_effect_application(self, intensity):
        if self._image is None:
            return False
        self.save_undo()
        kernel = max(1, int(intensity))
        if kernel % 2 == 0:
            kernel += 1
        self._image = cv2.GaussianBlur(self._image, (kernel, kernel), 0)
        return True

# function for detecting the edge of the image
    def edge_dector(self):
        if self._image is None:
            return False
        self.save_undo()
        gray = self._image
        if len(self._image.shape) == 3:
            gray = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        self._image = cv2.Canny(gray, 100, 200)
        return True

# function for increasing or decreasing the brightness
    def adjust_brightness(self, value):
        if self._image is None:
            return False
        self.save_undo()
        alpha = value / 100.0
        self._image = cv2.convertScaleAbs(self._image, alpha=alpha, beta=0)
        return True

# function for adjusting the contrast
    def adjust_contrast(self, value):
        if self._image is None:
            return False
        self.save_undo()
        alpha = value / 100.0
        self._image = cv2.convertScaleAbs(self._image, alpha=alpha, beta=0)
        return True

# function for rotating image into different angles
    def rotate(self, degrees):
        if self._image is None:
            return False
        self.save_undo()
        mapping = {
            90:  cv2.ROTATE_90_CLOCKWISE,
            180: cv2.ROTATE_180,
            270: cv2.ROTATE_90_COUNTERCLOCKWISE
        }
        if degrees in mapping:
            self._image = cv2.rotate(self._image, mapping[degrees])
        return True

# function for fliping the image
    def flip(self, direction):
        if self._image is None:
            return False
        self.save_undo()
        code = 1 if direction == "horizontal" else 0
        self._image = cv2.flip(self._image, code)
        return True

# function for resizing the image
    def resize(self, width, height):
        if self._image is None or width <= 0 or height <= 0:
            return False
        self.save_undo()
        self._image = cv2.resize(self._image, (int(width), int(height)))
        return True

# function for reversing all the changes
    def reverse_changes(self):
        if self._original_image is None:
            return False
        self.save_undo()
        self._image = self._original_image.copy()
        return True