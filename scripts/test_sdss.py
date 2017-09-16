import sqlite3
import sys
import numpy
import matplotlib
matplotlib.rcParams.update({'font.size': 6})
import matplotlib.pyplot as plt
f21cm  = 1420.4057517667
def main():
    print "Reading SQLite3 table"
    conn = sqlite3.connect('/share/data2/VIMALA/Lightcone/example.db')
    c = conn.cursor()
    sql = "SELECT PosTheta,Redshift FROM Lightcone WHERE (StellarMass > 1e8 AND PosPhi > 350.0*(3.142/180.0) AND PosPhi < 10.0*(3.142/180.0))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    print numpy.histogram(coor[:,0]/numpy.pi*180,bins=180)
    print numpy.histogram(coor[:,1],bins=18)
    #for a in coor:
    #    print a
    fig = plt.figure(figsize=(8, 6),dpi=240)
    ax = fig.add_subplot(111, polar=True)
    ax.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.1,marker=".")
    ax.grid(True)
    ax.set_ylim(0.0,0.16)
    ax.set_rlabel_position(0)
    fig.savefig("sdss.png")
    return 0
if __name__ == "__main__":
    main()
