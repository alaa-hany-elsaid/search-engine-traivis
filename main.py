from fastapi import FastAPI
from app.search_engine import get_trends, search as do_search
app = FastAPI()


@app.get("/")
async def root():
    return {}


@app.get("/api/v2/search")
async def search(query):
    return do_search(query)


@app.get("/api/v2/trends")
async def search(query):
    return get_trends(query)


@app.get("/api/v2/search-and-trends")
async def search(query):
    return do_search(query) + get_trends(query)
