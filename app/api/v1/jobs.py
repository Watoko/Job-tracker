"""
Job application API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db
from app.models.user import User
from app.repositories.job import JobRepository
from app.schemas.job import (
    JobApplicationCreate,
    JobApplicationRead,
    JobApplicationUpdate,
)
from app.services.job import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Job Applications"],
)


@router.post(
    "",
    response_model=JobApplicationRead,
    status_code=201,
)
def create_job(
    job_in: JobApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new job application.
    """

    service = JobService(JobRepository(db))

    try:
        return service.create_job(
            job_in=job_in,
            user_id=current_user.id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=list[JobApplicationRead],
)
def get_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve all job applications for the current user.
    """

    service = JobService(JobRepository(db))

    return service.get_user_jobs(current_user.id)


@router.get(
    "/{job_id}",
    response_model=JobApplicationRead,
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve a single job application.
    """

    service = JobService(JobRepository(db))

    try:
        job = service.get_job(job_id)

        if job.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to access this job application.",
            )

        return job

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.put(
    "/{job_id}",
    response_model=JobApplicationRead,
)
def update_job(
    job_id: int,
    job_in: JobApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update a job application.
    """

    service = JobService(JobRepository(db))

    try:
        job = service.get_job(job_id)

        # Ensure users can only update their own jobs.
        if job.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to update this job application.",
            )

        return service.update_job(
            job_id=job_id,
            job_in=job_in,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.delete(
    "/{job_id}",
    status_code=204,
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Delete a job application.
    """

    service = JobService(JobRepository(db))

    try:
        job = service.get_job(job_id)

        # Ensure users can only delete their own jobs.
        if job.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to delete this job application.",
            )

        service.delete_job(job_id)

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )