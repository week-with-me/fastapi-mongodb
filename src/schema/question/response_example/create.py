from src.schema.response import CreateResponseModel

create_response_example = {
    "200": {
        "model": CreateResponseModel,
        "description": "성공",
        "content": {"application/json": {"example": {"detail": "Success"}}},
    }
}
