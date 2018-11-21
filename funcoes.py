from pymysql import *
import GlobalVariable

def salvaScore():
    con = connect("localhost", "root", "", "Pynder")
    cur = con.cursor()
    sql = "INSERT INTO `score`(`nome`, `score`) VALUES (%s,%s)"
    val = (GlobalVariable.getNome(), GlobalVariable.getScore())
    cur.execute(sql,val)

