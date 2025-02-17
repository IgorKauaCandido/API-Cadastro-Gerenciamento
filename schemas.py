from pydantic import BaseModel, ConfigDict

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # ✅ Correção aqui

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoriaOut(ObrigacaoAcessoriaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  