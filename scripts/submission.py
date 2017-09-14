import sqlite3
import sys
import numpy 
import matplotlib.pyplot as plt
f21cm  = 1420.4057517667
def main():
    job_id = sys.argv[1]
    sql = sys.argv[2]
    print "Reading SQLite3 table"
    conn = sqlite3.connect('/share/data2/VIMALA/Lightcone/example.db')
    c = conn.cursor()
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    fig = plt.figure(figsize=(8, 6),dpi=240)
    ax = fig.add_subplot(111, polar=True)
    ax.scatter(coor[:,1]/numpy.pi*180,f21cm/coor[:,0]-1,s=0.1,marker=".")
    ax.grid(True)
    ax.set_ylim(0.0,0.16)
    ax.set_rlabel_position(0)
    fig.savefig("lightcone.png")
    return 0
if __name__ == "__main__":
    main()
