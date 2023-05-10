import json


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
            data['commissioner'].append(commissioner)
            self.writer.write_data(data)
            print(f"Commissioner '{commissioner['name']}' added successfully.")
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
