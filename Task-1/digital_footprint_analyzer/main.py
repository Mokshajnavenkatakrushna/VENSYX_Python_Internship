from core.analyzer import FootprintAnalyzer
from core.insights import InsightReport
from core.cache import WeekCache

def main():
    analyzer = FootprintAnalyzer(base_path="data")

    week = "week1"   # can be week1/week2/week3 dynamically

    try:
        cache = WeekCache(week)
        result = cache.load()
        print("Loaded from cache:\n")
    except:
        avg, category, risky = analyzer.analyze(week)
        report = InsightReport(avg, category, risky)
        result = report.generate()
        cache.save(result)

    # Print pretty report
    print(InsightReport(**result).pretty())


if __name__ == "__main__":
    main()
