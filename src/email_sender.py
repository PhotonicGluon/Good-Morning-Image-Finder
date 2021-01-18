"""
email_sender.py

Created on 2021-01-18
Updated on 2021-01-18

Copyright © Ryan Kan

Description: Sends the email.
"""

# IMPORTS
import smtplib
import ssl
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# FUNCTIONS
def configure_smtp(settings_dict):
    """
    Configures the SMTP gateway.

    Args:
        settings_dict (dict)

    Returns:
        smtplib.SMTP:
            The SMTP connection.

    Raises:
        Exception:
            If anything goes wrong.
    """

    # Create a SSL context
    context = ssl.create_default_context()

    # Try to connect to the server
    try:
        server = smtplib.SMTP(settings_dict["send_email"]["email_host"], settings_dict["send_email"]["email_port"])
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(settings_dict["send_email"]["email_user"], settings_dict["send_email"]["email_password"])

        return server

    except Exception as e:
        raise Exception(f"An exception occurred when logging onto the email server:\n{e}")


def send_emails(settings_dict, subject, body, attachments=None):
    """
    Sends the emails to the recipients.

    Args:
        settings_dict (dict)

        subject (str):
            The subject of the email.

        body (str):
            The body of the email.

        attachments (list[str]):
            Paths to the attachment(s).
            (Default = None)

    Returns:

    """

    # Define default for attachments
    if attachments is None:
        attachments = []

    # Get the server
    server = configure_smtp(settings_dict)

    # Get the recipients
    recipients = settings_dict["receive_email"]["recipients"]

    # Send an email to each recipient
    for recipient in recipients:
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = settings_dict["send_email"]["email_user"]
        message["To"] = recipient
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Add attachments
        for i, attachment in enumerate(attachments):
            # Open file in binary mode
            with open(attachment, "rb") as f:
                # Add file as image
                data = f.read()
                f.close()

            # Create an `MIMEImage` object
            img = MIMEImage(data, "jpg", name=attachment.split("/")[1])

            # Add a header
            img.add_header("Content-Disposition",
                           f"attachment; filename=\"{datetime.today().strftime('%Y-%m-%d')} Image {i + 1}.jpg\"")

            # Attach the image to the email
            message.attach(img)

        # Parse the `MIMEMultipart` as a string
        text = message.as_string()

        # Send the email
        server.sendmail(settings_dict["send_email"]["email_user"], recipient, text)

    # Close the server connection
    server.quit()


# DEBUG CODE
if __name__ == "__main__":
    # Imports
    from src.settings_reader import get_settings

    settings = get_settings("../settings.yaml")
    send_emails(settings, "Test Email For Myself",
                "Hello world! This is a test email! If you see this, this is successful.")
