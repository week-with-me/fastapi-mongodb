import traceback
from typing import Optional, List
from fastapi import status, Request, APIRouter, Body, Query
from fastapi.responses import JSONResponse

from src.crud import question_crud
from src.schema import (
                    CreateQuestion,
                    UpdateQuestion,
                    get_by_id_response_example,
                    get_multi_response_example,
                    create_response_example,
                    update_response_example,
                    delete_response_example
                    )


router = APIRouter()


@router.get('/{question_id}', responses=get_by_id_response_example)
async def get_qustion_by_id(question_id: str, request: Request):
    """
    ObjectID 값을 활용한 MBTI 질문 조회
    """
    try:
        response = await question_crud.get_by_id(
            id = question_id,
            request = request
        )
        
        if response:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {'data': response}
            )
        
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {'data': []}
            )
            
    except TypeError:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {'detail': f'ObjectId {question_id} is Invalid'}
        )
    
    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {'detail': error}
        )

@router.get('s', responses=get_multi_response_example)
async def get_multi_questions(
    request: Request,
    skip: int = Query(
        default = 0,
        description = '페이지네이션의 시작 값',
        example = 0  
    ),
    limit: int = Query(
        default = 0,
        description = '페이지네이션의 종료 값',
        example = 5
    ),
    sort: Optional[List[str]] = Query(
        default = ['question_order asc'],
        description = '정렬을 위한 쿼리 파라미터',
        example = 'question-order+asc'
    )
):
    """
    MBTI 질문 전체 또는 페이지네이션 조회
    """
    try:
        response = await question_crud.get_multi(
            request = request,
            skip = skip,
            limit = limit,
            sort = sort
        )
        
        if len(response) >= 1:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {'data': response}
            )
            
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {'data': []}
            )

    except ValueError:
        return JSONResponse(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            content = {'detail': f'Query String {sort} is Invalid'}
        )
    
    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                content = {'detail': error}
            )
        
@router.post('', responses=create_response_example)
async def create_question(
    request: Request,
    question_data: CreateQuestion = Body(...)
):
    """
    MBTI 질문 생성
    """
    try:
        response = await question_crud.create(
            request = request,
            insert_data = question_data
        )
        
        if response:
            return JSONResponse(
                status_code = status.HTTP_201_CREATED,
                content = {'detail': 'Success'}
            )
        
        else:
            return JSONResponse(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                content = {'detail': 'Database Error'}
            )
        
    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {'detail': error}
        )

        
@router.put('/{question_id}', responses=update_response_example)
async def update_question(
    question_id: str,
    request: Request,
    question_data: UpdateQuestion = Body(...)
):
    """
    MBTI 질문 수정
    """
    try:
        response = await question_crud.update(
            id = question_id,
            request = request,
            update_data = question_data
        )
        
        if response:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {'detail': 'Success'}
            )
        
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {'detail': f'ObjectId {question_id} Not Found'}
            )

    except TypeError:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {'detail': f'ObjectId {question_id} is Invalid'}
        )

    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {'detail': error}
        )
        
        
@router.delete('/{question_id}', responses=delete_response_example)
async def delete_question(question_id: str, request: Request):
    """
    MBTI 질문 삭제
    """
    try:
        response = await question_crud.delete(id=question_id, request=request)
        
        if response:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {'detail': 'Success'}
            )
        
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {'detail': f'ObjectId {question_id} Not Found'}
            )

    except TypeError:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {'detail': f'ObjectId {question_id} is Invalid'}
        )
        
    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {'detail': error}
        )