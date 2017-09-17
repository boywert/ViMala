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
    
    
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 170 AND Flux >= 50 AND (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,0],coor[:,1],s=0.01,marker=".",color="g",alpha=0.1)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 520 AND Flux >= 170 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,0],coor[:,1],s=0.02,marker=".",color="k",alpha=0.4)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux < 1700 AND Flux >=540 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,0],coor[:,1],s=0.04,marker=".",color="b",alpha=0.7)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (Flux >= 1700 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax1.scatter(coor[:,0],coor[:,1],s=0.1,marker=".",color="r")
    
    ax1.grid(True)
    ax1.set_ylim(0.0,0.16)
    ax1.set_rlabel_position(0)

    
    ax2 = fig.add_subplot(122, polar=True)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 1.70e-4 AND FluxDensity >= 5.0e-5 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,0],coor[:,1],s=0.01,marker=".",color="g",alpha=0.1)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 5.2e-4 AND FluxDensity >= 1.70e-4 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,0],coor[:,1],s=0.02,marker=".",color="k",alpha=0.4)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity < 1.7e-3 AND FluxDensity >=5.40e-4 AND (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,0],coor[:,1],s=0.04,marker=".",color="b",alpha=0.7)
    sql = "SELECT PosPhi,Redshift FROM Lightcone WHERE (FluxDensity >= 1.7e-3 AND  (PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    coor = numpy.array(result)
    print len(coor)
    ax2.scatter(coor[:,0],coor[:,1],s=0.1,marker=".",color="r")
    
    ax2.grid(True)
    ax2.set_ylim(0.0,0.16)
    ax2.set_rlabel_position(0)

    
    fig.savefig("lightcone.png")
    plt.close(fig)

    ax1 = fig.add_subplot(111)
    sql = "SELECT DeltaFrequency FROM Lightcone WHERE ((PosTheta > 70.0*(3.142/180.0) AND PosTheta < 80.0*(3.142/180.0)))"
    cursor = c.execute(sql)
    result = cursor.fetchall()
    result = numpy.log10(numpy.array(result))
    hist = numpy.histogram(result,bins=20)
    y = hist[0]
    x = numpy.zeros_like(y,dtype=numpy.float32)
    for i in range(len(hist[0])):
        x[i] = 0.5*(hist[1][i]+hist[1][i+1])
    print x,y
    ax1.plot(x,y,"-")
    ax1.set_yscale("log")
    ax1.set_xlabel(r"$\log_{10} (\Delta \nu/Hz)$")
    ax1.set_ylabel(r"$\log_{10} N$")
    fig.savefig("DeltaF.pdf")
    plt.close(fig)
    return 0
if __name__ == "__main__":
    main()
