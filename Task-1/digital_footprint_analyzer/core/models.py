class ScreenTime:
    def __init__(self, records):
        self.records = records  # list of (date, minutes)

    @property
    def average(self):
        total = sum(m for _, m in self.records)
        return total / len(self.records) if self.records else 0


class AppUsage:
    def __init__(self, usage_list):
        # usage_list: [(app, category, minutes)]
        self.usage_list = usage_list

    def get_category_totals(self):
        totals = {}
        for _, category, minutes in self.usage_list:
            totals[category] = totals.get(category, 0) + minutes
        return totals

    @property
    def highest_category(self):
        totals = self.get_category_totals()
        if not totals:
            return "No Data"
        return max(totals, key=totals.get)


class BrowsingData:
    def __init__(self, urls):
        self.urls = urls

    def count_risky(self, risky_sites):
        return sum(1 for url in self.urls if url in risky_sites)
