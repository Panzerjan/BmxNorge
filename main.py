import json
import uuid
from datetime import datetime
import random

class RaceGenerator:
    def __init__(self, track_file, commissioner_file, race_file):
        self.track_file = track_file
        self.commissioner_file = commissioner_file
        self.race_file = race_file

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{file_path}'.")
            return None
        
    def write_data(self, data):
        try:
            if "races" not in data:
                data["races"] = []
            with open(self.race_file, 'w') as file:
                json.dump(data, file, indent=4)
            print("Race JSON file updated successfully.")
        except Exception as e:
            print(f"Error writing to file '{self.race_file}': {e}")

    def generate_race(self, track_id, race_date, type_of_race):
        track_data = self.load_data(self.track_file)
        commissioner_data = self.load_data(self.commissioner_file)
        race_data = self.load_data(self.race_file)

        if None in (track_data, commissioner_data):
            print("Failed to generate race: Data could not be loaded.")
            return
        if race_data is None:
            race_data = {"races": []}

        for track in track_data.get("track", []):
            if track["Id"] == track_id:
                race = {
                    "Id": str(uuid.uuid4()),  # Generate unique ID for race
                    "TrackId": track_id,  # Include track ID
                    "Club": track["Club"],
                    "location": track["location"],
                    "Country": track["Country"],
                    "typeOfRace": type_of_race,
                    "date": race_date,
                    "address": track["address"],
                    "commissioners": []
                }

                matching_commissioners = [c for c in commissioner_data["commissioner"] if c["club"] !3= track["Club"]]
                if matching_commissioners:
                    selected_commissioners = random.sample(matching_commissioners, min(2, len(matching_commissioners)))
                    race["commissioners"] = selected_commissioners

                if "races" not in race_data:
                    race_data["races"] = []  # Initialize races if not present
                race_data["races"].append(race)
                self.write_data(race_data)
                return race

        print(f"No track found with ID '{track_id}'.")
        return None

def main():
    generator = RaceGenerator("./files/track.json", "./files/comi.json", "./files/race.json")

    track_id = input("Enter Track ID: ")
    race_date = input("Enter Race Date (YYYY-MM-DD): ")
    race_type = input("Enter Race Type (Local, National, Training): ")

    try:
        datetime.strptime(race_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    race_data = generator.generate_race(track_id, race_date, race_type)

    if race_data:
        print("Race JSON file updated with the new race.")

if __name__ == "__main__":
    main()
