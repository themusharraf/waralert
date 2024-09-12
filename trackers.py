import requests


class ErrorTracker:
    def __init__(self, api_url, user_id):
        self.api_url = api_url
        self.user_id = user_id

    def report_error(self, error_message, context=None):
        payload = {
            "user_id": self.user_id,
            "error_message": error_message,
            "context": context
        }
