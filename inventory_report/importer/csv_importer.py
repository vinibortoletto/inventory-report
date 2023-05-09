from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def get_content_from_csv(path):
        with open(path, encoding="utf-8") as file:
            file_content = csv.DictReader(file)
            return [row for row in file_content]

    @staticmethod
    def import_data(file_name):
        file_type = file_name.split(".")[1]

        if file_type != "csv":
            raise ValueError("Arquivo inválido")

        return CsvImporter.get_content_from_csv(file_name)
