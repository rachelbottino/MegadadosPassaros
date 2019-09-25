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
print(mencoes)

for post in mencoes:
	palavras = post[1].split(' ')
	print(palavras)
	for palavra in palavras:
		if palavra.startswith('@'):
			print(post[0], palavra)  
