import json


def add_race(races):
    # Load the data from the JSON file
    with open("./Python/comi/race.json", "r") as infile:
        data = json.load(infile)

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
    with open("./Python/comi/race.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


races_to_add = [{'location': 'Sola Bmx', 'type': 'National', 'date': '22042023'},    {
    'location': 'Sola Bmx', 'type': 'National', 'date': '23042023'}]

add_race(races_to_add)
