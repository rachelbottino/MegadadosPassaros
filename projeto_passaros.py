import pymysql
########################################################################################################################################################
#cidade
########################################################################################################################################################

def insert_cidade(conn, nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO cidade (nome_cidade) VALUES (%s)', (nome))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {nome} na tabela cidade')

def find_cidade(conn, nome):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_cidade FROM cidade WHERE nome_cidade = %s', (nome))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def update_cidade(conn, id, novo_nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE cidade SET nome_cidade=%s where id_cidade=%s', (novo_nome, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar nome do id {id} para {novo_nome} na tabela cidade')

def remove_cidade(conn, id):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM cidade WHERE id_cidade=%s', (id))

def lista_cidades(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_cidade from cidade')
        res = cursor.fetchall()
        cidades = tuple(x[0] for x in res)
        return cidades
#######################################################################################################################################################
#usuario
#######################################################################################################################################################

def insert_usuario(conn, nome,sobrenome, email, username, id_cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO usuario (primeiro_nome, ultimo_nome, email, username, id_cidade) VALUES (%s,%s,%s,%s,%s)', (nome,sobrenome,email,username, id_cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {nome} na tabela usuario')

def find_usuario(conn, nome,sobrenome):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario FROM usuario WHERE primeiro_nome = %s AND ultimo_nome = %s', (nome,sobrenome))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_usuario(conn, id):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM usuario WHERE id_usuario=%s', (id))

def update_usuario(conn, id, novo_nome, novo_sobrenome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE usuario SET primeiro_nome=%s, ultimo_nome=%s where id_usuario=%s', (novo_nome,novo_sobrenome, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar nome do id {id} para {novo_nome} na tabela usuario')

def update_usuario_email(conn, id, novo_email):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE usuario SET email=%s where id_usuario=%s', (novo_email, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar email do id {id} para {novo_email} na tabela usuario')

def update_usuario_cidade(conn, id, nova_cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE usuario SET id_cidade=%s where id_usuario=%s', (nova_cidade, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar cidade do id {id} para {nova_cidade} na tabela usuario')




def lista_usuarios(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario from usuario')
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios
############################################################################################################
#passaro
##########################################################################################################

def insert_passaro(conn, especie): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO passaro (especie) VALUES (%s)', (especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {especie} na tabela passaro')

def find_passaro(conn, especie):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_passaro FROM passaro WHERE especie = %s', (especie))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_passaro(conn, id):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM passaro WHERE id_passaro=%s', (id))

def update_passaro(conn, id, novo_nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE passaro SET especie=%s where id_passaro=%s', (novo_nome, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar nome do id {id} para {novo_nome} na tabela passaro')

def lista_passaros(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_passaro from passaro')
        res = cursor.fetchall()
        passaros = tuple(x[0] for x in res)
        return passaros

###################################################################################################################################
#preferencia passaro
###################################################################################################################################
def insert_preferencia_passaro(conn, id_usuario, id_passaro):
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO preferencia_passaro VALUES (%s, %s)', (id_usuario, id_passaro))

def remove_preferencia_passaro(conn, id_usuario, id_passaro):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM preferencia_passaro WHERE id_usuario=%s AND id_passaro=%s',(id_usuario, id_passaro))

def lista_preferencias_passaro(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_passaro FROM preferencia_passaro WHERE id_usuario=%s', (id_usuario))
        res = cursor.fetchall()
        passaros = tuple(x[0] for x in res)
        return passaros
##########################################################################################
#post
##########################################################################################
def insert_post(conn, id_usuario,titulo, texto, url_foto,ativo):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO post (id_usuario, titulo, texto, url_foto,ativo) VALUES (%s,%s,%s,%s,%s)', (id_usuario,titulo, texto, url_foto,ativo))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {titulo} na tabela post')

def find_post(conn, titulo):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_post FROM post WHERE titulo = %s ', (titulo))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_post(conn, id):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM post WHERE id_post=%s', (id))

def update_post_titulo(conn, id, novo_titulo):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE post SET titulo=%s where id_post=%s', (novo_titulo, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não foi possível alterar titulo do id {id} para {novo_titulo} na tabela post')

def update_post_texto(conn, id, novo_texto):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE post SET texto=%s where id_post=%s', (novo_texto, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar texto do id {id} para {novo_texto} na tabela post')

def update_post_url_foto(conn, id, novo_url):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE post SET url_foto=%s where id_post=%s', (novo_url, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar url do id {id} para {novo_url} na tabela post')

def update_post_ativo_foto(conn, id, novo_ativo):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE post SET id_ativo=%s where id_post=%s', (novo_ativo, id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar ativo do id {id} para {novo_ativo} na tabela post')


def lista_posts(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_post from post')
        res = cursor.fetchall()
        posts = tuple(x[0] for x in res)
        return posts
#####################################################################################################
#visualizou
#######################################################################################################
def insert_visualizou(conn, id_post,id_usuario, aparelho, browser,ip,instante):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO visualizou (id_post,id_usuario, aparelho, browser,ip,instante) VALUES (%s,%s,%s,%s,%s,%s)', (id_post,id_usuario, aparelho, browser,ip,instante))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {visualizada} na tabela visualizou')

def find_visualizou(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_view FROM visualizou WHERE id_post = %s ', (id_post))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_visualizou(conn, id):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM visualizou WHERE id_view=%s', (id))


def lista_visualizadas(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_view from visualizou')
        res = cursor.fetchall()
        visualizadas = tuple(x[0] for x in res)
        return visualizadas

##################################################################################################
#menciona
##################################################################################################
def insert_mencao(conn, id_post, id_usuario, ativo):
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO menciona VALUES (%s, %s, %s)', (id_post, id_usuario, ativo))

def remove_mencao(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM menciona WHERE id_post=%s AND id_usuario=%s',(id_post, id_usuario))

def lista_mencoes(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario FROM menciona WHERE id_post=%s', (id_post))
        res = cursor.fetchall()
        mencoes = tuple(x[0] for x in res)
        return mencoes

###############################################################################################
#referencia
###############################################################################################
def insert_referencia(conn, id_post, id_passaro, ativo):
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO referencia VALUES (%s, %s,%s)', (id_post, id_passaro, ativo))

def remove_referencia(conn, id_post, id_passaro):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM referencia WHERE id_post=%s AND id_passaro=%s',(id_post, id_passaro))

def lista_referencia(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_passaro FROM referencia WHERE id_post=%s', (id_post))
        res = cursor.fetchall()
        referencias = tuple(x[0] for x in res)
        return referencias