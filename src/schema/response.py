from typing import List, Dict, Union, Optional
from pydantic import BaseModel


class GetOneResponseModel(BaseModel):
    data: Optional[Dict[str, Union[str, int]]]
    
    
class GetMultiResponseModel(BaseModel):
    data: Optional[List[dict]]
    

class CreateResponseModel(BaseModel):
    detail: str
    

class UpdateResponseModel(BaseModel):
    detail: str
    

class DeleteResponseModel(BaseModel):
    detail: str
    
    
class ErrorResponseModel(BaseModel):
    detail: Union[str, list]