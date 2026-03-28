from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import artist

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # change if needed
    allow_credentials=False, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



# cd backend
# pip install python-dotenv
# poetry install
# pip install httpx