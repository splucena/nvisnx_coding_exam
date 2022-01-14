from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from db.connection import SessionLocal
import db.utilities as data_util

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/read/{job_id}/{limit}')
def read(job_id: int, limit: int, db: Session = Depends(get_db)):
    jobs = data_util.get_jobs(db, job_id=job_id, limit=limit)
    
    if jobs is None:
        raise HTTPException(status=404, detail="No jobs found.")

    data = [{'job_id': job.job_id, 'job_name': job.job_name,
             'job_summary': job.job_summary} for job in jobs]
    response = {'data': data, 'size': len(data)}
    return response


@app.get('/api/start_read_all/{job_id}')
def start_read_all(job_id: int, db: Session = Depends(get_db)):
    job = data_util.get_job_by_id(db, job_id)

    if job is None:
        raise HTTPException(status=404, detail="Job not found.")

    response = {'job_id': job}
    return response


@app.get('/api/read_all')
def read_all():
    return FileResponse(path='data/jobs.csv', media_type='application/octet-stream', filename='data/jobs.csv')
