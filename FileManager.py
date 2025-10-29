import json

class FileManager:

    def __init__(self, person_data = "data/personData.json",):
        self.person_data = person_data

    # Функція для запису нових користувачів
    def save_user(self, new_users):
        users = None
        try:
            with open(self.person_data, "r") as file:
                users = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            users = []

        users.append(new_users)

        with open(self.person_data, "w") as file:
            json.dump(users,file, indent=4)

    def read_file(self):
        pass
