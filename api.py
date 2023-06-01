from importlib import import_module
from argyaml import BaseHandler
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/api/{request:path}/")
async def make_request(request: str):
    args = request.split('/')
    try:
        handler = BaseHandler(args=args)
    except:
        BaseHandler._meta = {}
        return 404
    try:
        path = handler.get_path(handler.handlers_dir)
        result = import_module(path).Handler(server=True)
        response = result.response
        result.__del__()
    except ModuleNotFoundError:
        BaseHandler._meta = {}
        return 404
    BaseHandler._meta = {}
    return response


app.mount("/", StaticFiles(directory="ui", html=True), name="static")
