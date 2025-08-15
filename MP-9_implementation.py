Got it ✅  
You want a **sample Python application** that can **track sources of data** for a report.

I’ll give you a **simple, well-structured, and well-commented** Python example that:

- Lets you **add reports**  
- Lets you **add data sources** to each report  
- Lets you **view** all reports and their sources  
- Uses **object-oriented design** for clarity  
- Stores data in memory (can be extended to use a database later)

---

```python
"""
Sample Python application to track sources of data for reports.
Author: Your Name
Date: YYYY-MM-DD
"""

from typing import List


class DataSource:
    """
    Represents a single data source for a report.
    """
    def __init__(self, name: str, description: str, url: str):
        self.name = name
        self.description = description
        self.url = url

    def __str__(self):
        return f"{self.name} ({self.url}) - {self.description}"


class Report:
    """
    Represents a report that can have multiple data sources.
    """
    def __init__(self, title: str):
        self.title = title
        self.sources: List[DataSource] = []

    def add_source(self, source: DataSource):
        """Add a data source to the report."""
        self.sources.append(source)

    def list_sources(self):
        """Return a list of all sources for this report."""
        return self.sources

    def __str__(self):
        return f"Report: {self.title} - {len(self.sources)} sources"


class ReportManager:
    """
    Manages multiple reports and their sources.
    """
    def __init__(self):
        self.reports: List[Report] = []

    def create_report(self, title: str) -> Report:
        """Create a new report and add it to the manager."""
        report = Report(title)
        self.reports.append(report)
        return report

    def get_report(self, title: str) -> Report:
        """Find a report by title."""
        for report in self.reports:
            if report.title == title:
                return report
        return None

    def list_reports(self) -> List[Report]:
        """Return all reports."""
        return self.reports


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    manager = ReportManager()

    # Create a new report
    sales_report = manager.create_report("Q1 Sales Report")

    # Add data sources to the report
    sales_report.add_source(DataSource(
        name="Internal Sales DB",
        description="Primary sales database for Q1.",
        url="https://internal.example.com/sales"
    ))
    sales_report.add_source(DataSource(
        name="Market Research Report",
        description="External market trends data.",
        url="https://research.example.com/q1-trends"
    ))

    # Create another report
    finance_report = manager.create_report("Annual Finance Report")
    finance_report.add_source(DataSource(
        name="Finance Department Spreadsheet",
        description="Internal financial data for the year.",
        url="file:///finance/annual.xlsx"
    ))

    # Display all reports and their sources
    for report in manager.list_reports():
        print(report)
        for src in report.list_sources():
            print(f"  - {src}")
```

---

### How this works:
1. **DataSource class**  
   Holds the **name**, **description**, and **URL** of a data source.

2. **Report class**  
   Holds a **title** and a list of `DataSource` objects.

3. **ReportManager class**  
   Manages multiple reports and provides methods to create, retrieve, and list them.

4. **Example usage**  
   Demonstrates creating reports, adding sources, and listing them.

---

### Example Output:
```
Report: Q1 Sales Report - 2 sources
  - Internal Sales DB (https://internal.example.com/sales) - Primary sales database for Q1.
  - Market Research Report (https://research.example.com/q1-trends) - External market trends data.
Report: Annual Finance Report - 1 sources
  - Finance Department Spreadsheet (file:///finance/annual.xlsx) - Internal financial data for the year.
```

---

If you want, I can **extend this code** to:
- Save and load reports from a **JSON file** (persistent storage)  
- Add a **CLI menu** for user interaction  
- Integrate with a **database** for real-world use  

Do you want me to make it **persist the data** so sources aren’t lost when the program ends?