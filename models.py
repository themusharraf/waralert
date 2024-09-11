from pydantic import BaseModel


class ErrorReport(BaseModel):
    user_id: str
    error_message: str
    context: str = None
