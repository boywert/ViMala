import sqlite3
import sys
import numpy
import matplotlib
matplotlib.rcParams.update({'font.size': 6})
import matplotlib.pyplot as plt
f21cm  = 1420.4057517667
def main():
    print "Reading SQLite3 table"
    fig = plt.figure(figsize=(8, 6),dpi=240)
    ax = fig.add_subplot(111, polar=True)
    conn = sqlite3.connect('/share/data2/VIMALA/Lightcone/example.db')
    c = conn.cursor()
    
    
    
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 170 AND Flux >= 50 AND PosTheta > 0 AND PosTheta < 80.0*(3.142/180.0))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.1,marker=".",color="g",alpha=0.1)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 520 AND Flux >= 170 AND PosTheta > 0 AND PosTheta < 80.0*(3.142/180.0))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.2,marker=".",color="k",alpha=0.4)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 1700 AND Flux >=540 AND PosTheta > 0 AND PosTheta < 80.0*(3.142/180.0))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.4,marker=".",color="b")
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux >= 1700 AND PosTheta > 0 AND PosTheta < 80.0*(3.142/180.0))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.6,marker=".",color="r")
    
    ax.grid(True)
    ax.set_ylim(0.0,0.16)
    ax.set_rlabel_position(0)
    fig.savefig("lightcone.png")
    return 0
if __name__ == "__main__":
    main()
