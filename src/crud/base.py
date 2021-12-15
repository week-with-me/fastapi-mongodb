from typing import TypeVar, Generic, Optional
from bson.objectid import ObjectId
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pydantic.utils import Obj

CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema =  TypeVar('UpdateSchema', bound=BaseModel)


class CRUDBase(Generic[CreateSchema, UpdateSchema]):
    def __init__(self, collection) -> None:
        self.collection = collection
        
    async def get_by_id(self, id: str, request: Request) -> Optional[dict]:
        if not ObjectId.is_valid(id):
            return None
        
        document = await request.app.db[self.collection].find_one({'_id': id})
        document['_id'] = str(document['_id'])
        
        return document
        
    async def get_all(self, request: Request) -> list:        
        documents = await request.app.db[
            self.collection
        ].find().to_list(length=None)
        
        for document in documents:
            document['_id'] = str(document['_id'])

        return documents
    
    async def get_multi(
        self,
        request: Request,
        limit: int,
        skip: int
    ) -> list:
        documents = await request.app.db[self.collection].find().skip(
            skip
        ).limit(
            limit
        ).to_list(length=None)
        
        for document in documents:
            document['_id'] = str(document['_id'])
        
        return documents
        
    async def create(
        self,
        request: Request,
        insert_data: CreateSchema
    ) -> bool:
        inserted_document = await request.app.db[self.collection].insert_one(
            jsonable_encoder(insert_data)
        )
        result = inserted_document.acknowledged
        
        return result
        
    async def update(
        self,
        id: str,
        request: Request,
        update_data: UpdateSchema
    ) -> bool:
        if not ObjectId.is_valid(id):
            return None
        
        update_data = update_data.dict(exclude_none=True)

        updated_document = await request.app.db[
            self.collection
        ].find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': jsonable_encoder(update_data)},
            upsert = False
        )
        
        return updated_document
        
    async def delete(self, id: str, request: Request) -> bool:
        if not ObjectId.is_valid(id):
            return None
        
        deleted_document = await request.app.db[
            self.collection
        ].find_one_and_delete(
            {'_id': ObjectId(id)}
        )
        
        return deleted_document
        
        