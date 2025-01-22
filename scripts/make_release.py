import os
import shutil
from pathlib import Path
from no_special_chars import create_no_special_chars

BASE_DIR = Path(__file__).parent.parent


shutil.rmtree(BASE_DIR / "build" / "polski")
shutil.copytree(BASE_DIR / "polski", BASE_DIR / "build" / "polski")

create_no_special_chars()

shutil.make_archive("polish", "zip", BASE_DIR / "build", "polski")
shutil.make_archive(
    "polish_no_special_chars", "zip", BASE_DIR / "build", "polish_no_special_chars"
)
shutil.move(BASE_DIR / "polish.zip", BASE_DIR / "build")
shutil.move(BASE_DIR / "polish_no_special_chars.zip", BASE_DIR / "build")
