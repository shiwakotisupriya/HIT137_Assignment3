import tkinter as tk
from controller.editor import adjust_brightness, apply_grayscale, apply_blur, rotate_image
import tkinter.font as tkfont

def create_ui(app):
    main_frame = tk.Frame(app.root, bg="#1a1a2e")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Canvas with modern styling
    canvas_frame = tk.Frame(main_frame, bg="#16213e", bd=0)
    canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
    
    app.canvas = tk.Canvas(canvas_frame, bg="#0f3460", highlightthickness=0)
    app.canvas.pack(fill=tk.BOTH, expand=True)

    # Control panel with gradient-like effect
    control_frame = tk.Frame(main_frame, width=250, bg="#16213e")
    control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    control_frame.pack_propagate(False)

    # Header
    header_frame = tk.Frame(control_frame, bg="#6C63FF", height=60)
    header_frame.pack(fill=tk.X, pady=(0, 20))
    header_frame.pack_propagate(False)
    
    tk.Label(
        header_frame, 
        text="🎨 Controls", 
        font=("Segoe UI", 16, "bold"), 
        fg="white",
        bg="#6C63FF"
    ).pack(pady=15)

    # Brightness Section
    brightness_section = tk.Frame(control_frame, bg="#16213e")
    brightness_section.pack(fill=tk.X, padx=15, pady=(0, 20))
    
    tk.Label(
        brightness_section, 
        text="☀️ Brightness", 
        font=("Segoe UI", 11, "bold"), 
        fg="#FFD93D",
        bg="#16213e"
    ).pack(anchor=tk.W, pady=(0, 8))
    
    app.brightness_slider = tk.Scale(
        brightness_section, 
        from_=0.1, 
        to=2.0,
        resolution=0.1, 
        orient=tk.HORIZONTAL,
        bg="#16213e",
        fg="white",
        troughcolor="#0f3460",
        activebackground="#6C63FF",
        highlightthickness=0,
        font=("Segoe UI", 9),
        length=200,
        command=lambda val: adjust_brightness(app, val)
    )
    app.brightness_slider.set(1.0)
    app.brightness_slider.pack(fill=tk.X)

    # Filters Section
    filters_frame = tk.Frame(control_frame, bg="#16213e")
    filters_frame.pack(fill=tk.X, padx=15, pady=(0, 10))
    
    tk.Label(
        filters_frame, 
        text="Filters", 
        font=("Segoe UI", 11, "bold"), 
        fg="#4ECDC4",
        bg="#16213e"
    ).pack(anchor=tk.W, pady=(0, 10))

    # Grayscale Button
    grayscale_btn = tk.Button(
        filters_frame, 
        text="⚫ Grayscale", 
        width=18, 
        bg="#95A5A6",    
        fg="white",       
        font=("Segoe UI", 11, "bold"),
        relief=tk.FLAT,
        cursor="hand2",
        activebackground="#7F8C8D",
        activeforeground="white",
        borderwidth=0,
        pady=12,
        command=lambda: apply_grayscale(app)
    )
    grayscale_btn.pack(pady=(0, 10), fill=tk.X)

    # Blur Button
    blur_btn = tk.Button(
        filters_frame, 
        text="💫 Blur", 
        width=18, 
        bg="#3498DB",    
        fg="white",     
        font=("Segoe UI", 11, "bold"),
        relief=tk.FLAT,
        cursor="hand2",
        activebackground="#2980B9",
        activeforeground="white",
        borderwidth=0,
        pady=12,
        command=lambda: apply_blur(app)
    )
    blur_btn.pack(pady=(0, 10), fill=tk.X)

    # Rotate Button
    rotate_btn = tk.Button(
        filters_frame, 
        text="🔄 Rotate 90°", 
        width=18,  
        bg="#2ECC71", 
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief=tk.FLAT,
        cursor="hand2",
        activebackground="#27AE60",
        activeforeground="white",
        borderwidth=0,
        pady=12,
        command=lambda: rotate_image(app)
    )
    rotate_btn.pack(fill=tk.X)

    # Status bar with modern design
    status_frame = tk.Frame(app.root, bg="#6C63FF", height=40)
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)
    status_frame.pack_propagate(False)
    
    app.status = tk.Label(
        status_frame, 
        text="📷 No image loaded", 
        font=("Segoe UI", 11), 
        fg="white",
        bg="#6C63FF",
        anchor=tk.W,
        padx=15
    )
    app.status.pack(fill=tk.BOTH, expand=True)