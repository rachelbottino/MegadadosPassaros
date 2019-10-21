import pymysql

###################################################################################
#Posts do usuário em ordem cronológica reversa
###################################################################################

def consulta_1(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT titulo FROM post WHERE id_usuario = %s  ORDER BY id_post DESC',(id_usuario))
        res = cursor.fetchall()
        posts = tuple((x[0],x[1]+' '+x[2]) for x in res)
        return posts

#####################################################################################
#Usuários mais popular de cada cidade.
#####################################################################################

def consulta_2(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT primeiro_nome, ultimo_nome,id_cidade from (SELECT primeiro_nome, ultimo_nome,id_cidade, count(id_usuario) as soma FROM menciona inner join usuario using(id_usuario) group by id_usuario ORDER BY soma desc) t1 group by id_cidade')
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios

#########################################################################################
#Lista de usuários que referenciam um dado usuário
#########################################################################################

def consulta_3(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT post.id_usuario FROM menciona INNER JOIN post using(id_post) WHERE menciona.id_usuario = %s',(id_usuario))
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios

##########################################################################################
#Tabela cruzada de quantidade de aparelhos por tipo e por browser
##########################################################################################

def consulta_4a(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT count(aparelho),aparelho   from visualizou  group by aparelho')
        res = cursor.fetchall()
        aparelhos = tuple(x[0] for x in res)
        return aparelhos
def consulta_4b(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT count(browser),browser   from visualizou  group by browser')
        res = cursor.fetchall()
        browsers = tuple(x[0] for x in res)
        return browsers

###########################################################################################
#Lista com URLs de imagens e respectivos #tags de tipo de pássaro
###########################################################################################
def consulta_5(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT url_foto, id_passaro from post inner join referencia using(id_post)')
        res = cursor.fetchall()
        urls = tuple(x[0] for x in res)
        return urls

