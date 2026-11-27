from fastapi import FastAPI, HTTPException, status 
from typing import Literal
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK!"}

class SubmissionIn(BaseModel):
    problem_id: int = Field(gt=0)
    language: Literal["python"]
    code: str = Field(min_length=1, max_length=20_000)

submissions={}

@app.post("/submissions", status_code=202)
def create_submission(data: SubmissionIn):
    submission_id = uuid4()
    submissions[submission_id] = {
        "id": submission_id,
        "status": "queued",
        **data.model_dump(),
    }
    return {"id": submission_id, "status": "queued"}

@app.get("/submissions/{submission_id}")
def get_submission(submission_id: UUID):
    if submission_id not in submissions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Submission not found")
        
    return submissions[submission_id]
        

