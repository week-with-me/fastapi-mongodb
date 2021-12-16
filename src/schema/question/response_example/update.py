from src.schema.response import UpdateResponseModel, ErrorResponseModel


update_response_example = {
    '200': {
        'model': UpdateResponseModel,
        'description': '성공',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Success'
                }
            }
        }
    },
    '400': {
        'model': ErrorResponseModel,
        'description': '유효하지 않은 형태의 ObjectId 요청',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'ObjectId 1234 is Invalid'
                }
            }
        }
    },
    '404': {
        'model': ErrorResponseModel,
        'description': '존재하지 않는 엔티티',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'ObjectId 1234 Not Found'
                }
            }
        }
    }
}