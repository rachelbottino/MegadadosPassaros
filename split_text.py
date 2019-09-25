import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="rachelpbm",
  passwd="adgjlra1",
  database="passaros",
  charset="utf8mb4"
)
#filtrando posts com menções '@'
mycursor = mydb.cursor()
mycursor.execute("SELECT id_post, texto FROM POST WHERE texto like '%@%'")
mencoes = mycursor.fetchall()
print("Posts com @:")
#print(mencoes)

for post in mencoes:
	palavras = post[1].split(' ')
	#print(palavras)
	for palavra in palavras:
		if palavra.startswith('@'):
			palavra = str((palavra.split('@'))[1])
			id_post = post[0]
			#verifica se existe o nome de usuário marcado no post
			try:
				mycursor = mydb.cursor()
				sql = "SELECT id_usuario FROM usuario WHERE username = %s"
				uname = (palavra, )
				mycursor.execute(sql, uname)
				id_usuario = (mycursor.fetchone())[0]
				print("Username válido",id_post, id_usuario)

				try:
					sql = "INSERT INTO menciona (id_post, id_usuario) VALUES (%s, %s)"
					i = (int(id_post), int(id_usuario))
					mycursor.execute(sql, i)
					mydb.commit()
					print(mycursor.rowcount, "record inserted.")
				except:
					print("Falha na inserção")

			except:
				print("Username inválido")

#filtrando posts com referencias '#'
mycursor = mydb.cursor()
mycursor.execute("SELECT id_post, texto FROM POST WHERE texto like '%#%'")
referencias = mycursor.fetchall()
print("Posts com #:")
print(referencias)

for post in referencias:
	palavras = post[1].split(' ')
	print(palavras)
	for palavra in palavras:
		if palavra.startswith('#'):
			palavra = str((palavra.split('#'))[1])
			id_post = post[0]
			#verifica se existe o nome de usuário marcado no post
			try:
				mycursor = mydb.cursor()
				sql = "SELECT id_passaro FROM passaro WHERE especie = %s"
				esp = (palavra, )
				mycursor.execute(sql, esp)
				id_passaro = (mycursor.fetchone())[0]
				print("Especie válida",id_post, id_passaro)

				try:
					sql = "INSERT INTO referencia (id_post, id_passaro) VALUES (%s, %s)"
					i = (int(id_post), int(id_passaro))
					mycursor.execute(sql, i)
					mydb.commit()
					print(mycursor.rowcount, "record inserted.")
				except:
					print("Falha na inserção")

			except:
				print("Especie inválida")