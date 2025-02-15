from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
import schemas

def get_empresa_by_cnpj(db: Session, cnpj: str):
    return db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_empresas(db: Session):
    return db.query(Empresa).all()

def create_obrigacao_acessoria(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate):
    db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def get_obrigacoes_acessorias(db: Session):
    return db.query(ObrigacaoAcessoria).all()
