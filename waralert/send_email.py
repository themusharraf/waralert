import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


class EmailSender:
    def __init__(self):
        self.from_email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.to_email = os.getenv("TO")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email(self, subject, body):
        # SMTP serveriga ulanish # noqa
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.from_email, self.password)

            # Emailni yaratish # noqa
            msg = MIMEMultipart()
            msg["From"] = self.from_email
            msg["To"] = self.to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "html"))

            # Emailni yuborish # noqa
            server.sendmail(self.from_email, self.to_email, msg.as_string())
