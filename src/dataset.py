

import json
import requests
import os
from pathlib import Path
from src.config import DATA_DIR, DATA_FILE_NAME

CACHE_FILE = DATA_DIR / DATA_FILE_NAME
URL = "https://figshare.com/ndownloader/files/49622217"

def load_dataset_mie():
    if not CACHE_FILE.exists():
        # If cache doesn't exist, download and save the data
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            
            # Ensure the directory exists
            os.makedirs(DATA_DIR, exist_ok=True)
            
            # Save the data to cache
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file)
        else:
            raise Exception(f"Failed to download data: HTTP {response.status_code}")
    else:
        # If cache exists, load from the cache file
        with open(CACHE_FILE, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

    return data