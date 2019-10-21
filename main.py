from fastapi import FastAPI
from pydantic import BaseModel
import json
import pymysql
import logging
from datetime import datetime
import socket

from projeto_passaros import *
from consultas_projeto_passaros import *


class Usuario(BaseModel):
    primeiro_nome: str
    ultimo_nome: str 
    email: str
    username: str
    cidade: str
    novo_nome: str
    novo_sobrenome: str
    novo_email:str
    nova_cidade: str
class Cidade(BaseModel):
    nome: str
    novo_nome: str
class Passaro(BaseModel):
    especie: str
    nova_especie: str

class Post(BaseModel):
    nome_usuario: str
    sobrenome_usuario: str
    titulo: str 
    texto: str
    url_foto: str
    novo_titulo: str
    novo_texto: str
    nova_url_foto: str

class Preferencia(BaseModel):
    nome_usuario: str
    sobrenome_usuario: str
    especie_passaro:  str
class Visualizacao(BaseModel):
    titulo_post: str
    nome_usuario: str
    sobrenome_usuario: str
    aparelho: str
    browser: str

class Menciona(BaseModel):
    nome_usuario: str
    sobrenome_usuario: str
    titulo_post: str
    ativo: int

class Referencia(BaseModel):
    titulo_post: str
    especie_passaro: str
    ativo: int

class Joinha(BaseModel):
    titulo_post: str
    nome_usuario: str
    sobrenome_usuario: str
    reacao: int
    ativo : int

class Segue(BaseModel):
    nome_usuario: str
    sobrenome_usuario: str
    nome_seguir: str
    sobrenome_seguir: str
    ativo: int


app = FastAPI()

with open('config_tests.json', 'r') as f:
    config = json.load(f)
logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
conn = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='passaros'
        )

cont = 0
@app.post("/consulta1")
async def cons1(usuario:Usuario):
    id_usuario=find_usuario(conn, usuario.primeiro_nome,usuario.ultimo_nome)
    res = consulta_1(conn,id_usuario)
    return {"res":res}

@app.get("/consulta2")
async def cons2():
    res = consulta_2(conn)
    return {"res":res}

@app.post("/consulta3")
async def cons3(usuario:Usuario):
    id_usuario=find_usuario(conn, usuario.primeiro_nome,usuario.ultimo_nome)
    res = consulta_3(conn,id_usuario)
    return {"res":res}

@app.get("/consulta4a")
async def cons4a():
    res = consulta_4a(conn)
    return {"res":res}

@app.get("/consulta4b")
async def cons4b():
    res = consulta_4b(conn)
    return {"res":res}

@app.get("/consulta5")
async def cons5():
    res = consulta_5(conn)
    return {"res":res}

@app.get("/usuarios")
async def root():
    res = lista_usuarios(conn)
    return {"usuarios":res}

@app.get("/cidades")
async def root():
    res = lista_cidades(conn)
    return {"cidades":res}

@app.get("/posts")
async def root():
    res = lista_posts(conn)
    return {"posts":res}

@app.post("/adiciona/cidade")
async def adiciona_cidade(cidade: Cidade):

    try:
        insert_cidade(conn, cidade.nome)
    except Exception as e:
        print(e)
    return {'cidade adicionado':cidade.nome}

@app.post("/adiciona/passaro")
async def adiciona_passaro(passaro: Passaro):

    try:
        insert_passaro(conn, passaro.especie)
    except Exception as e:
        print(e)
    return {'passaro adicionado':passaro.especie}



@app.post("/adiciona/usuario")
async def adiciona_usuario(usuario: Usuario):

    try:
        cidade_id = find_cidade(conn,usuario.cidade)
        insert_usuario(conn, usuario.primeiro_nome,usuario.ultimo_nome,usuario.email,usuario.username,cidade_id)
    except Exception as e:
        print(e)
    return {'usuario adicionado':usuario.primeiro_nome}

@app.post("/adiciona/post")
async def adiciona_post(post: Post):

    try:
        usuario_id = find_usuario(conn,post.nome_usuario,post.sobrenome_usuario)
        insert_post(conn, usuario_id, post.titulo, post.texto, post.url_foto, 1)
    except Exception as e:
        print(e)
    return {'post adicionado':post.titulo}

@app.post("/adiciona/preferencia")
async def adiciona_preferencia(preferencia: Preferencia):

    try:
        usuario_id = find_usuario(conn,preferencia.nome_usuario,preferencia.sobrenome_usuario)
        passaro_id = find_passaro(conn,preferencia.especie_passaro)
        insert_preferencia(conn, usuario_id, passaro_id)
    except Exception as e:
        print(e)
    return {'preferencia adicionada':preferencia.nome_usuario}

