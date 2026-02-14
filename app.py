from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

minhas_tarefas = {}

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluida_tarefa: bool

@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa!"}
    return {"tarefas": list(minhas_tarefas.values())}
    
@app.post("/adiciona")
def post_tarefas(tarefa: Tarefa):
    if tarefa.nome_tarefa in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe, colega!")
    minhas_tarefas[tarefa.nome_tarefa] = tarefa.dict()
    return {"message": "A tarefa foi criada com sucesso!"}
    
@app.put("/concluir/{nome_tarefa}")
def concluir_tarefa(nome_tarefa: str):
    tarefa = minhas_tarefas.get(nome_tarefa)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    tarefa["concluida_tarefa"] = True
    return {"message": "A sua tarefa foi concluída com sucesso!"}
    

@app.delete("/deletar/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str):
    if nome_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    del minhas_tarefas[nome_tarefa]
    return {"message": "Sua tarefa foi deletada com sucesso!"}