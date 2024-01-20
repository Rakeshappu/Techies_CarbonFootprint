import MySQLdb

def connection():
    conn = MySQLdb.connect("localhost","root","2628","flask")
    c = conn.cursor()
    return c,conn