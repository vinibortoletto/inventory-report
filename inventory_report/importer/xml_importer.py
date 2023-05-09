from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
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

    @staticmethod
    def import_data(file_name):
        file_type = file_name.split(".")[1]

        if file_type != "xml":
            raise ValueError("Arquivo inválido")

        return XmlImporter.get_content_from_xml(file_name)
