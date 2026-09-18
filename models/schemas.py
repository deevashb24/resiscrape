from pydantic import BaseModel, UUID4
from typing import Optional

class Proxy(BaseModel):
    id: UUID4
    ip: str
    port: int
    status: str
    failure_count: int

class TargetDomain(BaseModel):
    id: UUID4
    domain: str
    strictness_level: int

class ScrapingJob(BaseModel):
    id: UUID4
    target_url: str
    used_proxy_id: UUID4
    success: bool
