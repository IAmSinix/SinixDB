import asyncio
import json
import os


class SinixDB:
    def __init__(self):
        self.buffer    = ""
        self.file_path = ""
        
    def load(self, file_path="default.json"):
        self.file_path = file_path
        if not os.path.isfile(self.file_path):
            self.file = open(self.file_path, "w+")
            self.file.write("{}")
            self.file.close()
        self.file = open(self.file_path, "r")
        try:
            self.buffer = json.loads(self.file.read())
        except Exception:
            raise Exception(
                f"The {file_path} format does not match the json format"
            )
        self.file.close()

    def is_json(json_object):
        try:
            json.loads(json_object)
        except ValueError:
            return False
        return True

    def set(self, key, data):
        if not self.check(key):
            self.buffer[str(key)] = {}
        for i in data:
            self.buffer[str(key)][i] = data[i]

    def remove(self, key):
        del self.buffer[str(key)]

    def get(self, key):
        return self.buffer[str(key)]
    
    def get_all(self):
        return self.buffer

    def check(self, key):
        if str(key) in self.buffer:
            return True
        else:
            return False

    def save(self, indent=4):
        self.save_file = open(self.file_path, "w", encoding="utf-8")
        json.dump(self.buffer, self.save_file, indent=indent)
        self.save_file.close()


class AsyncSinixDB:
    def __init__(self):
        self.buffer    = ""
        self.file_path = ""

    async def load(self, file_path="default.json"):
        self.file_path = file_path
        if not os.path.isfile(self.file_path):
            self.file = open(self.file_path, "w+")
            self.file.write("{}")
            self.file.close()
        self.file = open(self.file_path, "r")
        try:
            self.buffer = json.loads(self.file.read())
        except Exception:
            raise Exception(
                f"The {file_path} format does not match the json format"
            )
        self.file.close()

    async def is_json(self, json_object):
        try:
            json.loads(json_object)
        except ValueError:
            return False
        return True

    async def set(self, key, data):
        if not await self.check(key):
            self.buffer[str(key)] = {}
        for i in data:
            self.buffer[str(key)][i] = data[i]

    async def remove(self, key):
        del self.buffer[str(key)]

    async def get(self, key):
        return self.buffer[str(key)]
    
    async def get_all(self):
        return self.buffer

    async def check(self, key):
        if str(key) in self.buffer:
            return True
        else:
            return False

    async def save(self, indent=4):
        self.save_file = open(self.file_path, "w", encoding="utf-8")
        json.dump(self.buffer, self.save_file, indent=indent)
        self.save_file.close()
