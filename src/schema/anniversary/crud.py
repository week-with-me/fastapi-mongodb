from typing import Dict, Optional

from pydantic import BaseModel


class Anniversary(BaseModel):
    name: Dict[str, str]
    image: str


class CreateAnniversary(Anniversary):
    class Config:
        schema_extra = {
            "example": {
                "name": {"korean": "우정", "english": "Solid\nFriendship"},
                "image": "",
            }
        }


class UpdateAnniversary(Anniversary):
    name: Optional[Dict[str, str]]
    image: str

    class Config:
        schema_extra = {
            "example": {"name": {"korean": "사랑", "english": "Eternal\nLove"}}
        }
