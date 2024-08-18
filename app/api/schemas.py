from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class StartEnum(str, Enum):
    fetch = "fetch"
    culr = "curl"
    
class TargetEnum(str, Enum):
    request = "request"
    httpx = "httpx"
    
class RequestData(BaseModel):
    request_type: StartEnum = Field(..., title="Request Type", description="Fetch or Curl")
    target: TargetEnum = Field(..., title="Target", description="Request or Httpx")
    data_str: str = Field(..., title="Data String", description="Input data string")
    