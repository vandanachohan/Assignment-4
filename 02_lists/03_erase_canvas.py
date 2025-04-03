# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
# We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Canvas")

        # Create canvas
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Draw the grid of blue cells
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells.append(cell)

        # Create an eraser (pink rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        # Bind mouse movement for erasing
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        """ Erases blue cells by turning them white when in contact with the eraser """
        # Move the eraser to the current mouse position
        self.canvas.moveto(self.eraser, event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2)

        # Get all items overlapping with the eraser
        overlapping_items = self.canvas.find_overlapping(event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2, 
                                                          event.x + ERASER_SIZE // 2, event.y + ERASER_SIZE // 2)
        
        # Erase all the overlapping blue cells
        for item in overlapping_items:
            if item != self.eraser:  # Ensure the eraser itself isn't erased
                self.canvas.itemconfig(item, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop() 
