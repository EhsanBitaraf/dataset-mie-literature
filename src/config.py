import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
DATA_FILE = DATA_DIR / "repo.json"
OUTPUT_DIR = ROOT / "output"
CLI_ALERT_POINT = 500