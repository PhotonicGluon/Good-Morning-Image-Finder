"""
settings_reader.py

Created on 2021-01-18
Updated on 2021-01-18

Copyright © Ryan Kan

Description: Reads the settings file.
"""

# IMPORTS
import yaml


# FUNCTIONS
def get_settings(settings_file):
    """
    Gets the settings from the settings file.

    Args:
        settings_file (str):
            Path to the settings file.

    Returns:
        dict:
            Dictionary of the settings.
    """

    return yaml.load(open(settings_file, "r"), Loader=yaml.Loader)


# DEBUG CODE
if __name__ == "__main__":
    settings = get_settings("../settings.yaml")
    print(settings)
