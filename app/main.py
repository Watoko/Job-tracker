"""
Main entry point for the Job Tracker API.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Job Tracker API",
    version="0.1.0",
    description="Backend API for tracking job applications.",
)


@app.get("/")
async def root():
    """Root endpoint to verify the API is running."""
    return {"message": "Job Tracker API is running!"}