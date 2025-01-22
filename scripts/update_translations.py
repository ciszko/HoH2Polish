from pathlib import Path
import re
import os

BASE_DIR = Path(__file__).parent.parent

HOH2_PATH = Path(
    "/mnt/c/Program Files (x86)/Steam/steamapps/common/Heroes of Hammerwatch 2/"
)

REGEX = r'<string name="(.*?)">(.*?)<\/string>'


def update_translations():
    """Updates files to the latest translations"""
    os.makedirs("./build")
    for eng_file in (HOH2_PATH / "res" / "language" / "english").iterdir():
        pl_file = BASE_DIR / "polski" / eng_file.name
        with pl_file.open() as f:
            pl_lines = f.readlines()

        with eng_file.open() as f:
            eng_lines = f.readlines()

        result = []
        for line in eng_lines:
            if (match := re.search(REGEX, line)) is None:
                result.append(line)
                continue
            groups = match.groups()

            found = next((x for x in pl_lines if groups[0] in x), None)
            if found:
                pl_lines.remove(found)
                result.append(found)
                continue
            result.append(line)

        with open(f"./build/{eng_file.name}", "w") as f:
            f.writelines(result)


if __name__ == "__main__":
    update_translations()
