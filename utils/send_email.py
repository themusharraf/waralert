import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, from_email, password):
        self.from_email = from_email
        self.password = password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email(self, subject, body, to_email):
        # SMTP serveriga ulanish # noqa
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.from_email, self.password)

            # Emailni yaratish # noqa
            msg = MIMEMultipart()
            msg["From"] = self.from_email
            msg["To"] = to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "html"))

            # Emailni yuborish # noqa
            server.sendmail(self.from_email, to_email, msg.as_string())
