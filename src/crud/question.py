from fastapi import Request

from src.crud.base import CRUDBase
from src.schema import CreateQuestion, UpdateQuestion


class CRUDQuestion(CRUDBase[CreateQuestion, UpdateQuestion]):
    pass


question_crud = CRUDQuestion(collection='questions')