import mysql.connector
cnx = mysql.connector.connect(host="192.168.2.48",user='ViMala',password="ViMala@Sql", database='ViMala')

sql = "CREATE TABLE IF NOT EXISTS `ViMala`.`DBSTRUCT` ( `ID` INT NOT NULL , `FIELD` TEXT NOT NULL , `DESCRIPTION` TEXT NOT NULL , `TYPE` TEXT NOT NULL ) ENGINE = InnoDB;"
cur = cnx.cursor()
cur.execute(sql)
cnx.commit()
add_field = ("INSERT INTO `ViMala`.`DBSTRUCT` (ID, FIELD, DESCRIPTION, TYPE) VALUES (1, %s, %s, %s)") 
field_data = ("StellarMass","Stellar Mass in 1e10 Msun","<f4")
cur.execute(add_field,field_data)
cnx.commit()
cnx.close()
