Got it ✅  
You want a **sample Python application** that can **track sources of data from a report**.

Below is a **simple, clean, and well-commented** implementation using **object-oriented programming**.  
We’ll create:

- `DataSource` class → represents a source of data  
- `Report` class → represents a report containing multiple data sources  
- Example usage → adding sources, listing them, and saving to a file

---

```python
"""
Sample Python application to track sources of data from a report.

Author: Your Name
Date: YYYY-MM-DD
"""

from datetime import datetime
from typing import List
import json


class DataSource:
    """
    Represents a source of data for a report.
    """
    def __init__(self, name: str, source_type: str, location: str, notes: str = ""):
        """
        :param name: Name of the data source
        :param source_type: Type of data source (e.g., 'database', 'API', 'spreadsheet')
        :param location: Where the source can be accessed (e.g., URL, file path)
        :param notes: Additional notes about the source
        """
        self.name = name
        self.source_type = source_type
        self.location = location
        self.notes = notes
        self.added_on = datetime.now()

    def to_dict(self) -> dict:
        """
        Convert the data source to a dictionary for serialization.
        """
        return {
            "name": self.name,
            "source_type": self.source_type,
            "location": self.location,
            "notes": self.notes,
            "added_on": self.added_on.isoformat()
        }


class Report:
    """
    Represents a report that contains multiple data sources.
    """
    def __init__(self, title: str):
        """
        :param title: Title of the report
        """
        self.title = title
        self.sources: List[DataSource] = []

    def add_source(self, source: DataSource) -> None:
        """
        Add a data source to the report.
        """
        self.sources.append(source)
        print(f"✅ Source '{source.name}' added to report '{self.title}'.")

    def list_sources(self) -> None:
        """
        Print all data sources in the report.
        """
        if not self.sources:
            print("⚠️ No sources have been added yet.")
            return

        print(f"\n📄 Data Sources for Report: {self.title}")
        print("-" * 50)
        for idx, src in enumerate(self.sources, start=1):
            print(f"{idx}. {src.name} ({src.source_type})")
            print(f"   Location: {src.location}")
            if src.notes:
                print(f"   Notes: {src.notes}")
            print(f"   Added on: {src.added_on.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 50)

    def save_sources_to_file(self, filename: str) -> None:
        """
        Save the data sources to a JSON file for persistence.
        """
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([src.to_dict() for src in self.sources], f, indent=4)
        print(f"💾 Sources saved to '{filename}'.")


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    # Create a new report
    sales_report = Report("Monthly Sales Report")

    # Add some sources
    sales_report.add_source(DataSource(
        name="Sales Database",
        source_type="Database",
        location="postgresql://sales-db.company.com",
        notes="Contains all sales transactions"
    ))

    sales_report.add_source(DataSource(
        name="Marketing API",
        source_type="API",
        location="https://api.company.com/marketing",
        notes="Provides campaign performance data"
    ))

    # List all sources
    sales_report.list_sources()

    # Save sources to a file
    sales_report.save_sources_to_file("sales_report_sources.json")
```

---

### Features in this code:
- **OOP structure** for clarity and scalability  
- **`DataSource`** class to encapsulate source details  
- **`Report`** class to manage multiple sources  
- **Serialization to JSON** for persistence  
- **Readable console output** for tracking  

---

If you want, I can extend this code into a **CLI application** so users can add/list sources interactively.  
Do you want me to do that next?