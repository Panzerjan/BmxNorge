import json
import uuid


class CommissionerReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data


class CommissionerWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)


class CommissionerManager:
    def __init__(self, file_path):
        self.reader = CommissionerReader(file_path)
        self.writer = CommissionerWriter(file_path)

    def add_commissioner(self, commissioner):
        data = self.reader.read_data()

        existing_commissioners = [c['name'] for c in data['commissioner']]
        if commissioner['name'] not in existing_commissioners:
            # Generating a unique ID for the new commissioner
            commissioner_id = str(uuid.uuid4())
            commissioner['id'] = commissioner_id
            # Validating commissioner type
            commissioner_type = commissioner.get('type', '').lower()
            if commissioner_type in ["local", "national", "international"]:
                data['commissioner'].append(commissioner)
                self.writer.write_data(data)
                print(f"Commissioner '{commissioner['name']}' added successfully.")
            else:
                print("Commissioner type must be 'Local', 'National', or 'International'.")
        else:
            print(f"Commissioner '{commissioner['name']}' already exists.")

    def update_commissioner(self, commissioner_id, updated_data):
        data = self.reader.read_data()

        for commissioner in data['commissioner']:
            if commissioner['id'] == commissioner_id:
                commissioner.update(updated_data)
                self.writer.write_data(data)
                print(
                    f"Commissioner '{commissioner['name']}' updated successfully.")
                return

        print(f"Commissioner with ID '{commissioner_id}' not found.")

    def remove_commissioner(self, commissioner):
        data = self.reader.read_data()

        if "commissioner" in data:
            data["commissioner"] = [d for d in data["commissioner"] if d.get("name") != name]
        return data

    def remove_commissioner(self, name):
        data = self.reader.read_data()

        if "commissioner" in data:
            data["commissioner"] = [d for d in data["commissioner"] if d.get("name") != name]
            self.writer.write_data(data)
            print(f"Commissioner '{name}' removed successfully.")
            return
        else:
            print(f"No 'commissioner' data found in the file.")
