import tkinter as tk
from com.comi import CommissionerManager

## TODO add races and create race plan

class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Norway bmx")
        self.label.pack()

        # Button to open add commissioner window
        tk.Button(self, text="Add Commissioner", command=self.open_add_commissioner_window).pack()
        tk.Button(self, text="Add Race", command=self.open_race_window).pack()

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def open_add_commissioner_window(self):
        add_commissioner_window = tk.Toplevel(self.master)
        add_commissioner_window.title("Add Commissioner")
        
        # Labels
        tk.Label(add_commissioner_window, text="Name:").grid(row=0, column=0)
        tk.Label(add_commissioner_window, text="Type:").grid(row=1, column=0)
        tk.Label(add_commissioner_window, text="Club:").grid(row=2, column=0)

        # Entry fields
        self.name_entry = tk.Entry(add_commissioner_window)
        self.type_entry = tk.Entry(add_commissioner_window)
        self.club_entry = tk.Entry(add_commissioner_window)

        self.name_entry.grid(row=0, column=1)
        self.type_entry.grid(row=1, column=1)
        self.club_entry.grid(row=2, column=1)

        # Button to add commissioner
        tk.Button(add_commissioner_window, text="Add Commissioner", command=self.add_commissioner).grid(row=3, columnspan=2)
        tk.Button(add_commissioner_window, text="Remove Commissioner", command=self.remove_commissioner).grid(row=4, columnspan=2)

    def open_race_window(self):
        print("hei")

    def add_commissioner(self):
        name = self.name_entry.get()
        commissioner_type = self.type_entry.get()
        club = self.club_entry.get()
        status = True  # You can change this as needed

        # Validate commissioner type
        if commissioner_type.lower() not in ["local", "national", "international"]:
            self.status_label.config(text="Error: Commissioner type must be 'Local', 'National', or 'International'.")
            return
        
        new_commissioner = {
            "name": name,
            "type": commissioner_type,
            "club": club,
            "status": status
        }
        
        try:
            manager = CommissionerManager("./files/comi.json")
            manager.add_commissioner(new_commissioner)
            self.status_label.config(text="Commissioner added successfully!")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

    def remove_commissioner(self):
        name = self.name_entry.get()
    
        try:
            manager = CommissionerManager("./files/comi.json")
            manager.remove_commissioner(name)
            self.status_label.config(text="Commissioner was removed")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
