from pymysql import *

##banco: Pynder
##tabela: score
##campos: id,nome,score

con = connect("localhost", "root", "", "Pynder")

cur = con.cursor()

sql= "CREATE TABLE score (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(225), score INT, fim VARCHAR(1))"
cur.execute(sql)

con.commit()
con.close()