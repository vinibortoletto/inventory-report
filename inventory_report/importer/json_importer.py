from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def get_content_from_json(path):
        with open(path) as file:
            return json.load(file)

    def import_data(file_name):
        file_type = file_name.split(".")[1]

        if file_type != "json":
            raise ValueError("Arquivo inválido")

        return JsonImporter.get_content_from_json(file_name)
