import tkinter as tk
from controller.editor import adjust_brightness, apply_grayscale, apply_blur, rotate_image

def create_ui(app):
    main_frame = tk.Frame(app.root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    app.canvas = tk.Canvas(main_frame, bg="white")
    app.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    control_frame = tk.Frame(main_frame, width=200)
    control_frame.pack(side=tk.RIGHT, fill=tk.Y)

  
    tk.Label(control_frame, text="Controls", font=("Arial", 12, "bold"), fg="red").pack(pady=10)

   
    tk.Label(control_frame, text="Brightness", font=("Arial", 10, "bold"), fg="green").pack()
    app.brightness_slider = tk.Scale(
        control_frame, from_=0.1, to=2.0,
        resolution=0.1, orient=tk.HORIZONTAL,
        command=lambda val: adjust_brightness(app, val)
    )
    app.brightness_slider.set(1.0)
    app.brightness_slider.pack(pady=10)


    tk.Button(
        control_frame, 
        text="Grayscale", 
        width=10, 
        bg="#979799",    
        fg="white",       
        font=("Arial", 10, "bold"),
        command=lambda: apply_grayscale(app)
    ).pack(pady=(20, 5)) 

   
    tk.Button(
        control_frame, 
        text="Blur", 
        width=10, 
        bg="#1E90FF",    
        fg="white",     
        font=("Arial", 10, "bold"),
        command=lambda: apply_blur(app)
    ).pack(pady=5)

    tk.Button(control_frame, text="Rotate 90°", width=10,  bg="#32CD32", fg="white",font=("Arial", 10, "bold"),command=lambda: rotate_image(app) ).pack(pady=10)

 
    app.status = tk.Label(
        app.root, text="No image loaded", font=("Arial", 12, "bold"), padx = 10, pady = 10,
        bd=1, relief=tk.SUNKEN, anchor=tk.W
    )
    app.status.pack(side=tk.BOTTOM, fill=tk.X)