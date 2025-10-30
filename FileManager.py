import json
from Countrie import ALL_COUNTRIES

class FileManager:

    def __init__(self, person_data = "data/personData.json"):
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

    def read_file_users(self):
        all_users = None
        try:
            with open(self.person_data, "r") as file:
                all_users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_users = []

        print("\t","-" * 40)
        print(f"\t\033[32m Count users: {len(all_users)} \033[0m")
        print("\t","-" * 40)

        for i in all_users[:5]:
            print(f"\t {i["name"]}, age: {i["age"]}, country: {i["country"]}, profesion: {i["profession"]}")
            print("\t","-" * 40)

    def save_to_sql(self):
        pass

    
    def cleal_json_file(self):
        clean = []
        with open(self.person_data, "w") as f:
            json.dump(clean, f)
