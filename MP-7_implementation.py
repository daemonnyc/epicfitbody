Got it ✅.  
You want **sample Python code** for an application to track **sources of data** from a report.  
I’ll provide a **simple, clean, and well-commented** example that can be extended later.

---

## 📌 Design
We’ll create:
1. **`DataSource` class** – represents a data source (name, description, link, date added).
2. **`Report` class** – stores multiple data sources and can display them.
3. A **simple CLI** to add and list sources.

---

```python
"""
Data Source Tracker
-------------------
A simple Python application to track sources of data used in a report.
"""

from datetime import datetime
from typing import List


class DataSource:
    """
    Represents a single data source used in a report.
    """
    def __init__(self, name: str, description: str, link: str):
        self.name = name
        self.description = description
        self.link = link
        self.date_added = datetime.now()

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Link: {self.link}\n"
                f"Date Added: {self.date_added.strftime('%Y-%m-%d %H:%M:%S')}")


class Report:
    """
    Represents a report that contains multiple data sources.
    """
    def __init__(self, title: str):
        self.title = title
        self.sources: List[DataSource] = []

    def add_source(self, source: DataSource):
        """
        Add a new data source to the report.
        """
        self.sources.append(source)
        print(f"✅ Data source '{source.name}' added successfully.")

    def list_sources(self):
        """
        Display all data sources in the report.
        """
        if not self.sources:
            print("⚠️ No data sources found.")
            return

        print(f"\n📄 Data Sources for Report: {self.title}")
        print("-" * 50)
        for idx, source in enumerate(self.sources, start=1):
            print(f"[{idx}]")
            print(source)
            print("-" * 50)


def main():
    """
    Simple CLI to manage data sources for a report.
    """
    report_title = input("Enter the report title: ")
    report = Report(report_title)

    while True:
        print("\n--- Data Source Tracker ---")
        print("1. Add Data Source")
        print("2. List Data Sources")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter source name: ")
            description = input("Enter description: ")
            link = input("Enter source link/URL: ")
            source = DataSource(name, description, link)
            report.add_source(source)

        elif choice == "2":
            report.list_sources()

        elif choice == "3":
            print("👋 Exiting Data Source Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

---

## 🔹 How It Works
1. **Run the script**:
   ```bash
   python data_source_tracker.py
   ```
2. **Enter a report title**.
3. **Add sources** with name, description, and link.
4. **List sources** to see all entries.

---

## 🔹 Possible Enhancements
- Save sources to a **JSON / SQLite database** for persistence.
- Add **search/filter** functionality.
- Export sources to **CSV/Excel**.
- Build a **GUI** using Tkinter or PyQt.

---

Do you want me to **extend this code** so it saves and loads the data sources from a JSON file so they persist after closing the program? That would make it a more useful real-world tool.