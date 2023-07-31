from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
from databases import Database
from tortoise import Tortoise

app = FastAPI()
app.include_router(todo_router)
Tortoise.init_models(["api.models.todo"], 'models')
register_tortoise(
    app=app,
    # db_url="sqlite://./todo.db",
    db_url="mysql://root:14021999@localhost:3306/todo",
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models": ["api.models.todo"]}
)

@app.get("/")
def index():
    return {
        "status": "todo api is running"
    }