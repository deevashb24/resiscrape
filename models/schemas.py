from pydantic import BaseModel, HttpUrl
from typing import Optional, Literal
from datetime import datetime

class ProxyBase(BaseModel):
    ip: str
    port: int
    status: Literal['active', 'inactive', 'banned'] = 'active'
    failure_count: int = 0

class Proxy(ProxyBase):
    id: int
    created_at: datetime

class TargetDomainBase(BaseModel):
    domain: str
    strictness_level: Literal['low', 'medium', 'high']

class TargetDomain(TargetDomainBase):
    id: int
    created_at: datetime

class ScrapingJobBase(BaseModel):
    target_url: HttpUrl
    used_proxy_id: Optional[int]
    success: bool

class ScrapingJob(ScrapingJobBase):
    id: int
    created_at: datetime
