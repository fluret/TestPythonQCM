import xml.etree.ElementTree as ET
from typing import List

class MoodleXMLWriter:
    def __init__(self, categories: List):
        self.categories = categories

    def write(self, filepath: str):
        root = ET.Element("quiz")
        for category in self.categories:
            self._add_category_to_xml(category, root)
        tree = ET.ElementTree(root)
        tree.write(filepath, encoding="utf-8", xml_declaration=True)
    
    def _add_category_to_xml(self, category, root):
        cat_element = ET.SubElement(root, "question", {"type": "category"})
        text_element = ET.SubElement(ET.SubElement(cat_element, "category"), "text")
        text_element.text = category.name
