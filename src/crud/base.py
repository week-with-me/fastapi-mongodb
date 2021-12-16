from typing import TypeVar, Generic, Optional, List
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId

CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema =  TypeVar('UpdateSchema', bound=BaseModel)


class CRUDBase(Generic[CreateSchema, UpdateSchema]):
    def __init__(self, collection) -> None:
        self.collection = collection
        
    async def get_by_id(self, id: str, request: Request) -> Optional[dict]:          
        document = await request.app.db[self.collection].find_one({'_id': id})
        document['_id'] = str(document['_id'])
        
        return document
        
    async def get_multi(
        self,
        skip: Optional[int],
        limit: Optional[int],
        request: Request,
        sort: Optional[List[str]]
    ) -> list:
        query = request.app.db[self.collection].find()
        
        if sort:
            sort_field = []
            
            if type(sort) is list:
                for query_string in sort:
                    field, order = query_string.split(' ')
                    
                    field = field.replace('-', '_')
                    
                    if order == 'asc':
                        order = ASCENDING
                    elif order == 'desc':
                        order = DESCENDING
                    else:
                        raise ValueError
                    
                    sort_field.append((field, order))
        
            else:
                field, order = sort.split(' ')
        
                field = field.replace('-', '_')
                
                if order == 'asc':
                    order = ASCENDING
                elif order == 'desc':
                    order = DESCENDING
                else:
                    raise ValueError
                
                sort_field.append((field, order))
        
            query = query.sort(sort_field)
        
        documents = await query.skip(skip).limit(limit).to_list(length=None)
        
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