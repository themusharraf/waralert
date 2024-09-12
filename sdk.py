import os
import traceback
from utils.send_email import EmailSender
from dotenv import load_dotenv

load_dotenv()

email = EmailSender(from_email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))


def capture_exception():
    try:
        1 / 0
    except Exception as e:
        error_message = str(e)
        context = traceback.format_exc()
        email.send_email(
            subject="hello",
            body="""
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
            <h1>Alert!</h1>
            
        </body>
        </html>
            """,
            to_email=os.getenv("TO")
        )


capture_exception()
