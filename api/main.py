from fastapi import FastAPI

from lib.employers import get_employers


app = FastAPI()


@app.get('/employers/')
async def read_results():
    results = await get_employers()
    return results