@app.post("/adiciona/visualizacao")
async def adiciona_visualizacao(visualizacao: Visualizacao):

    try:
        hostname = socket.gethostname()    
        #IPAddr = socket.gethostbyname(hostname)
        IPAddr = '127.0.0.1'
        instante = datetime.now()
        instante = instante.strftime('%Y-%m-%d %H:%M:%S')
        usuario_id = find_usuario(conn,visualizacao.nome_usuario,visualizacao.sobrenome_usuario)
        post_id = find_post(conn, visualizacao.titulo_post)
        insert_visualizou(conn, post_id, usuario_id,visualizacao.aparelho, visualizacao.browser, IPAddr,instante )
    except Exception as e:
        print(e)
    return {'visualizacao adicionada':visualizacao.titulo_post}

@app.post("/adiciona/referencia")
async def adiciona_referencia(referencia: Referencia):

    try:
        post_id = find_post(conn,referencia.titulo_post)
        passaro_id = find_passaro(conn,referencia.especie_passaro)
        insert_referencia(conn, post_id, passaro_id)
    except Exception as e:
        print(e)
    return {'referencia adicionada':referencia.titulo_post}

@app.post("/adiciona/menciona")
async def adiciona_menciona(menciona: Menciona):

    try:
        usuario_id = find_usuario(conn,menciona.nome_usuario,menciona.sobrenome_usuario)
        post_id = find_post(conn,menciona.titulo_post)
        insert_mencao(conn, post_id, usuario_id)
    except Exception as e:
        print(e)
    return {'mencao adicionada':menciona.nome_usuario}

@app.post("/adiciona/joinna")
async def adiciona_joinha(joinha: Joinha):

    try:
        usuario_id = find_usuario(conn,joinha.nome_usuario,joinha.sobrenome_usuario)
        post_id = find_post(conn,joinha.titulo_post)
        insert_joinha(conn, post_id, usuario_id, joinha.reacao)
    except Exception as e:
        print(e)
    return {'joinha adicionada':joinha.nome_usuario}

@app.post("/adiciona/segue")
async def adiciona_segue(segue: Segue):

    try:
        usuario_id = find_usuario(conn,segue.nome_usuario,segue.sobrenome_usuario)
        usuario_segue_id = find_usuario(conn,segue.nome_seguir,segue.sobrenome_seguir)
        insert_segue(conn, usuario_id, usuario_segue_id)
    except Exception as e:
        print(e)
    return {'seguida adicionada':segue.nome_usuario}







###############################################################################
#remove
###############################################################################

@app.post("/remove/cidade")
async def remove_cidade1(cidade: Cidade):

    try:
        cidade_id = find_cidade(conn,cidade.nome)
        remove_cidade(conn,cidade_id)
    except Exception as e:
        print(e)
    return {'cidade removida':cidade.nome}


@app.post("/remove/passaro")
async def remove_passaro1(passaro: Passaro):

    try:
        passaro_id = find_passaro(conn,passaro.especie)
        remove_passaro(conn,passaro_id)
    except Exception as e:
        print(e)
    return {'passaro removido':passaro.especie}

@app.post("/remove/usuario")
async def remove_usuario1(usuario: Usuario):

    try:
        usuario_id = find_usuario(conn,usuario.primeiro_nome,usuario.ultimo_nome)
        remove_usuario(conn, usuario_id)
    except Exception as e:
        print(e)
    return {'usuario removido':usuario.primeiro_nome}

@app.post("/remove/post")
async def remove_post1(post: Post):

    try:
        post_id = find_post(conn,post.titulo)
        update_post_ativo(conn, post_id,0)
    except Exception as e:
        print(e)
    return {'post removido':post.titulo}

@app.post("/remove/preferencia")
async def remove_preferencia1(preferencia: Preferencia):

    try:
        usuario_id = find_usuario(conn,preferencia.nome_usuario,preferencia.sobrenome_usuario)
        passaro_id = find_passaro(conn,preferencia.especie_passaro)
        remove_preferencia(conn, usuario_id,passaro_id)
    except Exception as e:
        print(e)
    return {'preferencia removida removido':preferencia.nome_usuario}

@app.post("/remove/mencao")
async def remove_mencao1(menciona: Menciona):

    try:
        usuario_id = find_usuario(conn,menciona.nome_usuario,menciona.sobrenome_usuario)
        post_id = find_post(conn,menciona.titulo_post)
        update_mencao_ativo(conn, post_id,usuario_id,0)
    except Exception as e:
        print(e)
    return {'mencao removido':menciona.titulo_post}

