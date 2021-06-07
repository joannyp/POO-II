import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost', db='pooii', user='root', passwd='duplapooii')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios_senha (id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, senha VARCHAR(32) NOT NULL, email text NOT NULL);"""


nome = 'joanny'
senha = 'duplapooii'
email = 'joannypacheco@hotmail.com'

cursor.execute(sql)
#for i in range(5):
cursor.execute('INSERT INTO usuarios_senha (nome, senha, email) VALUES (%s,MD5(%s),%s)', (nome, senha, email))

#cursor.execute('SELECT * from usuarios_senha')
cursor.execute('SELECT * FROM usuarios_senha WHERE nome= %s AND senha=MD5(%s)', (nome, senha))

for c in range:
    print(c)

conexao.commit()
conexao.close()


