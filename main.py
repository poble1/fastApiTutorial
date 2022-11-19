from fastapi import FastAPI

app = FastAPI() # FastAPI 클래스를 바탕으로 app이란 인스턴스를 만듭니다.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/") # GET 메소드로 가장 루트 url로 접속할 경우
async def root(): # root() 함수를 실행하고
    return {"message": "Hello World"} # Hello World란 메시지 반환

# http://127.0.0.1:8000/hello/ruby
# {"message":"Hello ruby"}
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 1. 쿼리 파라미터 얻는 방법
"""
    http://127.0.0.1:8000/items/?skip=2&limit=20
    {"2":20}
    http://127.0.0.1:8000/items
    {"0":10}
"""
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {skip: limit}


# # 2. 경로 파라미터 얻기
# """
#     index.html , 1.html 참고
#     아래 예처럼 그냥 경로에서 값을 얻고 싶은 부분만 { }로 감싸주면 됨
#     그리고 함수 파라미터에 똑같이 추가
# """
# @app.get("/books/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