@app.post("/remove/referencia")
async def remove_referencia1(referencia: Referencia):

    try:
        post_id = find_post(conn,referencia.titulo)
        passaro_id = find_passaro(conn,referencia.especie_passaro)
        update_referencia_ativo(conn, post_id,passaro_id,0)
    except Exception as e:
        print(e)
    return {'referencia removido':referencia.titulo_post}

@app.post("/remove/joinha")
async def remove_joinha1(joinha: Joinha):

    try:
        post_id = find_post(conn,joinha.titulo_post)
        usuario_id = find_usuario(conn,joinha.nome_usuario,joinha.sobrenome_usuario)
        update_joinha_ativo(conn, post_id,usuario_id,0)
    except Exception as e:
        print(e)
    return {'joinha removido':joinha.titulo_post}

@app.post("/remove/segue")
async def remove_segue1(segue: Segue):

    try:
        usuario_id = find_usuario(conn,segue.nome_usuario,segue.sobrenome_usuario)
        segue_id = find_usuario(conn,segue.nome_seguir,segue.sobrenome_seguir)
        update_segue_ativo(conn, usuario_id,segue_id,0)
    except Exception as e:
        print(e)
    return {'seguida removida':segue.nome_usuario}

##########################################################################################
#update
##########################################################################################
@app.post("/update/cidade")
async def muda_cidade(cidade: Cidade):
    
    try:
        cidade_id = find_cidade(conn,cidade.nome)
        update_cidade(conn,cidade_id,cidade.novo_nome)
    except Exception as e:
        print(e)
    return {'cidade atualizada':cidade.novo_nome}

@app.post("/update/passaro")
async def muda_passaro(passaro: Passaro):

    try:
        passaro_id = find_passaro(conn,passaro.especie)
        update_passaro(conn,passaro_id,passaro.nova_especie)
    except Exception as e:
        print(e)
    return {'passaro atualizado':passaro.nova_especie}

@app.post("/update/usuario/nome")
async def muda_nome_usuario(usuario: Usuario):

    try:
        usuario_id = find_usuario(conn,usuario.primeiro_nome,usuario.ultimo_nome)
        update_usuario(conn, usuario_id,usuario.novo_nome,usuario.novo_sobrenome)
    except Exception as e:
        print(e)
    return {'usuario atualizado':usuario.novo_nome}

@app.post("/update/usuario/email")
async def muda_email_usuario(usuario: Usuario):

    try:
        usuario_id = find_usuario(conn,usuario.primeiro_nome,usuario.ultimo_nome)
        update_usuario_email(conn, usuario_id,usuario.email)
    except Exception as e:
        print(e)
    return {'email atualizado':usuario.email}

@app.post("/update/usuario/cidade")
async def muda_nome_usuario(usuario: Usuario):

    try:
        usuario_id = find_usuario(conn,usuario.primeiro_nome,usuario.ultimo_nome)
        cidade_id = find_cidade(conn,usuario.nova_cidade)
        update_usuario_cidade(conn, usuario_id,cidade_id)
    except Exception as e:
        print(e)
    return {'cidade atualizada':usuario.nova_cidade}

@app.post("/update/post/titulo")
async def muda_titulo(post: Post):

    try:
        post_id = find_post(conn,post.titulo)
        update_post_titulo(conn, post_id, post.novo_titulo)
    except Exception as e:
        print(e)
    return {'post atualizado':post.novo_titulo}

@app.post("/update/post/texto")
async def muda_texto(post: Post):

    try:
        post_id = find_post(conn,post.titulo)
        update_post_texto(conn, post_id, post.novo_texto)
    except Exception as e:
        print(e)
    return {'texto atualizado':post.novo_texto}

@app.post("/update/post/url")
async def muda_url(post: Post):

    try:
        post_id = find_post(conn,post.titulo)
        update_post_url_foto(conn, post_id, post.nova_url_foto)
    except Exception as e:
        print(e)
    return {'url atualizado':post.nova_url_foto}

@app.post("/update/joinha/reacao")
async def muda_reacao(joinha: Joinha):

    try:
        usuario_id = find_usuario(conn,joinha.nome_usuario,joinha.sobrenome_usuario)
        post_id = find_post(conn,joinha.titulo)
        joinha_id = find_joinha(conn, post_id,usuario_id)
        update_reacao_joinha(conn, post_id, usuario_id, joinha.reacao)


    except Exception as e:
        print(e)
    return {'reacao atualizada':joinha.reacao}

                                        