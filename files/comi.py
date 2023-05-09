import json
import uuid


class Commissar:

    def __init__(self) -> None:
        pass

    def generate_id(self):
        if not hasattr(self, "id_counter"):
            self.id_counter = 0
        self.id_counter += 1
        return str(self.id_counter)

    def add_commissar(self, name, com_type, club, status, id=None):
        id = self.generate_id()

        # Check if the new commissar already exists in the dictionary
        commissar_names = [c["name"] for c in self.commissars["commissioner"]]
        if name in commissar_names:
            print(f"{name} already exists in the list of Commissars.")
            return

        self.commissars["commissioner"].append(
            {"id": id, "name": name, "type": com_type, "club": club, "status": status})

    def update_commissar(self, id, name=None, com_type=None, club=None, status=None):
        for commissar in self.commissars["commissioner"]:
            if commissar["id"] == id:
                if name:
                    commissar["name"] = name
                if com_type:
                    commissar["type"] = com_type
                if club:
                    commissar["club"] = club
                if status:
                    commissar["status"] = status
                self.save_commissars()
                print(f"Commissar with ID {id} has been updated.")
                return

    def delete_commissar(self, id):
        for i, commissar in enumerate(self.commissars["commissioner"]):
            if commissar["id"] == id:
                del self.commissars["commissioner"][i]
                self.save_commissars()
                print(f"Commissar with ID {id} has been deleted.")
                return

        print(f"Commissar with ID {id} does not exist.")


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, "r") as infile:
            data = json.load(infile)
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
