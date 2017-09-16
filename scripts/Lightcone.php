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
    fig = plt.figure(figsize=(16, 8),dpi=240)

    ax1 = fig.add_subplot(121, polar=True)
    
    angle = 20.0
    
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 170 AND Flux >= 50 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.1,marker=".",color="g",alpha=0.1)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 520 AND Flux >= 170 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.2,marker=".",color="k",alpha=0.4)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 1700 AND Flux >=540 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.4,marker=".",color="b",alpha=0.7)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux >= 1700 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.6,marker=".",color="r")
    
    ax1.grid(True)
    ax1.set_ylim(0.0,0.16)
    ax1.set_rlabel_position(0)

    
    ax2 = fig.add_subplot(122, polar=True)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 1.70e-4 AND FluxDensity >= 5.0e-5 AND PosTheta > 0 AND PosTheta < angle*(3.142/1angle))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.1,marker=".",color="g",alpha=0.1)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 5.2e-4 AND FluxDensity >= 1.70e-4 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.2,marker=".",color="k",alpha=0.4)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 1.7e-3 AND FluxDensity >=5.40e-4 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.4,marker=".",color="b",alpha=0.7)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity >= 1.7e-3 AND PosTheta > 0 AND PosTheta < angle*(3.142/180))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,1]/numpy.pi*180,coor[:,0],s=0.6,marker=".",color="r")
    
    ax2.grid(True)
    ax2.set_ylim(0.0,0.16)
    ax2.set_rlabel_position(0)

    
    fig.savefig("lightcone.png")
    return 0
if __name__ == "__main__":
    main()
