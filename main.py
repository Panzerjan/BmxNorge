<<<<<<< HEAD
import tkinter as tk
from app.dashboard import Dashboard
=======
from bmx.comi import CommissionerManager
from bmx.race import RaceManager


def main():
    path = "./files/comi.json"
    filepath = "./files/race.json"
    manager = RaceManager(filepath)

    races_to_add = [{'location': 'Raade Bmx',
                     'type': 'National', 'date': '02072023'}]

    manager.add_race(races_to_add)
    manager.add_country_to_races()
    manager.add_description_to_races()
>>>>>>> b4d28f2c9532a14ff9ed16f7d151f3217ff41ad2

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        
        self.dashboard = Dashboard(self)
        self.dashboard.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
