"""
Class for building the top meanu i.e Upload, File (Save/Save As), Undo, Redo, Exit.
"""
import tkinter as tk
import tkinter.font as tkfont


class MenuBar:
    def __init__(self, app):
        self._app = app
        self._editor = app.editor
        self._build_menu()

    def _build_menu(self):
        menu_frame = tk.Frame(self._app.root, bg="#1a1a2e")
        menu_frame.pack(side=tk.TOP, fill=tk.X)

        menu_font  = tkfont.Font(family="Segoe UI", size=10)
        button_font = tkfont.Font(family="Segoe UI", size=11, weight="bold")

        # button upload
        tk.Button(
            menu_frame, text="Upload",
            font=button_font,
            bg="#6C63FF", fg="white",
            activebackground="#5A52D5", activeforeground="white",
            relief=tk.FLAT, cursor="hand2",
            padx=20, pady=10, borderwidth=0,
            command=self._editor.open_img          # calls ImageEditor method
        ).pack(side=tk.LEFT, padx=10, pady=10)

        # File dropdown
        file_btn = tk.Menubutton(
            menu_frame, text="File",
            font=button_font,
            bg="#16213e", fg="white",
            activebackground="#0f3460", activeforeground="white",
            relief=tk.FLAT, cursor="hand2",
            padx=20, pady=10, borderwidth=0
        )
        file_menu = tk.Menu(file_btn, tearoff=0, font=menu_font,
                            bg="#f8f9fa", fg="#1a1a2e", bd=0)
        file_menu.add_command(label="💾 Save",    command=self._editor.save_img)
        file_menu.add_command(label="📝 Save As", command=self._editor.save_as_img)
        file_btn.config(menu=file_menu)
        file_btn.pack(side=tk.LEFT, padx=5, pady=10)

        # Undo button
        tk.Button(
            menu_frame, text="Undo",
            font=button_font,
            bg="#FF6B6B", fg="white",
            activebackground="#EE5A52", activeforeground="white",
            relief=tk.FLAT, cursor="hand2",
            padx=20, pady=10, borderwidth=0,
            command=self._editor.undo
        ).pack(side=tk.LEFT, padx=5, pady=10)

        # Redo button
        tk.Button(
            menu_frame, text="Redo",
            font=button_font,
            bg="#4ECDC4", fg="white",
            activebackground="#45B7AF", activeforeground="white",
            relief=tk.FLAT, cursor="hand2",
            padx=20, pady=10, borderwidth=0,
            command=self._editor.redo
        ).pack(side=tk.LEFT, padx=5, pady=10)

        # Exit button
        tk.Button(
            menu_frame, text="Exit",
            font=button_font,
            bg="#E74C3C", fg="white",
            activebackground="#C0392B", activeforeground="white",
            relief=tk.FLAT, cursor="hand2",
            padx=20, pady=10, borderwidth=0,
            command=self._app.root.destroy
        ).pack(side=tk.LEFT, padx=5, pady=10)