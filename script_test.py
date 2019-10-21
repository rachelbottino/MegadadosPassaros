import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql
from datetime import datetime

from projeto_passaros import *

class TestProjeto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='passaros'
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('START TRANSACTION')

    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

##################################################################################################################################
#cidade
#################################################################################################################################

    def test_insert_cidade(self):
        conn = self.__class__.connection
    
        cidade = 'Campinas'

        # Adiciona uma cidade não existente.
        insert_cidade(conn, cidade)

        # Tenta adicionar o mesma cidade duas vezes.
        try:
            insert_cidade(conn, cidade)
            self.fail('mesma cidade adicionada duas vezes.')
        except ValueError as e:
            pass

        # Checa se a cidade existe.
        id = find_cidade(conn, cidade)
        self.assertIsNotNone(id)

        # Tenta achar uma cidade inexistente.
        id = find_cidade(conn, 'Petrolina')
        self.assertIsNone(id)

    def test_remove_cidade(self):
        conn = self.__class__.connection
        insert_cidade(conn, 'Cotia')
        id = find_cidade(conn, 'Cotia')

        res = lista_cidades(conn)
        self.assertCountEqual(res, (id,))

        remove_cidade(conn, id)

        res = lista_cidades(conn)
        self.assertFalse(res)

    def test_muda_nome_cidade(self):
        conn = self.__class__.connection

        insert_cidade(conn, 'Manaus')

        insert_cidade(conn, 'Peruibe')
        id = find_cidade(conn, 'Peruibe')

        # Tenta mudar nome para algum nome já existente.
        try:
            update_cidade(conn, id, 'Manaus')
            self.fail('Nome ja existente.')
        except ValueError as e:
            pass

        # Tenta mudar nome para nome inexistente.
        update_cidade(conn, id, 'Andrelandia')

        # Verifica se mudou.
        id_novo = find_cidade(conn, 'Andrelandia')
        self.assertEqual(id, id_novo)

    def test_lista_cidades(self):
        conn = self.__class__.connection

        # Verifica que ainda não tem cidades no sistema.
        res = lista_cidades(conn)
        self.assertFalse(res)

        # Adiciona algumas cidades.
        cidades_id = []
        for c in ('Manaus', 'Peruibe', 'Andrelandia'):
            insert_cidade(conn, c)
            cidades_id.append(find_cidade(conn, c))

        # Verifica se as cidades foram adicionados corretamente.
        res = lista_cidades(conn)
        self.assertCountEqual(res, cidades_id)

        # Remove as cidades.
        for c in cidades_id:
            remove_cidade(conn, c)

        # Verifica se todos as cidades foram removidos.
        res = lista_cidades(conn)
        self.assertFalse(res)

