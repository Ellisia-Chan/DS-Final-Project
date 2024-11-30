import tkinter as tk

class DragAndDropCard(tk.Label):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.x_offset = event.x
        self.y_offset = event.y

    def on_drag(self, event):
        new_x = self.winfo_x() - self.x_offset + event.x
        new_y = self.winfo_y() - self.y_offset + event.y
        self.place(x=new_x, y=new_y)

    def on_release(self, event):
        # Snap logic example
        if self.winfo_x() < 200:
            self.place(x=100, y=100)
        else:
            self.place(x=400, y=300)

root = tk.Tk()
root.geometry("800x600")

card = DragAndDropCard(root, text="Card", bg="red", width=10, height=5)
card.place(x=400, y=300)

root.mainloop()
