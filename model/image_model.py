class image_model:
    def __init__(self):
        self.image = None
        self.original_image = None
        self.image_path = None
        self.undo_stack = []
        self.redo_stack = []

    def reset_history(self):
        self.undo_stack.clear()
        self.redo_stack.clear()
