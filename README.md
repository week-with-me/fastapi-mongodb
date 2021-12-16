# :rocket: FastAPI with MongoDB

*:warning: 현재 작업 진행 중입니다!*

## Table Of Contents

* [:tada: Introduce](#tada-introduce)
* [:pushpin: Usage](#pushpin-usage)
    * [Pacakge](#package)
    * [Run](#run)
    * [API Document](#api-document)
    * [Environment Variable](#environment-variable)
    * [Sample Database](#sample-database)


### :tada: Introduce

FastAPI와 MongoDB를 활용한 간단한 비동기 REST API입니다.

MongoDB의 경우 [motor](https://motor.readthedocs.io/en/stable/) 패키지를 활용하여 접근하고 처리했습니다. 이때 데이터베이스 연결은 [main.py](/src/main.py)에서 `on_event` 기능을 통해 구현하였습니다.


### :pushpin: Usage

#### Package

[Poetry](https://python-poetry.org/)를 활용하여 패키지를 관리하였습니다. [pyproject.toml](pyproject.toml) 및 [poetry.lock](poetry.lock) 파일을 통해 패키지를 설치할 수 있습니다. 명령어는 아래와 같습니다.

```sh
poetry install
```

#### Run

정상적으로 패키지를 설치했다면 아래와 같은 명령어를 통해 애플리케이션을 실행할 수 있습니다.

```sh
python -m src.main
```

#### API Document

[http://localhost:8000/docs](http://localhost:8000/docs)로 이동하여 OpenAPI를 통해 작성된 API 문서를 확인할 수 있습니다.

이때 [CRUDBase](/src/crud/base.py)를 활용하여 여러 콜렉션에 대한 CRUD 기능을 종속하여 사용할 수 있게 하였습니다. 예시로 작성된, 다시 말해 CRUDBase를 상속 받아 작성된 [QuestionCRUD](/src/crud/question.py) 및 [QuestionAPI](/src/api/question.py) 사용 방법을 해당 API 문서를 통해 확인할 수 있습니다.

또한 OpenAPI에 작성될 예시 등을 위해 딕셔너리 형태의 스키마를 활용했습니다. 관련해서는 [get_multi](/src/schema/question/response_example/get_multi.py)와 같은 파일이 포함된 `response_model` 디렉토리를 확인하기 바랍니다.

#### Environment Variable

[.env](.env) 파일에 필요한 환경 변수가 적혀있습니다. 해당 환경 변수는 [config.py](/src/core/config.py) 파일에서 관리됩니다.

#### Sample Database

[questions.json](/sample/questions.json) 파일을 활용하여 테스트해 볼 수 있습니다.
