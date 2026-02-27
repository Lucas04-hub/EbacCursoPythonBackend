from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

minhas_tarefas = {}

class TarefaDB(Base):
    __tablename__ = "tarefas"

    nome = Column(String, primary_key=True, index=True)
    descricao = Column(String, index=True)
    conluida = Column(String, index=True)

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluida_tarefa: bool = False

Base.metadata.create_all(bind=engine)



def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def listar_tarefas(page: int = 1, limit: int = 10, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(security)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page ou limit estão com valores inválidos!!!")
    
    tarefas = db.query(TarefaDB).offset((page - 1) * limit).limit(limit).all()

    if not tarefas:
        return {"message": "Não existe nenhum livro!!!"}


    total_tarefas = db.query(TarefaDB).count()

    return {
        "page": page,
        "limit": limit,
        "total": total_tarefas,
        "tarefas": [{"nome_tarefa": tarefa.nome_tarefa, "descricao_tarefa": tarefa.descricao_tarefa, "conluida_tarefa": tarefa.concluida_terfa} for tarefa in tarefas]
    }


@app.post("/tarefas")
def post_tarefa(tarefa: Tarefa, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(security)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome_tarefa == TarefaDB.nome_tarefa, TarefaDB.descricao_tarefa == TarefaDB.descricao_tarefa).first()
    if db_tarefa:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe dentro do banco de dados!!!")
    
    nova_tarefa = TarefaDB(nome_tarfea=TarefaDB.nome_livro, descricao_tarefa=TarefaDB.descricao_tarefa, concluida_tarefa=TarefaDB.concluida_tarefa)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return {"messgae": "A tarefa foi criada com sucesso!"}
    
@app.put("/tarefas/{nome_tarefa}/concluir")
def concluir_tarefa(nome_tarefa: str, tarefa: Tarefa, db: Session = Depends(sessao_db)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome == nome_tarefa).first()
    if not db_tarefa:
        raise HTTPException(status_code=400, details="Esta tarefa foi encontrada no seu banco de dados!")

    db_tarefa.nome_tarefa = tarefa.nome_tarefa
    db_tarefa.descricao_tarefa = tarefa.descricao_tarefa
    db_tarefa.concluida_tarefa = tarefa.concluida_tarefa

    db.commit()
    db.refresh(db_tarefa)

    return {"message": "A tarefa foi atualizada com sucesso!!!"}

@app.delete("/tarefas/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(security)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome == nome_tarefa).filter()
    
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Esta tarefa não foi encontrada no seu banco de dados!!!")
    
    db.delete(db_tarefa)
    db.commit
    
    return {"message": "Sua tarefa foi deletada com sucesso!"}