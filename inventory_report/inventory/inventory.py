from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(self, path, report_type):
        with open(path, encoding="utf-8") as file:
            file_content = csv.DictReader(file)
            product_list = [row for row in file_content]

        report = ""

        if report_type == "simples":
            report = SimpleReport.generate(product_list)
        elif report_type == "completo":
            report = CompleteReport.generate(product_list)

        return report
