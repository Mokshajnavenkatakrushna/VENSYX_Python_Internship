

# 📊 Digital Footprint Analyzer (Privacy-Focused)

A fully **offline**, **privacy-focused** analytics engine that analyzes personal 
digital activity—including **screen time**, **app usage**, and **browsing logs**—to 
generate meaningful insights about productivity and online habits.

No data leaves your machine.  
No cloud uploads.  
Everything runs locally.

---

# 🚀 Features

### ✔ **Offline Analytics**
All analysis happens on your device. No internet or third-party services.

### ✔ **Weekly Insights**
For each week, the system reads:
- `screen_time.csv`
- `app_usage.csv`
- `browsing.txt`

And generates a summary report.

### ✔ **Smart Insight Generation**
Outputs include:
- **Average daily screen time**
- **Most-used app category** (Productivity / Social / Entertainment / etc.)
- **Number of risky site visits**  
  (based on a predefined list: YouTube, Facebook, Snapchat, TikTok)

### ✔ **Clean Modular Architecture**
Designed for scalability and maintainability using:
- OOP Models  
- Encapsulated insights  
- Utilities for streaming + file reading  
- Caching system to avoid repeated computation

### ✔ **Error Handling**
Graceful handling of missing files or invalid data using custom exceptions.

---

# 📁 Project Structure


```
digital_footprint_analyzer/
│
├── data/
│    └── week1/
│        ├── screen_time.csv
│        ├── app_usage.csv
│        └── browsing.txt
│   
│
├── core/
│   ├── models.py
│   ├── analyzer.py
│   ├── insights.py
│   ├── cache.py
│   └── exceptions.py
│
├── utils/
│   ├── docstream.py
│   └── file_readers.py
│
├── cache/
│   └── week1.json (auto-generated)
│
└── main.py

```

---

# 🧠 How It Works (Flow Summary)

```

1. User runs main.py
2. System checks if a cached report exists
3. If cache available → load results instantly
4. Otherwise:
   - Read CSV + text files
   - Parse and clean data
   - Process screen/app/browsing logs
   - Generate insights
   - Save to cache
5. Display formatted weekly insight report

```

---

# 📄 Data Input Format

### **1. screen_time.csv**
```

date,minutes
2026-01-01,320
2026-01-02,410
2026-01-03,290
...

```

### **2. app_usage.csv**
```

app,category,minutes
YouTube,Entertainment,60
VSCode,Productivity,180
Instagram,Social,90
...

```

### **3. browsing.txt**
```

youtube.com
instagram.com
stackoverflow.com
facebook.com
snapchat.com

```

---

# 📊 Example Output

```

--- Digital Footprint Insights ---
Average daily screen time: 354.3 minutes
High Productivity usage
Risky site visits: 3

````

---

# 🛠 Installation & Setup

## 1️⃣ Clone the repository
```bash
git clone https://github.com/yourname/digital_footprint_analyzer.git
cd digital_footprint_analyzer
````

## 2️⃣ Install Python (3.8+ recommended)

Check version:

```bash
python3 --version
```

## 3️⃣ Prepare your weekly data

Put files inside:

```
data/week1/
data/week2/
...
```

Example:

```
data/week1/screen_time.csv
data/week1/app_usage.csv
data/week1/browsing.txt
```

## 4️⃣ Run the application

```bash
python main.py
```

---

# 🧩 Core Modules (Explanation)

## 🔶 `core/models.py`

Contains the main data models:

* **ScreenTime**
* **AppUsage**
* **BrowsingData**

Each performs internal calculations like averages, category totals, risky site counts.

---

## 🔶 `core/analyzer.py`

The **central processing engine**:

* Loads CSV + text files
* Validates data
* Delegates processing to models
* Returns computed insights

---

## 🔶 `core/insights.py`

Formats and structures the final output.

Creates:

* JSON-ready insight dictionary
* Friendly, formatted text report

---

## 🔶 `core/cache.py`

Stores and retrieves weekly analysis reports.

Reduces computation time by loading saved insights when available.

---

## 🔶 `core/exceptions.py`

Custom exceptions:

* `DataNotFoundError`
* `CacheNotFoundError`

---

## 🔶 `utils/docstream.py`

Generator-based file streaming for memory-efficient reading.

---

## 🔶 `utils/file_readers.py`

Provides CSV-reading utilities.

---

## 🔶 `main.py`

Entry point of the project:

* Selects week
* Loads or generates insights
* Shows final formatted report

---

# ⚠️ Important Notes

### 🔹 If you change the InsightReport field names

➡ Make sure to **delete old cached JSON files** in `/cache/`.

### 🔹 Ensure CSV files do not contain invalid formatting.

The project uses a robust CSV loader to avoid issues.

---

# 🧪 Future Improvements (Optional Enhancements)

You can extend the project with features like:

* 📈 Weekly comparison charts (matplotlib)
* 🌐 Web dashboard (Flask/React)
* 📱 Mobile UI
* 🎯 Productivity scoring system
* 🔍 Detecting app addiction trends
* 📔 Export report as PDF
* 🤖 AI-based productivity suggestions

Just ask if you want me to build any of these.

---

# 👨‍💻 Author

Mokshajna Venkata Krushna
