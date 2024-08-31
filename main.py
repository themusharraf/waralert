from fastapi import FastAPI, HTTPException
from collections import deque
from models import ErrorReport
import uvicorn

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
        raise HTTPException(status_code=404, detail="No error found")
    else:
        return errors


@app.get("/notify/")
async def notify(error_id: int):
    if error_id not in errors_db:
        raise HTTPException(status_code=404, detail="Error ID not found")
    error = errors_db[error_id]
    return {"message": "Notification sent for error", "error": error}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
