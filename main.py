import tkinter as tk
from app.dashboard import Dashboard


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        
        self.dashboard = Dashboard(self)
        self.dashboard.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
