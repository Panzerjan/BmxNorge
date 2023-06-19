import json


class RaceManager:
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def add_description_to_races(self):
        with open(self.filepath, "r") as file:
            existing_data = json.load(file)

            # Step 2: Update each race with the description
        for race in existing_data["race"]:
            if "description" not in race:
                race["description"] = f"This is a {race['type']} race taking place at {race['location']} on {race['date']}."

            # Step 3: Write the updated content back to the JSON file
            with open(self.filepath, 'w') as file:
                json.dump(existing_data, file, indent=4)

    def add_country_to_races(self):
        with open(self.filepath, "r") as file:
            existing_data = json.load(file)

        # Step 2: Update each race with the Country
        for race in existing_data["race"]:
            if 'country' not in race:
                race['Country'] = 'Norway'

        # Step 3: Write the updated content back to the JSON file
        with open(self.filepath, 'w') as file:
            json.dump(existing_data, file, indent=4)

    def add_race(self, races):
        # Load the data from the JSON file
        with open(self.filepath, "r") as file:
            data = json.load(file)

        # Add each race to the data
        for race in races:
            if race['date'] in [r['date'] for r in data['race']]:
                print(f"{race['date']} already exists in the list of races.")
            else:
                data['race'].append({
                    'location': race['location'],
                    'type': race['type'],
                    'date': race['date']

                })
                print(f"{race['date']} has been added to the list of races.")

        # Write the updated data back to the JSON file
        with open("./files/race.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
