from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from curl_fetch2py import CurlFetch2Py
from app.api.schemas import RequestData
from app.api.utils import execute_request

router = APIRouter(
    prefix="",
    tags=["API"],
)
templates = Jinja2Templates(directory='app/templates')

@router.get("/", summary="Main page")
async def get_main_page(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})

@router.post("/api", summary="Main API method")
async def main_logic(request: RequestData):
    request_type = request.request_type
    target = request.target
    data_str = request.data_str
    
    try:
        if request_type == "fetch":
            context = CurlFetch2Py.parse_curl_context(data_str)
        elif request_type == "curl":
            context = CurlFetch2Py.parse_fetch_context(data_str)
        else:
            raise ValueError("Invalid request type")
        return {"request_string": execute_request(context, target).strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
