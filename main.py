from typing import List

import uvicorn
from fastapi import FastAPI

from src.responses import TrendItem
from src.services import get_trends, save_trends

app = FastAPI()

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends()

if __name__ == "__main__":
    # Verifica se já existem trending topics salvos
    trends = get_trends()

    # Se não existirem, salva os trending topics
    if not trends:
        save_trends()

    # Inicia o servidor FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)
