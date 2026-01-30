class InsightReport:
    def __init__(self, average_daily_screen_time, top_usage_category, risky_site_visits):
        self.screen_time = average_daily_screen_time
        self.app_usage = top_usage_category
        self.risky_count = risky_site_visits

    def generate(self):
        return {
            "average_daily_screen_time": round(self.screen_time, 2),
            "top_usage_category": self.app_usage,
            "risky_site_visits": self.risky_count
        }

    def pretty(self):
        return f"""
--- Digital Footprint Insights ---
 Average daily screen time: {round(self.screen_time,2)} minutes
 High {self.app_usage} usage
 Risky site visits: {self.risky_count}
"""
