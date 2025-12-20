"""Application paths for your game. This is useful for storing your data files (e.g. settings) or other important files in one place.
"""

import os
from platformdirs import user_data_dir

# App identity
APP_NAME = "my_app"
APP_AUTHOR = "my_name"

# Get the proper app data directory. Set roaming to True if you want it to go under roaming, remove it if you want it to go under local.
APP_DATA_DIR = user_data_dir(APP_NAME, APP_AUTHOR, roaming=True)

# Ensure the directory exists
os.makedirs(APP_DATA_DIR, exist_ok=True)

# File path examples. Create file variables and store them below.
# SETTINGS_FILE = os.path.join(APP_DATA_DIR, "settings.dat")
# SCORES_FILE = os.path.join(APP_DATA_DIR, "scores.dat")