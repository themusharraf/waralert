from fastapi import FastAPI, HTTPException
from utils.send_email import EmailSender
from dotenv import load_dotenv
from models import ErrorReport
from collections import deque
from html import escape
import uvicorn
import os

load_dotenv()

email = EmailSender(from_email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))

app = FastAPI()

# Xatolarni saqlash uchun dict va queue (list) # noqa

errors_db = {}
error_queue = deque()


@app.post("/report_error/")
async def report_error(error: ErrorReport):
    error_id = len(errors_db) + 1

    errors_db[error_id] = {
        "user_id": error.user_id,
        "error_message": error.error_message,
        "context": error.context
    }

    error_queue.append(error_id)
    return {"message": "Error reported successfully", "error_id": error_id}


@app.get("/get_errors/")
async def get_errors():
    errors = [errors_db[error_id] for error_id in error_queue]

    if not errors:
        raise HTTPException(status_code=404, detail="No errors found")

    return errors


@app.get("/notify/")
async def notify(error_id: int):
    if error_id not in errors_db:
        raise HTTPException(status_code=404, detail="Error ID not found")
    errors = [errors_db[error_id] for error_id in error_queue]
    error = errors_db[error_id]
    if error:
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
            <p><code>{escape(errors[0]["error_message"])}</code></p>
            <hr>
            <p><strong>Context:</strong></p>
            <pre><code>{escape(errors[0]["context"])}</code></pre>
        </body>
        </html>
        """
        email.send_email(
            subject=errors[0]["error_message"],
            body=html_body,
            to_email=os.getenv("TO")
        )
        return "message send successfully"

    return {"message": "Notification sent for error", "error": error}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
