import MySQLdb
import serial
n1 = "090096E07708"
n2 = "090096E8E691"


dat = serial.Serial("COM6",9600)

def connectDB(server,username,password,database):
    db = MySQLdb.connect(server,username,password,database )
    return db

def executeSQL(db,sql):
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def disconnectDB(db):
    db.close()

def dbFunc(rfid):
    db = connectDB("127.0.0.1","root","1234","people")
    if (rfid==n1):
         executeSQL(db,"insert into attendance values ('"+rfid+"','anand',1,curdate(),curtime(),0)")
         print executeSQL(db,"SELECT COUNT(rfid) FROM attendance where rfid ='"+n1+"';")
    elif (rfid==n2):
            executeSQL(db,"insert into attendance values ('"+rfid+"','mridul',1,curdate(),curtime(),0)")
            print executeSQL(db,"SELECT COUNT(rfid) FROM attendance where rfid ='"+n2+"';")
            
    executeSQL(db,"SELECT COUNT(rfid) FROM attendance where rfid ='"+n1+"';")       
    db.commit()
    disconnectDB(db)



while(1==1):
    inp = (dat.readline().strip())
    if inp != "" :
        dbFunc(inp)
    print (inp.decode("utf-8"))
    
