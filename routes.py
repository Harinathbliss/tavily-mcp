from fastapi import APIRouter
from pydantic import BaseModel
import requests

class Demo(BaseModel):
    query:str


router = APIRouter(prefix="/api")


@router.post('/search')
def search_query(request:Demo):
    request_query = request.model_dump()
    url = "https://api.tavily.com/search"
    payload = {
        "query":request_query['query'],
        "api_key":"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"
    }
    k = requests.post(url,json=payload)
    return k.json()