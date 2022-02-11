import json
import pathlib

class SinixDB:
    def __init__(self, file_path):
        self.file_path = pathlib.Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text("{}")
        try:
            self.data = json.loads(self.file_path.read_text())
        except Exception:
            raise Exception(
                f"Формат {file_path} не соответствует формату json"
            )

    def set(self, key, data):
        if not self.check(key):
            self.data[str(key)] = {}
        for i in data:
            self.data[str(key)][i] = data[i]

    def remove(self, key):
        del self.data[str(key)]

    def get(self, key):
        return self.data[str(key)]

    def check(self, key):
        if str(key) in self.data:
            return True
        else:
            return False

    def save(self):
        self.save_file = open(self.file_path, "w", encoding="utf-8")
        json.dump(self.data, self.save_file, indent=4)
        self.save_file.close()