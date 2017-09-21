import mysql.connector
import sys
sys.path.append("../")
sys.path.append("../lib/")
sys.path.append("../python/")
from config import *

def main():
    cnx = mysql.connector.connect(host="192.168.2.48",user='ViMala',password="ViMala@Sql", database='ViMala')
    sql = "DROP TABLE ` DBSTRUCT`"
    cur.execute(sql)
    cnx.commit()
    sql = "CREATE TABLE `ViMala`.`DBSTRUCT` ( `ID` INT NOT NULL , `FIELD` TEXT NOT NULL , `DESCRIPTION` TEXT NOT NULL , `TYPE` TEXT NOT NULL ) ENGINE = InnoDB;"
    cur = cnx.cursor()
    cur.execute(sql)
    cnx.commit()
    i = 0
    for field in db_struct.names:
        add_field = ("INSERT INTO `ViMala`.`DBSTRUCT` (ID, FIELD, DESCRIPTION, TYPE) VALUES ("+str(i)+",%s , %s, %s)") 
        field_data = (str(field),"Description",str(db_struct[field]))
        cur.execute(add_field,field_data)
        i += 1
    cnx.commit()
    cnx.close()
    return 0

if __name__ == "__main__":
    main()
