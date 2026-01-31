from PIL import ImageEnhance, ImageFilter, ImageOps
from controller.open_save_close import show_image

# function for adjusting a brightness by using image enhancer
def adjust_brightness(app, value):
    if app.model.image is None:
        return
    app.model.undo_stack.append(app.model.image.copy())
    enhancer = ImageEnhance.Brightness(app.model.original_image)
    app.model.image = enhancer.enhance(float(value))
    show_image(app)

# function for undo the unwanted changes made
def undo(app):
    if app.model.undo_stack:
        app.model.redo_stack.append(app.model.image.copy())
        app.model.image = app.model.undo_stack.pop()
        show_image(app)

# function for redo
def redo(app):
    if app.model.redo_stack:
        app.model.undo_stack.append(app.model.image.copy())
        app.model.image = app.model.redo_stack.pop()
        show_image(app)


# Function for applying gray scale effect to the image using ImageOps
def apply_grayscale(app):
    if app.model.image is None:
        return
    app.model.undo_stack.append(app.model.image.copy())
    app.model.image = ImageOps.grayscale(app.model.image)
    show_image(app)

# Function for applying blur filter to the image
def apply_blur(app):
    if app.model.image is None:
        return
    app.model.undo_stack.append(app.model.image.copy())
    app.model.image = app.model.image.filter(ImageFilter.BLUR)
    show_image(app)

# Function for rotating the image
def rotate_image(app):
    if app.model.image is None:
        return
    app.model.undo_stack.append(app.model.image.copy())
    app.model.image = app.model.image.rotate(90, expand=True)
    show_image(app)