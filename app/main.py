from fastapi import FastAPI, status
from pydantic import BaseModel


class Primo(BaseModel):
    name: str
    email: str
    age: int


app = FastAPI(title="API da PodCodar")

PRIMOS_DB = []  # NUNCA FAÇA ISSO!


@app.get("/")
def get_root():
    """Rota para a raiz"""
    return {"message": "ok!"}


@app.get("/primos", response_model=list[Primo])
def get_primos():
    return PRIMOS_DB


@app.post("/primos", status_code=status.HTTP_201_CREATED)
def create_primo(primo_data: Primo):
    PRIMOS_DB.append(primo_data)
    return primo_data
