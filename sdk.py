from main import send_exception


@send_exception
def capture_exception():
    print(1 / 0)


capture_exception()
