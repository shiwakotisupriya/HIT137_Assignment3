import tkinter as tk
from controller.open_save_close import open_image, save_image, save_as_image
from controller.editor import undo, redo
import tkinter.font as tkfont

def create_menu(app):
   
    menu_frame = tk.Frame(app.root, )  #menuframe is same as row used in flutter which we put item on the horizontal line 
    menu_frame.pack(side=tk.TOP, fill=tk.X) #tk.x  = width: double.,infinity tk.top = column (flutter)
    
    menu_font = tkfont.Font(family="Arial", size=11, weight="bold")
    
    file_btn = tk.Menubutton(
        menu_frame, text="File",
        font=("Arial", 13, "bold"),  
        
    )
    
    file_menu = tk.Menu(file_btn, tearoff=0, font = menu_font)   #tearoff = 0 prevents to show menue item on another screen 
    file_menu.add_command(label="Open", command=lambda: open_image(app))
    file_menu.add_command(label="Save", command=lambda: save_image(app))
    file_menu.add_command(label="Save As", command=lambda: save_as_image(app))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=app.root.destroy)
    file_btn.config(menu=file_menu)
    file_btn.pack(side=tk.LEFT, padx=10, pady=5)

 
    edit_btn = tk.Menubutton(
        menu_frame, text="Edit",
        font=("Arial", 13, "bold"),  
       
    )
    edit_menu = tk.Menu(edit_btn, tearoff=0, font = menu_font)
    edit_menu.add_command(label="Undo", command=lambda: undo(app))
    edit_menu.add_command(label="Redo", command=lambda: redo(app))
    edit_btn.config(menu=edit_menu)
    edit_btn.pack(side=tk.LEFT, padx=10, pady=5)