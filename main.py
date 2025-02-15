from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresas/", response_model=schemas.EmpresaOut)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa_by_cnpj(db, empresa.cnpj)
    if db_empresa:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    return crud.create_empresa(db, empresa)

@app.get("/empresas/", response_model=list[schemas.EmpresaOut])
def list_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db)

@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaOut)
def create_obrigacao_acessoria(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao_acessoria(db, obrigacao)

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoriaOut])
def list_obrigacoes_acessorias(db: Session = Depends(get_db)):
    return crud.get_obrigacoes_acessorias(db)
