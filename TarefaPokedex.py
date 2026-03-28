from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI()

async def busca_pokemon_kanto():
    tempo = random.uniform(1, 5)
    await asyncio.sleep(tempo)
    return "Pikachu"

async def busca_pokemon_johto():
    tempo = random.uniform(1, 5)
    await asyncio.sleep(tempo)
    return "Cyndaquil"

async def busca_pokemon_hoenn():
    tempo = random.uniform(1, 5)
    await asyncio.sleep(tempo)
    return "Mudkip"

@app.get("/buscar_pokemons")
async def buscar_pokemons():
    inicio = time.perf_counter()
    
    pokemons = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn()
    )
    fim = time.perf_counter()
    tempo_total = fim - inicio
    return {
        "Kanto": pokemons[0],
        "Johto": pokemons[1],
        "Hoenn": pokemons[2],
        "Tempo_total_segundos": round(tempo_total, 2)
    }