from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="ResiScrape API")

# --- SCHEMA / DICTIONARY DB ---
class Proxy(BaseModel):
    ip: str
    active: bool

class JobResult(BaseModel):
    job_id: str
    target_url: str
    status: str
    data: Optional[str] = None

db = {
    "proxies": [
        {"ip": "192.168.1.100", "active": True},
        {"ip": "10.0.0.5", "active": False},
        {"ip": "172.16.0.2", "active": True}
    ],
    "jobs": []
}

proxy_index = 0

# --- ROUTES ---
@app.get("/api/proxy/next")
def get_next_proxy():
    global proxy_index
    active_proxies = [p for p in db["proxies"] if p["active"]]
    
    if not active_proxies:
        raise HTTPException(status_code=404, detail="No active proxies available")
        
    proxy = active_proxies[proxy_index % len(active_proxies)]
    proxy_index += 1
    
    return {"proxy": proxy["ip"]}

@app.post("/api/jobs")
def submit_job(job: JobResult):
    db["jobs"].append(job.model_dump() if hasattr(job, "model_dump") else job.dict())
    return {"message": "Job submitted successfully", "job_id": job.job_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)
