"""
Demonstrates:
- Single Responsibility Principle
- Open/Closed Principle
- Dependency Inversion
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import Iterable

@dataclass
class SalesRecord:
    order_id: int
    amount: float
    date: date

class ReportGenerator(ABC):
    """Abstract base for report generators"""
    @abstractmethod
    def generate(self, records: Iterable[SalesRecord]) -> str:
        pass

class HTMLReportGenerator(ReportGenerator):
    def generate(self, records: Iterable[SalesRecord]) -> str:
        html = "<table><tr><th>Order ID</th><th>Amount</th></tr>"
        for record in records:
            html += f"<tr><td>{record.order_id}</td><td>${record.amount:.2f}</td></tr>"
        return html + "</table>"

class CSVReportGenerator(ReportGenerator):
    def generate(self, records: Iterable[SalesRecord]) -> str:
        csv = "Order ID,Amount\n"
        for record in records:
            csv += f"{record.order_id},{record.amount:.2f}\n"
        return csv

class ReportService:
    """Service that adheres to Dependency Inversion"""
    def __init__(self, generator: ReportGenerator):
        self.generator = generator
    
    def create_report(self, records: Iterable[SalesRecord]) -> str:
        return self.generator.generate(records)

# Usage
records = [
    SalesRecord(101, 12.99, date.today()),
    SalesRecord(102, 24.50, date.today())
]

html_report = ReportService(HTMLReportGenerator()).create_report(records)
print(html_report)
