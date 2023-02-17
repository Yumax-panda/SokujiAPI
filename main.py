from typing import Union
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from deta import Deta

deta = Deta('ProjectKeyHere')

app = FastAPI()

@app.get('/user/{name}')
async def show(name: str):
    return await get(name)



async def get(name: str) -> JSONResponse:
    db = deta.AsyncBase('sokuji')
    data: dict[str, Union[str, int]] = await db.get(name)
    await db.close()

    try:
        data.pop('key')
        return JSONResponse(content=data)
    except (KeyError, AttributeError):
        return JSONResponse(
            content = {
                'dif': "+0",
                'left': 0,
                'scores': [0,0],
                'teams': ['N/A', 'N/A'],
                'win': 0
            }
        )
