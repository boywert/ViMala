import sqlite3
import sys
def main():
    job_id = sys.argv[1]
    sql = sys.argv[2]
    print "Reading SQLite3 table"
    conn = sqlite3.connect('/share/data2/VIMALA/Lightcone/example.db')
    c = conn.cursor()
    cursor = c.execute(sql)
    for row in cursor:
        print row[0],row[1]
    return 0

if __name__ == "__main__":
    main()
