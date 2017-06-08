import MySQLdb
def connectDB(server,username,password,database):
    db = MySQLdb.connect(server,username,password,database )
    return db
n1 = "090096E07708"
def executeSQL(db,sql):
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def disconnectDB(db):
    db.close()





db = connectDB("127.0.0.1","root","1234","people")
executeSQL(db,"SELECT COUNT(rfid) FROM attendance where rfid ='"+n1+"';")
db.commit()
disconnectDB(db)
