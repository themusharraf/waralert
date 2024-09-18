import traceback
from html import escape
from waralert.send_email import EmailSender

email = EmailSender()


def send_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = str(e)
            context = traceback.format_exc()
            html_body = f"""
                 <!DOCTYPE html>
                 <html>
                 <head>
                     <style>
                         pre {{
                             background-color: #f4f4f4;
                             border: 1px solid #ddd;
                             border-radius: 4px;
                             padding: 10px;
                             overflow: auto;
                         }}
                         code {{
                             color: #d63384;
                             font-family: monospace;
                         }}
                     </style>
                 </head>
                 <body>
                     <h1>Alert!</h1>
                     <p><strong>Error Message:</strong></p>
                     <p><code>{escape(error_message)}</code></p>
                     <hr>
                     <p><strong>Context:</strong></p>
                     <pre><code>{escape(context)}</code></pre>
                 </body>
                 </html>
                 """
            email.send_email(
                subject="Xato sodir bo'ldi",  # noqa
                body=html_body,  # noqa
            )

    return wrapper
