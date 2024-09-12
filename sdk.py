from main import send_exception


@send_exception
def capture_exception():
    s = "1d"
    print(int(s))


capture_exception()

