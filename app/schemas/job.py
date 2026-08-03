"""
Pydantic schemas for job applications.
"""

from datetime import date

from pydantic import BaseModel


class JobApplicationBase(BaseModel):
    """
    Shared job application fields.
    """

    company: str
    position: str
    status: str = "Applied"
    location: str | None = None
    salary: int | None = None
    notes: str | None = None
    applied_date: date
    follow_up_date: date | None = None


class JobApplicationCreate(JobApplicationBase):
    """
    Schema for creating a job application.
    """


class JobApplicationUpdate(BaseModel):
    """
    Schema for updating a job application.
    """

    company: str | None = None
    position: str | None = None
    status: str | None = None
    location: str | None = None
    salary: int | None = None
    notes: str | None = None
    applied_date: date | None = None
    follow_up_date: date | None = None


class JobApplicationRead(JobApplicationBase):
    """
    Schema returned to clients.
    """

    id: int
    user_id: int

    model_config = {
        "from_attributes": True,
    }
