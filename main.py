import tkinter as tk
from menubar import create_menu
from statusbar import create_ui

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assignment Third")
        self.root.geometry("900x600")


        self.image = None
        self.original_image = None
        self.image_path = None
        self.undo_stack = []
        self.redo_stack = []

        create_menu(self)  
        create_ui(self)

        #create_menu(self) and create_ui(self) is likely stateless widget and statefullwidget which helps to create ui and function

if __name__ == "__main__":
    root = tk.Tk()   #it starts the app 
    app = ImageEditorApp(root)
    root.mainloop()   #it is same as runapp() which was start the app in dart and the root.mainloop also does the same function which was done in flutter