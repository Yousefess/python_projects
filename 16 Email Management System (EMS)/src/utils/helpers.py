import os

import yagmail
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


def send_email(to, subject, contents, attachments=None):
    """
    Send an email using yagmail, with sender credentials from environment variables.

    Parameters
    - to (str or list): The email address(es) of the to(s)
    - subject (str): The subject of the email
    - contents (str or list): The contents of the email
    - attachments (str or list, optional): Path(s) to file(s) to attached

    Returns:
    - bool: True if the email was sent successfully, False otherwise
    """
    try:
        # Get sender credentials from environment variables
        sender_email = os.getenv("EMAIL_SENDER")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            raise ValueError(
                "Sender email or password not found in environment variable."
            )

        # Initialize the SMTP client
        yag = yagmail.SMTP(send_email, sender_password)

        # Send the email
        yag.send(to=to, subject=subject, contents=contents,
                 attachments=attachments)

        logger.success("Email sent successfully!")
    except Exception as e:
        logger.error(f"An error occurred while sending the email: {str(e)}")
        return False
    else:
        return True
    finally:
        # Close the connection
        if "yag" in locals():
            yag.close()
