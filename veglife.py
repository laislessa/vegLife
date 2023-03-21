from fastapi import FastAPI,HTTPException,status
from models import Produto
import uvicorn

app = FastAPI()

produtos = {
    1: {
    'titulo':'Futuro Burger 2030',
    'preco':'20,00'
    },
    2: {
    'titulo' : 'Futuro Frango',
    'preco':'18,00'
    },
    3: {
    'titulo' : 'Almôndega Futuro',
    'preco':'22,00'
    },
    3: {
    'titulo' : 'Futuro Burger Defumado',
    'preco':'21,00'
    },
    4: {
    'titulo' :'Nuggets de Frango Incrivel',
    'preco':'15,00'
    },
    5:{
    'titulo' : 'Isca de Peixe Incrivel',
    'preco':'16,00'
    },
    6:{
    'titulo' : 'Carne de Soja',
    'preco':'8,00'
    }
}

@app.get('/')
async def inicio():
    return {"texto":"Living a green life!"} 

@app.get('/home')
async def home():
    return {"Bem-vindo a vegLife! "} 


@app.get('/produtos/')
async def listar_produtos():
    return produtos

@app.get('/produtos/{produtos_id}')
async def detalhar_produtos(produtos_id:int):
    try:
        produto = produtos[produtos_id]
        return produto
    except KeyError:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail = 'Produto inexistente.')

@app.post('/produtos/', status_code=status.HTTP_201_CREATED)
async def produto_curso(produto: Produto):
   id = len(produtos) + 1
   produtos[id] = produto
   return produtos

@app.put('/produtos/{produtos_id}')
def atualizar_produtos(produtos_id : int, produto:Produto):
    produtos[produtos_id] = produto
    return{"Alerta" : "Produto atualizado!"}
    
@app.delete('/produtos/{produtos_id}')
def deletar_produto( produtos_id : int):
    try:
        del produtos[produtos_id]
        return{"Alerta":"Produto deletado!"}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail = 'Produto inexistente.')

if __name__ == '__veglife__':

    uvicorn.run("veglife:app",
                host ="0.0.0.0",
                port=8000,
                reload=True
                )