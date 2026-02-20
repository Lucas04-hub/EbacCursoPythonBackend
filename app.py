from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets


app = FastAPI()

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

minhas_tarefas = {}

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluida_tarefa: bool = False



def encontrar_tarefa(nome: str):
    return minhas_tarefas.get(nome)

def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )

@app.get("/tarefas")
def listar_tarefas(page: int = 1, limit: int = 10, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page ou limit estão com valores inválidos!!!")

    tarefas = list(minhas_tarefas.values())

    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa!!!"}

    tarefas_ordenadas = sorted(minhas_tarefas.items(), key=lambda x: x[0])

    start = (page - 1) * limit
    end = start + limit

    tarefas_paginadas = [
        {"nome_tarefa": tarefa_data["nome_tarefa"], "descricao_tarefa": tarefa_data["descricao_tarefa"], "concluida_tarefa": tarefa_data.get("concluida_tarefa", False)}
        for id_tarefa, tarefa_data in tarefas_ordenadas[start:end]

    ]

    return {
        "page": page,
        "limit": limit,
        "total": len(tarefas),
        "livros": [tarefa.dict() for tarefa in tarefas_paginadas]
    }


@app.post("/tarefas")
def post_tarefa(tarefa: Tarefa):
    if tarefa.nome_tarefa in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe, colega!")
    minhas_tarefas[tarefa.nome_tarefa] = tarefa
    return {"message": "A tarefa foi criada com sucesso!"}

    
@app.put("/tarefas/{nome_tarefa}/concluir")
def concluir_tarefa(nome_tarefa: str):
    tarefa = minhas_tarefas.get(nome_tarefa)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    tarefa.concluida_tarefa = True
    return {"message": "A sua tarefa foi concluída com sucesso!"}


@app.delete("/tarefas/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str):
    if nome_tarefa not in minhas_tarefas:
        raise HTTPException(status_code=404, detail="Essa tarefa não foi encontrada!")
    del minhas_tarefas[nome_tarefa]
    return {"message": "Sua tarefa foi deletada com sucesso!"}