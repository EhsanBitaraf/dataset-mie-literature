import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
DATA_FILE_NAME = "dataset-mie.json"
DATA_FILE_PATH = DATA_DIR / DATA_FILE_NAME
OUTPUT_DIR = ROOT / "output"
CLI_ALERT_POINT = 500