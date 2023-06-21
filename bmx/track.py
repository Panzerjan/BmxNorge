import json
import datetime

file = "./files/track.json"


def find_highest_id(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    highest_id = 0

    for item in data['track']:
        current_id = int(item['Id']) if item['Id'].isdigit() else int(item['Id'])
        if current_id > highest_id:
            highest_id = current_id

    return highest_id


def get_today_date():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")


def add_track(path, tracks):
    # Load the data from the JSON file
    with open(path, "r") as file:
        data = json.load(file)

    highest_id = find_highest_id(path)
    new_id = str(highest_id + 1)

    # get today
    today_date = get_today_date()

    # Add each race to the data
    for track in tracks:
        if track['Club'] in [r['Club'] for r in data['track']]:
            print(
                f"{track['Club']} already exists in the list of tracks.")
        else:
            data['track'].append({
                'Id': new_id,
                'Club': track['Club'],
                'location': track['location'],
                'Country': track['Country'],
                'Region': track['Region'],
                'date': today_date,
                'address': track['address']


            })
            print(f"{track['Club']} has been added to the list of tracks.")

    # Write the updated data back to the JSON file
    with open(path, "w") as outfile:
        json.dump(data, outfile, indent=4)


tracks = [{'Club': 'Aremark BMX', 'location': 'Aremark',
           'Country': 'Norway', 'Region': 'East', 'address': 'Asketjernveien'}, {'Club': 'BOC BMX', 'location': 'Rykkinn',
                                                                                 'Country': 'Norway', 'Region': 'East', 'address': 'Gamle Lommedalsvei 99'}]

add_track(file, tracks)
