import xml.etree.ElementTree as ET
import os
from pathlib import Path
from unidecode import unidecode

BASE_DIR = Path(__file__).parent.parent


def create_no_special_chars():
    os.makedirs(BASE_DIR / "build" / "polish_no_special_chars", exist_ok=True)
    for file in (BASE_DIR / "polski").iterdir():
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(file, parser)
        root = tree.getroot()

        for line in root:
            try:
                line.text = unidecode(line.text)
            except Exception:
                ...

        tree.write(BASE_DIR / "build" / "polish_no_special_chars" / file.name, "utf-8")


if __name__ == "__main__":
    create_no_special_chars()
