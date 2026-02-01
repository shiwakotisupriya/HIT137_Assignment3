import tkinter as tk
from model.image_model import ImageModel       # Model class
from controller.editor import Editor      # Controller class
from view.menubar import MenuBar               # Top bar
from view.statusbar import StatusBar              # Canvash and control bar


class EditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assignment Third")
        self.root.state("zoomed")

        self.model  = ImageModel()
        self.editor = Editor(self)
        MenuBar(self)
        StatusBar(self)


if __name__ == "__main__":
    root = tk.Tk()
    app = EditorApp(root)
    root.mainloop()