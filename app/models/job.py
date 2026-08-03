"""
Job application model.
"""

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class JobApplication(Base):
    """
    Represents a job application submitted by a user.
    """

    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(255), nullable=False)

    position = Column(String(255), nullable=False)

    status = Column(
        String(50),
        default="Applied",
        nullable=False,
    )

    location = Column(String(255), nullable=True)

    salary = Column(Integer, nullable=True)

    notes = Column(Text, nullable=True)

    applied_date = Column(Date, nullable=False)

    follow_up_date = Column(Date, nullable=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="job_applications",
    )
