"""
This is the main UI which builds the image display area, the right-side control panel, and the bottom status bar.
"""
import tkinter as tk


class StatusBar:
    def __init__(self, app):
        self._app = app
        # Store reference to the controller (Class Interaction)
        self._editor = app.editor
        self.build_canvas()
        self.build_control()
        self.status_bar()


# Canvash for image display area
    def build_canvas(self):
        main_frame = tk.Frame(self._app.root, bg="#1a1a2e")
        main_frame.pack(fill=tk.BOTH, expand=True)
        self._main_frame = main_frame          

        canvas_frame = tk.Frame(main_frame, bg="#16213e", bd=0)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self._app.canvas = tk.Canvas(canvas_frame, bg="#0f3460", highlightthickness=0)
        self._app.canvas.pack(fill=tk.BOTH, expand=True)

#  function for creating righ side controll bar
    def build_control(self):
        control_frame = tk.Frame(self._main_frame, width=250, bg="#16213e")
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
        control_frame.pack_propagate(False)

        # Scrollable inner areas
        canvas_ctrl = tk.Canvas(control_frame, bg="#16213e", highlightthickness=0)
        scrollbar = tk.Scrollbar(control_frame, orient="vertical", command=canvas_ctrl.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas_ctrl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas_ctrl.configure(yscrollcommand=scrollbar.set)

        inner = tk.Frame(canvas_ctrl, bg="#16213e", width=250)
        canvas_ctrl.create_window((0, 0), window=inner, anchor="nw")

        def on_configure(event):
            canvas_ctrl.configure(scrollregion=canvas_ctrl.bbox("all"))
        inner.bind("<Configure>", on_configure)

        # Header
        header = tk.Frame(inner, bg="#6C63FF", height=60)
        header.pack(fill=tk.X, pady=(0, 15))
        header.pack_propagate(False)
        tk.Label(
            header, text="Controls",
            font=("Segoe UI", 16, "bold"), fg="white", bg="#6C63FF"
        ).pack(pady=15)

        # healper functions
        def section_label(text, color="#4ECDC4"):
            tk.Label(
                inner, text=text,
                font=("Segoe UI", 11, "bold"), fg=color, bg="#16213e"
            ).pack(anchor=tk.W, pady=(10, 6), padx=15)

        def styled_btn(text, command, bg="#3498DB", active="#2980B9"):
            tk.Button(
                inner, text=text, width=18,
                bg=bg, fg="white",
                font=("Segoe UI", 11, "bold"),
                relief=tk.FLAT, cursor="hand2",
                activebackground=active, activeforeground="white",
                borderwidth=0, pady=10,
                command=command
            ).pack(pady=(0, 8), padx=15, fill=tk.X)

        # brightness slider
        section_label("Brightness", "#FFD93D")
        bright_frame = tk.Frame(inner, bg="#16213e")
        bright_frame.pack(fill=tk.X, padx=15)

        self._app.brightness_slider = tk.Scale(
            bright_frame,
            from_=0, to=200, resolution=1,
            orient=tk.HORIZONTAL,
            bg="#16213e", fg="white",
            troughcolor="#0f3460", activebackground="#6C63FF",
            highlightthickness=0, font=("Segoe UI", 9), length=200,
            command=lambda val: self._editor.adjust_brightness(val)
        )
        self._app.brightness_slider.set(100)
        self._app.brightness_slider.pack(fill=tk.X)

        # contrass slider
        section_label("Contrast", "#FFD93D")
        contrast_frame = tk.Frame(inner, bg="#16213e")
        contrast_frame.pack(fill=tk.X, padx=15)

        self._app.contrast_slider = tk.Scale(
            contrast_frame,
            from_=0, to=200, resolution=1,
            orient=tk.HORIZONTAL,
            bg="#16213e", fg="white",
            troughcolor="#0f3460", activebackground="#6C63FF",
            highlightthickness=0, font=("Segoe UI", 9), length=200,
            command=lambda val: self._editor.adjust_contrast(val)
        )
        self._app.contrast_slider.set(100)
        self._app.contrast_slider.pack(fill=tk.X)

        # Apply filter
        section_label("Filters", "#4ECDC4")
        styled_btn("⚫ Grayscale",      self._editor.apply_grayscale,
                   bg="#95A5A6", active="#7F8C8D")
        styled_btn("Blur",           lambda: self._editor.blur_effect_application(5),
                   bg="#3498DB", active="#2980B9")
        styled_btn("Edge Detection", self._editor.apply_edge_dector,
                   bg="#9B59B6", active="#8E44AD")

        # ── Transform ──
        section_label("Transform", "#E67E22")
        styled_btn("Rotate 90°",     lambda: self._editor.img_rotate(90),
                   bg="#2ECC71", active="#27AE60")
        styled_btn("Rotate 180°",    lambda: self._editor.img_rotate(180),
                   bg="#2ECC71", active="#27AE60")
        styled_btn("Rotate 270°",    lambda: self._editor.img_rotate(270),
                   bg="#2ECC71", active="#27AE60")
        styled_btn("Flip Horizontal", self._editor.horizontal_flip_img,
                   bg="#E67E22", active="#D35400")
        styled_btn("Flip Vertical",   self._editor.vertical_flip_img,
                   bg="#E67E22", active="#D35400")
        styled_btn("Resize",          self._editor.img_resize,
                   bg="#F39C12", active="#E08E0B")

        # Reset image
        section_label("Reset", "#E74C3C")
        styled_btn("Reset to Original", self._editor.img_reset,
                   bg="#E74C3C", active="#C0392B")

    # Status bar
    def status_bar(self):
        status_frame = tk.Frame(self._app.root, bg="#6C63FF", height=40)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        status_frame.pack_propagate(False)

        self._app.status = tk.Label(
            status_frame, text="  No image loaded",
            font=("Segoe UI", 11), fg="white", bg="#6C63FF",
            anchor=tk.W, padx=15
        )
        self._app.status.pack(fill=tk.BOTH, expand=True)