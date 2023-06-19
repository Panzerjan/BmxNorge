import json
import datetime

file = "./files/track.json"


def get_today_date():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")


def add_track(path, tracks):
    # Load the data from the JSON file
    with open(path, "r") as file:
        data = json.load(file)

    # get today

    today_date = get_today_date()
    # Add each race to the data
    for track in tracks:
        if track['TrackName'] in [r['TrackName'] for r in data['track']]:
            print(
                f"{track['TrackName']} already exists in the list of tracks.")
        else:
            data['track'].append({
                'TrackName': track['TrackName'],
                'location': track['location'],
                'Country': track['Country'],
                'Region': track['Region'],
                'date': today_date,
                'address': track['address']


            })
            print(f"{track['TrackName']} has been added to the list of races.")

    # Write the updated data back to the JSON file
    with open(path, "w") as outfile:
        json.dump(data, outfile, indent=4)


tracks = [{'TrackName': 'Bmx Verona', 'location': 'Verona',
           'Country': 'Italy', 'Region': ' Provinsen Verona', 'address': 'Via Sogare, 1'}, {'TrackName': 'BMX Club Circuit Zolder', 'location': ' Circuit Zolder',
                                                                                            'Country': 'Belgium', 'Region': 'Heusden-Zolder', 'address': 'Terlaemenlaan 30'}]

add_track(file, tracks)