#####################################################################################################################################
#usuario
#####################################################################################################################################

    def test_insert_usuario(self):
        conn = self.__class__.connection

        nome = 'Joao'
        sobrenome = 'Castro'
        email = 'jppc@gmail.com'
        cidade = 1
        username = 'joaoppc'

        # Adiciona usuario não existente.
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn, nome,sobrenome,email,username,id_cidade)

        #Adiciona usuário com mesmo nome mas sobrenome diferente
        insert_usuario(conn,nome,'Pieroni','jp@gmail.com','jppc',id_cidade) 

        # Tenta adicionar a mesmo usuario duas vezes.
        try:
            insert_usuario(conn, nome,sobrenome,"asdf@gmail.com",'jppcc',id_cidade)
            self.fail('Tentando adicionar o mesmo usuário duas vezes.')
        except ValueError as e:
            pass
        # Tenta adicionar a mesmo email duas vezes.
        try:
            insert_usuario(conn, "Rachel","Moraes",email,'jpppccc',id_cidade)
            self.fail('Tentando adicionar o mesmo email duas vezes.')
        except ValueError as e:
            pass

        #Tenta adicionar o mesmo username duas vezes
        try:
            insert_usuario(conn, "Rachel","Bottino",'rm@hotmail.com',username,id_cidade)
            self.fail('Tentando adicionar o mesmo username duas vezes.')
        except ValueError as e:
            pass

        # Checa se a usuario existe.
        id = find_usuario(conn, nome, sobrenome)
        self.assertIsNotNone(id)

        # Tenta achar usuario inexistente.
        id = find_usuario(conn, 'Aderbaldo', 'Arantes')
        self.assertIsNone(id)

    def test_remove_usuario(self):
        nome = 'Joao'
        sobrenome = 'Castro'
        email = 'jppc@gmail.com'
        cidade = 1
        username = 'joappc'

        conn = self.__class__.connection
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn, nome,sobrenome,email,username,id_cidade)
        id_usuario = find_usuario(conn, nome, sobrenome)

        res = lista_usuarios(conn)
        self.assertCountEqual(res, (id_usuario,))

        remove_usuario(conn, id_usuario)

        res = lista_usuarios(conn)
        self.assertFalse(res)

    def test_muda_nome_usuario(self):
        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_cidade(conn,'Suzano')
        id_cidade2 = find_cidade(conn,'Suzano')

        insert_usuario(conn, 'Joao','Castro','jp@gmail.com','cpppppcc',id_cidade)
        insert_usuario(conn, 'Joao','Pieroni','jpc@gmail.com','jppccc',id_cidade)
        id = find_usuario(conn, 'Joao','Pieroni')

        # Tenta mudar nome para algum nome já existente.
        try:
            update_usuario(conn, id, 'Joao','Castro')
            self.fail('Não deveria ter mudado o nome.')
        except ValueError as e:
            pass
       
        # Tenta mudar nome para nome e email inexistente.
        update_usuario(conn, id, 'Rachel','Moraes')

        #Tenta mudar para um email existente
        try:
            update_usuario_email(conn, id, 'jp@gmail.com')
            self.fail('Não deveria ter mudado o email.')
        except ValueError as e:
            pass
        #Tenta mudar email para email inexistente
        update_usuario_email(conn, id, 'rm@gmail.com')

        #Tenta mudar cidade
        update_usuario_cidade(conn, id, id_cidade2)


    def test_lista_usuarios(self):
        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')

        # Verifica que ainda não tem usuarios no sistema.
        res = lista_usuarios(conn)
        self.assertFalse(res)

        # Adiciona algumas usuarios.
        usuarios_id = []
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppc',id_cidade)
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','jpppc',id_cidade)
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmm10',id_cidade)
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        # Verifica se os usuarios foram adicionadas corretamente.
        res = lista_usuarios(conn)
        self.assertCountEqual(res, usuarios_id)

        # Remove os usuarios.
        for u in usuarios_id:
            remove_usuario(conn, u)

        # Verifica que todos os usuarios foram removidas.
        res = lista_usuarios(conn)
        self.assertFalse(res)

##############################################################################################################################
#passaro
##############################################################################################################################

    def test_insert_passaro(self):
        conn = self.__class__.connection
    
        passaro = 'Flamingo'

        # Adiciona um passaro não existente.
        insert_passaro(conn, passaro)

        # Tenta adicionar o mesmo passaro duas vezes.
        try:
            insert_passaro(conn, passaro)
            self.fail('mesmo passaro adicionada duas vezes.')
        except ValueError as e:
            pass

        # Checa se o passaro existe.
        id = find_passaro(conn, passaro)
        self.assertIsNotNone(id)

        # Tenta achar um passaro inexistente.
        id = find_passaro(conn, 'bemtevi')
        self.assertIsNone(id)

    def test_remove_passaro(self):
        conn = self.__class__.connection
        insert_passaro(conn, 'Colibri')
        id = find_passaro(conn, 'Colibri')

        res = lista_passaros(conn)
        self.assertCountEqual(res, (id,))

        remove_passaro(conn, id)

        res = lista_passaros(conn)
        self.assertFalse(res)

    def test_muda_nome_passaro(self):
        conn = self.__class__.connection

        insert_passaro(conn, 'Pintassilgo')

        insert_passaro(conn, 'Rouxinol')
        id = find_passaro(conn, 'Rouxinol')

        # Tenta mudar nome para algum nome já existente.
        try:
            update_passaro(conn, id, 'Pintassilgo')
            self.fail('Nome ja existente.')
        except ValueError as e:
            pass

        # Tenta mudar nome para nome inexistente.
        update_passaro(conn, id, 'Grauna')

        # Verifica se mudou.
        id_novo = find_passaro(conn, 'Grauna')
        self.assertEqual(id, id_novo)

    def test_lista_passaros(self):
        conn = self.__class__.connection

        # Verifica que ainda não tem passaros no sistema.
        res = lista_passaros(conn)
        self.assertFalse(res)

        # Adiciona algumas passaros.
        passaros_id = []
        for p in ('Rouxinol', 'Grauna', 'Flamingo'):
            insert_passaro(conn, p)
            passaros_id.append(find_passaro(conn, p))

        # Verifica se as passaros foram adicionados corretamente.
        res = lista_passaros(conn)
        self.assertCountEqual(res, passaros_id)

        # Remove as passaros.
        for c in passaros_id:
            remove_passaro(conn, c)

        # Verifica se todos as passaros foram removidos.
        res = lista_passaros(conn)
        self.assertFalse(res)
