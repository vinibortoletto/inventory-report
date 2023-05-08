from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def get_content_from_csv(path):
        with open(path, encoding="utf-8") as file:
            file_content = csv.DictReader(file)
            return [row for row in file_content]

    def get_content_from_json(path):
        with open(path) as file:
            return json.load(file)

    def get_content_from_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        content = []

        for element in root:
            item = {}

            for sub_element in element:
                item[sub_element.tag] = sub_element.text

            content.append(item)

        return content

    @classmethod
    def import_data(self, path, report_type):
        file_type = path.split(".")[1]
        product_list = []

        if file_type == "csv":
            product_list = self.get_content_from_csv(path)
        elif file_type == "json":
            product_list = self.get_content_from_json(path)
        elif file_type == "xml":
            product_list = self.get_content_from_xml(path)

        report = ""

        if report_type == "simples":
            report = SimpleReport.generate(product_list)
        elif report_type == "completo":
            report = CompleteReport.generate(product_list)

        return report
