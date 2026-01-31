import tkinter as tk
from controller.open_save_close import open_image, save_image, save_as_image
from controller.editor import undo, redo
import tkinter.font as tkfont

def create_menu(app):
   
    menu_frame = tk.Frame(app.root, bg="#1a1a2e")
    menu_frame.pack(side=tk.TOP, fill=tk.X)
    
    menu_font = tkfont.Font(family="Segoe UI", size=10)
    button_font = tkfont.Font(family="Segoe UI", size=11, weight="bold")
    
    # Image upload Button along with plesent style
    upload_btn = tk.Button(
        menu_frame,
        text="Upload",
        font=button_font,
        bg="#6C63FF",
        fg="white",
        activebackground="#5A52D5",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0,
        command=lambda: open_image(app)
    )
    upload_btn.pack(side=tk.LEFT, padx=10, pady=10)
    
    # File Menu  buttons i.e save save as
    file_btn = tk.Menubutton(
        menu_frame, 
        text="File",
        font=button_font,
        bg="#16213e",
        fg="white",
        activebackground="#0f3460",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0
    )
    
    file_menu = tk.Menu(file_btn, tearoff=0, font=menu_font, bg="#f8f9fa", fg="#1a1a2e", bd=0)
    file_menu.add_command(label="💾 Save", command=lambda: save_image(app))
    file_menu.add_command(label="📝 Save As", command=lambda: save_as_image(app))
    file_btn.config(menu=file_menu)
    file_btn.pack(side=tk.LEFT, padx=5, pady=10)

    # Undo Button
    undo_btn = tk.Button(
        menu_frame,
        text="Undo",
        font=button_font,
        bg="#FF6B6B", 
        fg="white",
        activebackground="#EE5A52",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0,
        command=lambda: undo(app)
    )
    undo_btn.pack(side=tk.LEFT, padx=5, pady=10)
    
    # Redo Button
    redo_btn = tk.Button(
        menu_frame,
        text="Redo",
        font=button_font,
        bg="#4ECDC4", 
        fg="white",
        activebackground="#45B7AF",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0,
        command=lambda: redo(app)
    )
    redo_btn.pack(side=tk.LEFT, padx=5, pady=10)
    
    # Exit Button
    exit_btn = tk.Button(
        menu_frame,
        text="Exit",
        font=button_font,
        bg="#E74C3C",
        fg="white",
        activebackground="#C0392B",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0,
        command=app.root.destroy
    )
    exit_btn.pack(side=tk.LEFT, padx=5, pady=10)