################################################################################################################
#preferencia passaro
################################################################################################################
    def test_insert_preferencia(self):
        conn = self.__class__.connection
    

        # Cria alguns usuarios
        usuarios_id = []
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppccc',id_cidade)
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','jpjpjpj',id_cidade)
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmmmm',id_cidade)
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        #cria alguns passaros
        passaros_id = []
        for p in ('Rouxinol', 'Grauna', 'Flamingo'):
            insert_passaro(conn, p)
            passaros_id.append(find_passaro(conn, p))

        # adiciona preferencia de passaro.
        insert_preferencia_passaro(conn, usuarios_id[0], passaros_id[0])
        insert_preferencia_passaro(conn, usuarios_id[1], passaros_id[1])
        insert_preferencia_passaro(conn, usuarios_id[2], passaros_id[2])
        insert_preferencia_passaro(conn, usuarios_id[0], passaros_id[2])
        insert_preferencia_passaro(conn, usuarios_id[1], passaros_id[0])
        insert_preferencia_passaro(conn, usuarios_id[2], passaros_id[1])
    

        res = lista_preferencias_passaro(conn, usuarios_id[0])
        self.assertCountEqual(res, (passaros_id[0], passaros_id[2]))

        res = lista_preferencias_passaro(conn, usuarios_id[1])
        self.assertCountEqual(res, (passaros_id[1], passaros_id[0]))

        res = lista_preferencias_passaro(conn, usuarios_id[2])
        self.assertCountEqual(res, (passaros_id[2], passaros_id[1]))
        

 #######################################################################################################################################
 #post
 #######################################################################################################################################      
    def test_insert_post(self):
        conn = self.__class__.connection

        titulo = 'Novo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'



        # Adiciona post não existente.
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcca',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)


        # Checa se a post existe.
        id = find_post(conn, titulo)
        self.assertIsNotNone(id)

        # Tenta achar post inexistente.
        id = find_post(conn, 'post inexistente' )
        self.assertIsNone(id)

    def test_remove_post(self):
        titulo = 'Novo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'
        

        conn = self.__class__.connection
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcaa',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)

        res = lista_posts(conn)
        self.assertCountEqual(res, (id_post,))

        remove_post(conn, id_post)

        res = lista_posts(conn)
        self.assertFalse(res)

    def test_muda_post(self):
        titulo = 'Novo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcaaa',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)


       
        # Tenta mudar titulo do post.
        update_post_titulo(conn, id_post, 'novo titulo')

        #Tenta mudar texto do post
        update_post_texto(conn, id_post, 'novo texto')

        #Tenta mudar url foto
        update_post_url_foto(conn, id_post, 'novourl.com.br')

        #tenta mudar ativo
        update_post_ativo(conn, id_post, 0)


    def test_lista_posts(self):

        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        texto2 = 'Novo passaro encontrado'
        texto3 = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcaas',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')

        # Verifica que ainda não tem posts no sistema.
        res = lista_posts(conn)
        self.assertFalse(res)

        # Adiciona algumas posts.
        posts_id = []
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario, titulo2, texto2, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario, titulo3, texto3, url_foto)
        id_post = find_post(conn, titulo)
        posts_id.append(find_post(conn,titulo ))
        posts_id.append(find_post(conn,titulo2 ))
        posts_id.append(find_post(conn,titulo3 ))

        # Verifica se os posts foram adicionadas corretamente.
        res = lista_posts(conn)
        self.assertCountEqual(res, posts_id)

        # Remove os posts.
        for u in posts_id:
            remove_post(conn, u)

        # Verifica que todos os posts foram removidas.
        res = lista_posts(conn)
        self.assertFalse(res)

