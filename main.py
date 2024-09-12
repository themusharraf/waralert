import traceback
from utils.send_email import EmailSender

email = EmailSender()


def send_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = str(e)
            context = traceback.format_exc()
            # Elektron pochta jo'natish # noqa
            email.send_email(
                subject="Xato sodir bo'ldi",  # noqa
                body=f"Xato xabari: {error_message}\n\nIzoh:\n{context}",  # noqa
            )

    return wrapper


@send_exception
def capture_exception():
    print(1 / 0)


capture_exception()
