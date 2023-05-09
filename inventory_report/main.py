from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    importers = {
        "csv": CsvImporter(),
        "json": JsonImporter(),
        "xml": XmlImporter(),
    }

    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
        file_type = path.split(".")[1]

        report = InventoryRefactor(importers[file_type]).import_data(
            path, report_type
        )

        sys.stdout.write(report)
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
