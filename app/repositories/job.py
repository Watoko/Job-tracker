"""
Repository for job application database operations.
"""

from sqlalchemy.orm import Session

from app.models.job import JobApplication
from app.schemas.job import JobApplicationCreate, JobApplicationUpdate


class JobRepository:
    """
    Repository for CRUD operations on job applications.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        job_in: JobApplicationCreate,
        user_id: int,
    ) -> JobApplication:
        """
        Create a new job application.
        """

        job = JobApplication(
            **job_in.model_dump(),
            user_id=user_id,
        )

        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def get_by_id(
        self,
        job_id: int,
    ) -> JobApplication | None:
        """
        Retrieve a job application by ID.
        """

        return self.db.query(JobApplication).filter(JobApplication.id == job_id).first()

    def get_all_for_user(
        self,
        user_id: int,
    ) -> list[JobApplication]:
        """
        Retrieve all job applications for a user.
        """

        return (
            self.db.query(JobApplication)
            .filter(JobApplication.user_id == user_id)
            .order_by(JobApplication.applied_date.desc())
            .all()
        )

    def update(
        self,
        job: JobApplication,
        job_in: JobApplicationUpdate,
    ) -> JobApplication:
        """
        Update a job application.
        """

        update_data = job_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(job, field, value)

        self.db.commit()
        self.db.refresh(job)

        return job

    def delete(
        self,
        job: JobApplication,
    ) -> None:
        """
        Delete a job application.
        """

        self.db.delete(job)
        self.db.commit()
