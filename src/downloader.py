"""
downloader.py

Created on 2021-01-18
Updated on 2021-01-18

Copyright © Ryan Kan

Description: Helps download the images and save it into the images folder.
"""

# IMPORTS
import os

import requests
from tqdm import tqdm


# FUNCTIONS
def download_file(url, folder_to_save_it_into=""):
    """
    Downloads a single file at the `url`.

    Args:
        url (str)

        folder_to_save_it_into (str)
    """

    local_filename = os.path.join(folder_to_save_it_into, url.split("/")[-1])  # This is the ending file name

    with requests.get(url, stream=True) as r:
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred; image will be skipped:\n{e}")

        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def download_files(links, downloads_folder="imgs"):
    """
    Downloads the files.

    Args:
        links (list[str]):
            Links to the files.

        downloads_folder (str):
            Path to the downloads folder.
    """

    for link in tqdm(links, desc="Downloading"):
        download_file(link, downloads_folder)


# DEBUG CODE
if __name__ == "__main__":
    download_files(["https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg",
                    "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                    "https://www.google.com/logos/doodles/2021/petrona-eyles-155th-birthday-6753651837108842-2x.png"],
                   "../imgs")
