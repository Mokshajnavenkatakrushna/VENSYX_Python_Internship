import os
import csv
from core.models import ScreenTime, AppUsage, BrowsingData
from core.exceptions import DataNotFoundError

class FootprintAnalyzer:

    risky_sites = ["youtube.com", "facebook.com", "snapchat.com", "tiktok.com"]

    def __init__(self, base_path):
        self.base_path = base_path

    def _load_csv(self, path):
        if not os.path.exists(path):
            raise DataNotFoundError(f"Missing file: {path}")

        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                # Skip empty or invalid rows
                if not row or len(row) < 2:
                    continue
                
                # Clean whitespace
                cleaned = [col.strip() for col in row]

                yield cleaned   # generator returns clean row

    def load_week_data(self, week):

        week_path = os.path.join(self.base_path, week)
        if not os.path.isdir(week_path):
            raise DataNotFoundError(f"Week folder not found: {week}")

        # screen_time.csv
        st_data = [
            (date, int(minutes))
            for date, minutes in self._load_csv(os.path.join(week_path, "screen_time.csv"))
        ]
        screen_obj = ScreenTime(st_data)

        # app_usage.csv
        app_usage = [
            (app, category, int(minutes))
            for app, category, minutes in self._load_csv(os.path.join(week_path, "app_usage.csv"))
        ]
        app_obj = AppUsage(app_usage)

        # browsing.txt
        browsing_path = os.path.join(week_path, "browsing.txt")
        if not os.path.exists(browsing_path):
            raise DataNotFoundError("browsing.txt not found")

        with open(browsing_path, "r") as f:
            urls = [line.strip() for line in f]
        browse_obj = BrowsingData(urls)

        return screen_obj, app_obj, browse_obj

    def analyze(self, week):
        screen_obj, app_obj, browse_obj = self.load_week_data(week)

        avg_screen = screen_obj.average
        top_category = app_obj.highest_category
        risky_count = browse_obj.count_risky(self.risky_sites)

        return avg_screen, top_category, risky_count
