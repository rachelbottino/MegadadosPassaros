import pymysql
########################################################################################################################################################
#cidade
########################################################################################################################################################

def insert_cidade(conn, nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('CALL adiciona_cidade(%s)', (nome))
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
            cursor.execute('CALL adiciona_usuario(%s,%s,%s,%s,%s)', (nome,sobrenome,email,username, id_cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir {nome} na tabela usuario')

def find_usuario(conn, nome,sobrenome): #achar por username
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
            cursor.execute('CALL adiciona_passaro(%s)', (especie))
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
        cursor.execute('CALL adiciona_preferencia(%s, %s)', (id_usuario, id_passaro))

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
def insert_post(conn, id_usuario,titulo, texto, url_foto):
    with conn.cursor() as cursor:
        try:
            cursor.execute('CALL adiciona_post(%s,%s,%s,%s)', (id_usuario,titulo, texto, url_foto))
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

def update_post_ativo(conn, id, novo_ativo): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE post SET ativo=%s where id_post=%s', (novo_ativo, id))
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
            cursor.execute('CALL adiciona_visualizacao(%s,%s,%s,%s,%s,%s)', (id_post,id_usuario, aparelho, browser,ip,instante))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir na tabela visualizou')

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
def insert_mencao(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('CALL adiciona_mencao(%s, %s)', (id_post, id_usuario))

def remove_mencao(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM menciona WHERE id_post=%s AND id_usuario=%s',(id_post, id_usuario))

def update_mencao_ativo(conn, id_post,id_usuario, novo_ativo): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE menciona SET ativo=%s where id_post=%s AND id_usuario = %s', (novo_ativo, id_post,id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar ativo do id para {novo_ativo} na tabela mencao')

def lista_mencoes(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario FROM menciona WHERE id_post=%s ', (id_post))
        res = cursor.fetchall()
        mencoes = tuple(x[0] for x in res)
        return mencoes

###############################################################################################
#referencia
###############################################################################################
def insert_referencia(conn, id_post, id_passaro):
    with conn.cursor() as cursor:
        cursor.execute('CALL adiciona_referencia(%s, %s)', (id_post, id_passaro))

def remove_referencia(conn, id_post, id_passaro):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM referencia WHERE id_post=%s AND id_passaro=%s',(id_post, id_passaro))

def update_referencia_ativo(conn, id_post,id_passaro, novo_ativo): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE referencia SET ativo=%s where id_post=%s AND id_passaro=%s', (novo_ativo, id_post,id_passaro))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar ativo do id para {novo_ativo} na tabela referencia')

def lista_referencia(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_passaro FROM referencia WHERE id_post=%s', (id_post))
        res = cursor.fetchall()
        referencias = tuple(x[0] for x in res)
        return referencias

#################################################################################################
#joinhas
#################################################################################################
def insert_joinha(conn, id_post,id_usuario,reacao):
    with conn.cursor() as cursor:
        try:
            cursor.execute('CALL adiciona_joinha(%s,%s,%s)', (id_post,id_usuario,reacao))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir na tabela joinha')

def find_joinha(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_view FROM joinha WHERE id_post = %s AND id_usuario = %s', (id_post,id_usuario))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_joinha(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM joinha WHERE id_post=%s AND id_usuario=%s', (id_post,id_usuario))

def update_joinha_ativo(conn, id_post,id_usuario, novo_ativo): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE joinha SET ativo=%s where id_post=%s AND id_usuario=%s', (novo_ativo, id_post,id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar ativo do id para {novo_ativo} na tabela joinha')
def update_reacao_joinha(conn, id_post,id_usuario, nova_reacao): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE joinha SET reacao=%s where id_post=%s AND id_usuario=%s', (nova_reacao, id_post,id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar reacao do id para {nova_reacao} na tabela joinha')


def lista_joinhas(conn,id_post):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario FROM joinha WHERE id_post=%s ', (id_post))
        res = cursor.fetchall()
        joinhas = tuple(x[0] for x in res)
        return joinhas

##############################################################################################################
#segue
##############################################################################################################
def insert_segue(conn, id_usuario,id_usuario_seguido):
    with conn.cursor() as cursor:
        try:
            cursor.execute('CALL adiciona_segue(%s,%s)', (id_usuario,id_usuario_seguido))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não é possível inserir na tabela segue')

def find_segue(conn, id_usuario, id_usuario_seguido):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_view FROM segue WHERE id_usuario = %s AND id_usuario_seguido = %s', (id_usuario,id_usuario_seguido))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def remove_segue(conn, id_usuario, id_usuario_seguido):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM segue WHERE id_usuario=%s AND id_usuario_seguido=%s', (id_usuario,id_usuario_seguido))

def update_segue_ativo(conn, id_usuario,id_usuario_seguido, novo_ativo): 
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE segue SET ativo=%s where id_usuario=%s AND id_usuario_seguido=%s', (novo_ativo, id_usuario,id_usuario_seguido))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar ativo do id para {novo_ativo} na tabela segue')


def lista_seguidas(conn,id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id_usuario_seguido FROM segue WHERE id_usuario=%s ', (id_usuario))
        res = cursor.fetchall()
        seguidas = tuple(x[0] for x in res)
        return seguidas