############################################################################################################################
#visualizou
############################################################################################################################
    def test_insert_visualizou(self):
        conn = self.__class__.connection

        aparelho = 'android'
        ip = '127.0.0.1'
        browser = 'chrome'
        titulo = 'Novo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'
        instante = datetime.now()
        instante = instante.strftime('%Y-%m-%d %H:%M:%S')



        # Adiciona visualizou não existente.
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcaaas',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)

        insert_visualizou(conn,id_post, id_usuario, aparelho, browser, ip, instante)


        # Checa se a visualizou existe.
        id = find_visualizou(conn, id_post)
        self.assertIsNotNone(id)

        # Tenta achar visualizou inexistente.
        id = find_visualizou(conn, 10 )
        self.assertIsNone(id)




    def test_lista_visualizadas(self):

        aparelho = 'android'
        ip = '127.0.0.1'
        browser = 'chrome'
        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'
        instante = datetime.now()
        instante = instante.strftime('%Y-%m-%d %H:%M:%S')

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','jppcaaassd',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post2 = find_post(conn, titulo)
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post3 = find_post(conn, titulo)

        # Verifica que ainda não tem visualizous no sistema.
        res = lista_visualizadas(conn)
        self.assertFalse(res)

        # Adiciona algumas visualizadas.
        visualizadas_id = []
        insert_visualizou(conn,id_post, id_usuario, aparelho, browser, ip, instante)
        id_visualizou = find_visualizou(conn, id_post)
        insert_visualizou(conn,id_post2, id_usuario, aparelho, browser, ip, instante)
        id_visualizou2 = find_visualizou(conn, id_post)
        insert_visualizou(conn,id_post3, id_usuario, aparelho, browser, ip, instante)
        id_visualizou3 = find_visualizou(conn, id_post)
        visualizadas_id.append(find_visualizou(conn,id_post ))
        visualizadas_id.append(find_visualizou(conn,id_post2 ))
        visualizadas_id.append(find_visualizou(conn,id_post3 ))


###############################################################################################################################
#menciona
#################################################################################################################################
    def test_insert_menciona(self):

        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        texto2 = 'Novo passaro encontrado'
        texto3 = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection
    

        # Cria alguns usuarios
        usuarios_id = []
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','joaopedro',id_cidade)
        id_usuario2 = find_usuario(conn,'Joao','Pieroni')
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmmmmms',id_cidade)
        id_usuario3 = find_usuario(conn,'Rachel','Moraes')
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        #cria alguns posts
        posts_id = []
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario2, titulo2, texto2, url_foto)
        id_post = find_post(conn, titulo2)
        insert_post(conn,id_usuario3, titulo3, texto3, url_foto)
        id_post = find_post(conn, titulo3)
        posts_id.append(find_post(conn,titulo ))
        posts_id.append(find_post(conn,titulo2 ))
        posts_id.append(find_post(conn,titulo3 ))

        # adiciona preferencia de passaro.
        insert_mencao(conn,posts_id[0], usuarios_id[0])
        insert_mencao(conn,posts_id[1], usuarios_id[1])
        insert_mencao(conn,posts_id[2], usuarios_id[2])
        insert_mencao(conn,posts_id[0], usuarios_id[1])
        insert_mencao(conn,posts_id[1], usuarios_id[2])
        insert_mencao(conn,posts_id[2], usuarios_id[0])
    

        res = lista_mencoes(conn, posts_id[0])
        self.assertCountEqual(res, (usuarios_id[0], usuarios_id[1]))

        res = lista_mencoes(conn, posts_id[1])
        self.assertCountEqual(res, (usuarios_id[1], usuarios_id[2]))

        res = lista_mencoes(conn, posts_id[2])
        self.assertCountEqual(res, (usuarios_id[2], usuarios_id[0]))
    def test_update_ativo(self):
        titulo = 'titulo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_mencao(conn,id_post, id_usuario)
        #tenta mudar ativo
        update_mencao_ativo(conn, id_post, id_usuario, 0)


