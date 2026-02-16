from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()



class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluida_tarefa: bool = False

minhas_tarefas: List[Tarefa] = []

def encontrar_tarefa(nome: str):
    return next((tarefa for tarefa in minhas_tarefas if tarefa.nome_tarefa == nome), None)

@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa!"}
    return {"tarefas": [tarefa.dict() for tarefa in minhas_tarefas]}

@app.post("/tarefas")
def post_tarefa(tarefa: Tarefa):
    if encontrar_tarefa(tarefa.nome_tarefa):
        raise HTTPException(status_code=400, detail="Essa tarefa já existe, colega!")
    minhas_tarefas.append(tarefa)
    return {"message": "A tarefa foi criada com sucesso!"}
    
@app.put("/tarefas/{nome_tarefa}/concluir")
def concluir_tarefa(nome_tarefa: str):
    tarefa = encontrar_tarefa(nome_tarefa)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    tarefa.concluida_tarefa = True
    return {"message": "A sua tarefa foi concluída com sucesso!"}


@app.delete("/tarefas/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str):
    tarefa = encontrar_tarefa(nome_tarefa)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    minhas_tarefas.remove(tarefa)
    return {"message": "Sua tarefa foi deletada com sucesso!"}