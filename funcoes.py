from pymysql import *
from GlobalVariable import GlobalVariable

def salvaScore(nome,score,fim):
    con = connect("localhost", "root", "", "Pynder")
    cur = con.cursor()
    sql = "INSERT INTO score(nome, score, fim ) VALUES (%s,%s,%s)"
    val = (nome, score, fim)
    cur.execute(sql,val)

