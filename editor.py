from PIL import ImageEnhance, ImageFilter, ImageOps
from open_save_close import show_image

def adjust_brightness(app, value):
    if app.image is None:
        return
    app.undo_stack.append(app.image.copy())
    enhancer = ImageEnhance.Brightness(app.original_image)
    app.image = enhancer.enhance(float(value))
    show_image(app)

def undo(app):
    if app.undo_stack:
        app.redo_stack.append(app.image.copy())
        app.image = app.undo_stack.pop()
        show_image(app)

def redo(app):
    if app.redo_stack:
        app.undo_stack.append(app.image.copy())
        app.image = app.redo_stack.pop()
        show_image(app)



def apply_grayscale(app):
    if app.image is None:
        return
    app.undo_stack.append(app.image.copy())
    app.image = ImageOps.grayscale(app.image)
    show_image(app)

def apply_blur(app):
    if app.image is None:
        return
    app.undo_stack.append(app.image.copy())
    app.image = app.image.filter(ImageFilter.BLUR)
    show_image(app)

def rotate_image(app):
    if app.image is None:
        return
    app.undo_stack.append(app.image.copy())
    app.image = app.image.rotate(90, expand=True)
    show_image(app)