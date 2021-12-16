from src.schema.response import ErrorResponseModel, GetMultiResponseModel

get_multi_response_example = {
    "200": {
        "model": GetMultiResponseModel,
        "description": "성공",
        "content": {
            "application/json": {
                "example": {
                    "data": [
                        {
                            "_id": "61b9a8290a71a767f5684471",
                            "question_order": 1,
                            "question": "처음에 둘은 어떻게 친해졌나요?",
                            "answers": [
                                {
                                    "id": 1,
                                    "content": "name이(가) 먼저 제게 말을 걸어줬어요.",
                                    "personality": "E",
                                },
                                {
                                    "id": 2,
                                    "content": "제가 name에게 먼저 말을 걸었어요.",
                                    "personality": "I",
                                },
                            ],
                        },
                        {
                            "_id": "61b9ab1d79601be2c7220ecd",
                            "question_order": 2,
                            "question": "name의 어떤 부분이 좋았어요?",
                            "answers": [
                                {
                                    "id": 1,
                                    "content": "다른 사람들 앞에서 자신감 있는 모습이 좋았어요.",
                                    "personality": "E",
                                },
                                {
                                    "id": 2,
                                    "content": "한 명, 한 명 배려해주는 세심함이 좋았어요.",
                                    "personality": "I",
                                },
                            ],
                        },
                    ]
                }
            }
        },
    },
    "404": {
        "model": GetMultiResponseModel,
        "description": "존재하지 않는 엔티티",
        "content": {"application/json": {"example": {"data": []}}},
    },
    "422": {
        "model": ErrorResponseModel,
        "description": "유효하지 않은 매개변수 사용",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["query", "skip"],
                            "msg": "field required",
                            "type": "value_error.missing",
                        }
                    ]
                }
            }
        },
    },
}
