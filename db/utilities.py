import csv
from sqlalchemy.orm import Session
from typing import List

from . import models

filepath = 'data/jobs.csv'


def data_to_csv(data: List):
    with open(filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def get_jobs(db: Session, job_id: int = 0, limit: int = 100):
    jobs = db.query(models.Job).filter(
        models.Job.job_id >= job_id).limit(limit).all()
    return jobs


def get_job_by_id(db: Session, job_id: int):
    j = db.query(models.Job).filter(models.Job.job_id == job_id).first()
    data_to_csv([j.job_id, j.job_name, j.job_summary])
    return job_id
