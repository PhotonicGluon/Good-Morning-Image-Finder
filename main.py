"""
main.py

Created on 2021-01-18
Updated on 2021-01-18

Copyright © Ryan Kan

Description: The main file.
"""

# IMPORTS
import os
from datetime import datetime
from random import sample

from apscheduler.schedulers.background import BlockingScheduler

from src.downloader import download_files
from src.email_sender import send_emails
from src.scraper import search_images_on_google
from src.settings_reader import get_settings

# CONSTANTS
SEARCH_TERM = "Good Morning"
NUM_IMAGES = 100
NUM_IMAGES_TO_SEND = 5

SETTINGS_FILE = "settings.yaml"
IMAGES_DIR = "imgs"

CHECK_IMAGE_HOUR = 7  # In 24 h notation
SEND_EMAIL_HOUR = 8  # In 24 h notation

EMAIL_BODY = """Hello!

Attached to this email you can find today's "Good Morning" images.

Hope you like them!
"""


# FUNCTIONS
def check_available_images():
    """
    Checks if there are sufficient images in the images directory, and if there isn't, replenishes them.
    """

    # Get all available images
    images = os.listdir(IMAGES_DIR)

    # Check if there are enough images
    if len(images) <= NUM_IMAGES_TO_SEND + 1:
        print("Insufficient images; restocking.")

        # Delete the remaining images
        for img in images:
            os.remove(os.path.join(IMAGES_DIR, img))

        # Download the new images
        download_files(search_images_on_google(SEARCH_TERM, num_images=NUM_IMAGES), downloads_folder=IMAGES_DIR)

    print("Images Checked!")


def send_good_morning_email():
    """
    Sends the good morning image email.
    """

    # Choose a random image to send
    images_to_send = [os.path.join(IMAGES_DIR, p) for p in sample(os.listdir(IMAGES_DIR), k=NUM_IMAGES_TO_SEND)]

    # Send the email to the recipients
    send_emails(get_settings(SETTINGS_FILE), "Your \"Good Morning\" Images for "
                                             f"{datetime.today().strftime('%Y-%m-%d')}",
                EMAIL_BODY, attachments=images_to_send)

    # Delete the selected images from the images folder
    for image in images_to_send:
        os.remove(image)

    print("Emails sent!")


# CODE
print("Starting script.")

# Start a blocking scheduler as this is the only process we are running
scheduler = BlockingScheduler()
scheduler.add_job(check_available_images, "cron", hour=CHECK_IMAGE_HOUR)
scheduler.add_job(send_good_morning_email, "cron", hour=SEND_EMAIL_HOUR)
# scheduler.add_job(check_available_images, "cron", second=0)
# scheduler.add_job(send_good_morning_email, "cron", second=30)
scheduler.start()
