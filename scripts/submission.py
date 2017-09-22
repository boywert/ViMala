import sqlite3
import sys
import numpy
import matplotlib
import mysql.connector
matplotlib.rcParams.update({'font.size': 6})
import matplotlib.pyplot as plt
f21cm  = 1420.4057517667
def main():
    print sys.argv
    job_id = sys.argv[1]
    cnx = mysql.connector.connect(host="192.168.2.48",user='ViMala',password="ViMala@Sql", database='ViMala')
    cur = cnx.cursor()
    sql  = "SELECT PARAMS,CONDITIONS FROM JobSubmission WHERE ID = "+str(job_id)+" LIMIT 1"
    cur.execute(sql)
    for row in cur:
        field_data = row[0].split("|")
        field_data.remove("")
        field_data.remove("condition")
        sql = 'SELECT '+','.join(field_data)
        if row[1] != "":
            sql = sql + " WHERE " + row[1]
    print sql
    return 0
    sql = sql + " LIMIT 10"
    print "Reading SQLite3 table"
    conn = sqlite3.connect('/share/data2/VIMALA/Lightcone/example.db')
    c = conn.cursor()
    cursor = c.execute(sql)
    result = cursor.fetchall()
    f = open("/share/data2/VIMALA_output/"+job_id+".txt", "w+")
    for x in result:
        print >> f, x
   
    sql = "UPDATE JobSubmission SET STATUS = 2 WHERE ID = "+job_id
    cur.execute(sql)
    cnx.commit()
    return 0
if __name__ == "__main__":
    main()
