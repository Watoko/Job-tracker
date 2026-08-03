"""
Business logic for job applications.
"""

from app.models.job import JobApplication
from app.repositories.job import JobRepository
from app.schemas.job import JobApplicationCreate, JobApplicationUpdate


class JobService:
    """
    Business logic for job applications.
    """

    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def create_job(
        self,
        job_in: JobApplicationCreate,
        user_id: int,
    ) -> JobApplication:
        """
        Create a new job application.
        """

        return self.job_repository.create(job_in, user_id)

    def get_job(
        self,
        job_id: int,
    ) -> JobApplication:
        """
        Retrieve a job application by ID.

        Raises:
            ValueError: If the job does not exist.
        """

        job = self.job_repository.get_by_id(job_id)

        if job is None:
            raise ValueError("Job application not found.")

        return job

    def get_user_jobs(
        self,
        user_id: int,
    ) -> list[JobApplication]:
        """
        Retrieve all job applications for a user.
        """

        return self.job_repository.get_all_for_user(user_id)

    def update_job(
        self,
        job_id: int,
        job_in: JobApplicationUpdate,
    ) -> JobApplication:
        """
        Update a job application.

        Raises:
            ValueError: If the job does not exist.
        """

        job = self.job_repository.get_by_id(job_id)

        if job is None:
            raise ValueError("Job application not found.")

        return self.job_repository.update(job, job_in)

    def delete_job(
        self,
        job_id: int,
    ) -> None:
        """
        Delete a job application.

        Raises:
            ValueError: If the job does not exist.
        """

        job = self.job_repository.get_by_id(job_id)

        if job is None:
            raise ValueError("Job application not found.")

        self.job_repository.delete(job)