###################################################################################################################################
#Referencia
####################################################################################################################################
    def test_insert_referencia(self):

        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        texto2 = 'Novo passaro encontrado'
        texto3 = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection
    

        # Cria alguns usuarios
        usuarios_id = []
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaoppc',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','jpppcccastr',id_cidade)
        id_usuario2 = find_usuario(conn,'Joao','Pieroni')
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmoraes',id_cidade)
        id_usuario3 = find_usuario(conn,'Rachel','Moraes')
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        # Cria alguns passaros
        passaros_id = []
        for p in ('Rouxinol', 'Grauna', 'Flamingo'):
            insert_passaro(conn, p)
            passaros_id.append(find_passaro(conn, p))

        #cria alguns posts
        posts_id = []
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario2, titulo2, texto2, url_foto)
        id_post = find_post(conn, titulo2)
        insert_post(conn,id_usuario3, titulo3, texto3, url_foto)
        id_post = find_post(conn, titulo3)
        posts_id.append(find_post(conn,titulo ))
        posts_id.append(find_post(conn,titulo2 ))
        posts_id.append(find_post(conn,titulo3 ))

        # adiciona preferencia de passaro.
        insert_referencia(conn,posts_id[0], passaros_id[0])
        insert_referencia(conn,posts_id[1], passaros_id[1])
        insert_referencia(conn,posts_id[2], passaros_id[2])
        insert_referencia(conn,posts_id[0], passaros_id[1])
        insert_referencia(conn,posts_id[1], passaros_id[2])
        insert_referencia(conn,posts_id[2], passaros_id[0])
    

        res = lista_referencia(conn, posts_id[0])
        self.assertCountEqual(res, (passaros_id[0], passaros_id[1]))

        res = lista_referencia(conn, posts_id[1])
        self.assertCountEqual(res, (passaros_id[1], passaros_id[2]))

        res = lista_referencia(conn, posts_id[2])
        self.assertCountEqual(res, (passaros_id[2], passaros_id[0]))

    def test_update_ativo_referencia(self):
        titulo = 'titulo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_passaro(conn, 'Flamingo')
        id_passaro = find_passaro(conn, 'Flamingo')
        insert_referencia(conn,id_post, id_passaro)
        #tenta mudar ativo
        update_referencia_ativo(conn, id_post, id_passaro, 0)

##########################################################################################################
#joinha
##########################################################################################################
    def test_insert_joinha(self):

        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        texto2 = 'Novo passaro encontrado'
        texto3 = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection
    

        # Cria alguns usuarios
        usuarios_id = []
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','joaopedro',id_cidade)
        id_usuario2 = find_usuario(conn,'Joao','Pieroni')
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmmmmms',id_cidade)
        id_usuario3 = find_usuario(conn,'Rachel','Moraes')
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        #cria alguns posts
        posts_id = []
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_post(conn,id_usuario2, titulo2, texto2, url_foto)
        id_post = find_post(conn, titulo2)
        insert_post(conn,id_usuario3, titulo3, texto3, url_foto)
        id_post = find_post(conn, titulo3)
        posts_id.append(find_post(conn,titulo ))
        posts_id.append(find_post(conn,titulo2 ))
        posts_id.append(find_post(conn,titulo3 ))

        # adiciona preferencia de passaro.
        insert_joinha(conn,posts_id[0], usuarios_id[0],1)
        insert_joinha(conn,posts_id[1], usuarios_id[1],1)
        insert_joinha(conn,posts_id[2], usuarios_id[2],0)
        insert_joinha(conn,posts_id[0], usuarios_id[1],0)
        insert_joinha(conn,posts_id[1], usuarios_id[2],1)
        insert_joinha(conn,posts_id[2], usuarios_id[0],0)
    

        res = lista_joinhas(conn, posts_id[0])
        self.assertCountEqual(res, (usuarios_id[0], usuarios_id[1]))

        res = lista_joinhas(conn, posts_id[1])
        self.assertCountEqual(res, (usuarios_id[1], usuarios_id[2]))

        res = lista_joinhas(conn, posts_id[2])
        self.assertCountEqual(res, (usuarios_id[2], usuarios_id[0]))
    def test_update_ativo_joinha(self):
        titulo = 'titulo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_joinha(conn,id_post, id_usuario,1)
        #tenta mudar ativo
        update_joinha_ativo(conn, id_post, id_usuario, 0)
    def test_update_reacao_joinha(self):
        titulo = 'titulo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_post(conn,id_usuario, titulo, texto, url_foto)
        id_post = find_post(conn, titulo)
        insert_joinha(conn,id_post, id_usuario,1)
        #tenta mudar ativo
        update_reacao_joinha(conn, id_post, id_usuario, 0)
