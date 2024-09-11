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
        try:
            response = requests.post(f"{self.api_url}/report_error/", json=payload)
            if response.status_code == 200:
                print("Error reported successfully")
            else:
                print("Failed to report error")

        except Exception as e:
            print(f"Error during reporting: {str(e)}")
