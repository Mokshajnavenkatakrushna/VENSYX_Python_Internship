import json
import os

CACHE_DIR = "cache"

class WeekCache:
    def __init__(self, week_name):
        self.week_name = week_name
        self.path = os.path.join(CACHE_DIR, f"{week_name}.json")

    def save(self, data):
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError("No cache found")
        with open(self.path, "r") as f:
            return json.load(f)