##########################################################################################################
#segue
##########################################################################################################

    def test_insert_segue(self):

        titulo = 'titulo passaro'
        titulo2 = 'titulo passaro2'
        titulo3 = 'titulo passaro 3'
        texto = 'Novo passaro encontrado'
        texto2 = 'Novo passaro encontrado'
        texto3 = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection
    

        # Cria alguns usuarios
        usuarios_id = []
        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_usuario(conn,'Joao','Pieroni','jp@gmail.com','joaopedro',id_cidade)
        id_usuario2 = find_usuario(conn,'Joao','Pieroni')
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rmmmmms',id_cidade)
        id_usuario3 = find_usuario(conn,'Rachel','Moraes')
        usuarios_id.append(find_usuario(conn,'Joao','Castro' ))
        usuarios_id.append(find_usuario(conn,'Joao','Pieroni' ))
        usuarios_id.append(find_usuario(conn,'Rachel','Moraes' ))

        # adiciona preferencia de passaro.
        insert_segue(conn,usuarios_id[0], usuarios_id[1])
        insert_segue(conn,usuarios_id[0], usuarios_id[2])
        insert_segue(conn,usuarios_id[1], usuarios_id[0])
        insert_segue(conn,usuarios_id[1], usuarios_id[2])
        insert_segue(conn,usuarios_id[2], usuarios_id[1])
        insert_segue(conn,usuarios_id[2], usuarios_id[0])
    

        res = lista_seguidas(conn, usuarios_id[0])
        self.assertCountEqual(res, (usuarios_id[1], usuarios_id[2]))

        res = lista_seguidas(conn, usuarios_id[1])
        self.assertCountEqual(res, (usuarios_id[0], usuarios_id[2]))

        res = lista_seguidas(conn, usuarios_id[2])
        self.assertCountEqual(res, (usuarios_id[0], usuarios_id[1]))
    def test_update_ativo_segue(self):
        titulo = 'titulo passaro'
        texto = 'Novo passaro encontrado'
        url_foto = 'foto.com.br'

        conn = self.__class__.connection

        insert_cidade(conn,'Campinas')
        id_cidade = find_cidade(conn,'Campinas')
        insert_usuario(conn,'Joao','Castro','jc@gmail.com','joaopedrocastro',id_cidade)
        id_usuario = find_usuario(conn,'Joao','Castro')
        insert_usuario(conn,'Rachel','Moraes','rm@gmail.com','rachel100',id_cidade)
        id_usuario2 = find_usuario(conn,'Rachel','Moraes')
        insert_segue(conn,id_usuario2, id_usuario)
        #tenta mudar ativo
        update_segue_ativo(conn, id_usuario2, id_usuario, 0)

def run_sql_script(filename):
    global config
    with open(filename, 'rb') as f:
        subprocess.run(
            [
                config['MYSQL'], 
                '-u', config['USER'], 
                '-p' + config['PASS'], 
                '-h', config['HOST']
            ], 
            stdin=f
        )

def setUpModule():
    filenames = [entry for entry in os.listdir() 
        if os.path.isfile(entry) and re.match(r'.*_\d{3}\.sql', entry)]
    for filename in filenames:
        run_sql_script(filename)

def tearDownModule():
    run_sql_script('tear_down.sql')

if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)

