import json
import uuid


def add_commissar(name, com_type, club, status, id=None):
    # Open the JSON file and load the data into a Python dictionary
    with open("./files/comi.json", "r") as f:
        commissars = json.load(f)

    if id is None:
        id = str(uuid.uuid4())

    # Check if the new commissar already exists in the dictionary
    commissar_names = [c["name"] for c in commissars["commissioner"]]
    if name in commissar_names:
        print(f"{name} already exists in the list of Commissars.")
        return

    commissars["commissioner"].append(
        {"id": id, "name": name, "type": com_type, "club": club, "status": status})

    # Write the updated dictionary back to the JSON file
    with open("./files/comi.json", "w") as outfile:
        json.dump(commissars, outfile, indent=4)

    print(f"{name} has been added to the list of Commissars.")


add_commissar('Endre boe', 'local', "Sola Bmx", "Aktiv")
