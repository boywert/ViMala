import sys
sys.path.append("../")
sys.path.append("../lib/")
sys.path.append("../python/")
from config import *
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=hubble_h*100.0, Om0=OmegaM)

from math import *

import numpy
import os
os.system("cp dummy_dtype.py LGalaxyStruct.py")
import LGalaxyStruct
import add_observations

import read_lgal_advance as read_lgal
import timeit
from numpy.ctypeslib import ndpointer
from ctypes import CDLL, POINTER, c_int, c_float, c_double
#import test as mymodule
mymodule = CDLL('../lib/libsphere.so')
_twodimp = ndpointer(dtype=c_float,ndim=2)
_onedimp = ndpointer(dtype=c_float,ndim=1)
arg2 = ndpointer(ndim=2)
arg3 = ndpointer(shape=(10,10))
mymodule.make_sphere.argtypes = [c_int, c_float, _twodimp, _twodimp, _twodimp, _twodimp]
import healpy
from timeit import default_timer as timer

def loadfilter(structfile):
    from random import randint
    ranki = str(randint(0,1024))
    rankj = str(randint(0,1024))
    os.system("mkdir -p ../tmp/"+ranki+"/"+rankj)
    sys.path.insert(0,"../tmp/"+ranki+"/"+rankj)
    os.system("cp "+structfile+" ../tmp/"+ranki+"/"+rankj+"/LGalaxyStruct.py")
    os.system("rm -f ../tmp/"+ranki+"/"+rankj+"/LGalaxyStruct.pyc")
    reload(LGalaxyStruct)
    filter = LGalaxyStruct.properties_used
    for fi in filter:
        fi = False    
    filter['Pos'] = True
    filter['Vel'] = True
    filter['StellarMass'] = True
    filter['ColdGas'] = True
    filter['Mvir'] = True
    filter['Vvir'] = True
    filter['FileUniqueGalID'] = True
    dt = LGalaxyStruct.struct_dtype
    return (filter,dt)

dt = []
filter = []
for i in range(len(struct_file)):
    (f,t) = loadfilter(struct_file[i])
    filter.append(f)
    dt.append(t)

#filter model
filter_tmp = []
dt_tmp = []
model_names_tmp = []
struct_file_tmp = []
model_labels_tmp = []
model_paths_tmp = []
for i in range(len(use_model)):
    if use_model[i]:
        filter_tmp.append(filter[i])
        dt_tmp.append(dt[i])
        model_names_tmp.append(model_names[i])
        struct_file_tmp.append(struct_file[i])
        model_labels_tmp.append(model_labels[i])
        model_paths_tmp.append(model_paths[i])

filter = filter_tmp
dt = dt_tmp
model_names = model_names_tmp
struct_file = struct_file_tmp
model_labels = model_labels_tmp
model_paths = model_paths_tmp       




#zlist = open(zlistfile,"r").readlines()

NSIDE = 2048
f21cm  = 1420.4057517667 #MHz
def readgal(z,i_model,i_file):
        i = i_model
        index = model_names[i]
        if index[:4] == "lgal":
            zz = "%10.2f"%(z)
        elif index[:4] == "sage":
            zz = "%10.3f"%(z)
        file_prefix = "model_z"+zz.strip()
        (nTrees,nGals,nTreeGals,gal) = read_lgal.readsnap_lgal_advance(model_paths[i],file_prefix,i_file,i_file,filter[i],dt[i],1)
        pos = numpy.ascontiguousarray(gal['Pos'])
        vel = numpy.ascontiguousarray(gal['Vel'])
        pos_sphere = numpy.empty((nGals*8,3),dtype=numpy.float32)
        vel_R = numpy.empty((nGals*8,3),dtype=numpy.float32)
        mymodule.make_sphere(c_int(nGals),c_float(boxsize),pos,vel,pos_sphere,vel_R)
        return nGals,gal,pos_sphere,vel_R
def nu_from_a(a): #MHz
    return a*f21cm
def a_from_nu(f):
    return f/f21cm
def nu_from_z(z):
    return f21cm/(1.+z)
def z_from_nu(f):
    return f21cm/f - 1.0
def t_from_a(a):
    return cosmo.age(1./a - 1.0)
def t_from_z(z):
    return cosmo.age(z)
def a_from_z(z):
    return 1./(z+1.)
def z_from_a(a):
    return 1./a - 1.0

alist_file =  "/lustre/HI_FAST/SAM_code/LGAL/input/zlists/zlist_planck_MR.txt"

hubble_h=0.683

def gen_lightcone(dataset,dataname,file):
    
    first_z = 0.0
    last_z = z_from_nu(1220.0)
    f_step = 0.5 #MHz
    print "a", a_from_z(first_z), a_from_z(last_z)
    print "f", nu_from_z(first_z), nu_from_z(last_z)
    print "t", t_from_z(first_z), t_from_z(last_z)
    print "d", cosmo.comoving_distance(first_z)*hubble_h,cosmo.comoving_distance(last_z)*hubble_h
    #construct table for lookup f-d
    f_array = numpy.arange(nu_from_z(first_z),nu_from_z(last_z)-f_step,-0.1)
    d_array = numpy.empty(len(f_array),dtype=numpy.float32)
    d_array[:] = cosmo.comoving_distance(z_from_nu(f_array[:])).value*hubble_h
    print f_array
    print d_array

    
    alist = numpy.loadtxt(alist_file)
    alist = alist[(alist >= a_from_z(last_z)) & (alist <= a_from_z(first_z))]
    alist.sort()
    alist = alist[::-1]
    print alist,a_from_z(last_z),a_from_z(first_z)

    fc_list = numpy.arange(nu_from_z(first_z),nu_from_z(last_z)-f_step,-1*f_step)
    fb_list = numpy.empty(len(fc_list)-1,dtype = numpy.float32)
    for i in range(len(fc_list)-1):
        fb_list[i] = 0.5*(fc_list[i]+fc_list[i+1])
    ngals = []
    gals = []
    start_r = 0.0
    totalNgals = []
    for i in range(len(alist)):
        z = "%10.3f" % (z_from_a(alist[i]))
        if i < len(alist)-1:
            alist_distance = cosmo.comoving_distance(z_from_a(alist[i+1])).value*hubble_h
        else:
            alist_distance = cosmo.comoving_distance(last_z).value*hubble_h
        ngal_i,gal_i,pos_i,vR_i = readgal(float(z),dataset,file)
        #ngals.append(ngal_i)
        #pos.append(pos_i)
        #vR.append(vR_i)
        fullgal = numpy.empty(ngal_i*8,dtype = gal_i.dtype)
        if "FileUniqueGalID" in gal_i.dtype.names:
            for j in range(8):
                fullgal[ngal_i*j:ngal_i*(j+1)] = gal_i
                fullgal[ngal_i*j:ngal_i*(j+1)]['FileUniqueGalID'] += ngal_i*j

        else:
            for j in range(8):
                fullgal[ngal_i*j:ngal_i*(j+1)] = gal_i      

        del(gal_i)
        gallist = numpy.where((pos_i[:,0] >= start_r) & (pos_i[:,0] <= alist_distance))[0]
        print "z = ",z,"a=",alist[i],"r = ",start_r,"-",alist_distance
        #store data
        ogal = numpy.empty(len(gallist),dtype=db_struct)
        if (len(gallist) > 0):
            ogal['PosX'] = fullgal['Pos'][gallist,0]/hubble_h
            ogal['PosY'] = fullgal['Pos'][gallist,1]/hubble_h
            ogal['PosZ'] = fullgal['Pos'][gallist,2]/hubble_h
            ogal['VelX'] = fullgal['Vel'][gallist,0]
            ogal['VelY'] = fullgal['Vel'][gallist,1]
            ogal['VelZ'] = fullgal['Vel'][gallist,2]
            ogal['StellarMass'] = fullgal['StellarMass'][gallist]*1e10/hubble_h
            ogal['ColdGas'] = fullgal['ColdGas'][gallist]*1e10/hubble_h
            coldtostellar =  ogal['ColdGas']/ogal['StellarMass']
            ogal['PosR'] = pos_i[gallist,0]
            ogal['PosTheta'] = pos_i[gallist,1]
            ogal['PosPhi'] = pos_i[gallist,2]
            ogal['Healpix'] = healpy.pixelfunc.ang2pix(NSIDE, ogal['PosTheta'], ogal['PosPhi'])
            ogal['VelR'] = vR_i[gallist,0]
            ogal['VelTheta'] = vR_i[gallist,1]
            ogal['VelPhi'] = vR_i[gallist,2]
            ogal['Frequency'] = numpy.interp(ogal['PosR'],d_array,f_array)
            ogal['Redshift'] = z_from_nu(ogal['Frequency'][:])
            ogal['DeltaFrequency'] = 1000.0*fullgal['Vvir'][gallist]/3e8*f21cm*1e6
            ogal['PosR'] = pos_i[gallist,0]/hubble_h
            ogal['LuminosityDistance'] = ogal['PosR']*(z_from_nu(ogal['Frequency'][:])+1)
            ogal['NeutralH'] = ogal['ColdGas']*0.41/(numpy.power(coldtostellar,-0.52)+numpy.power(coldtostellar,0.56))
            ogal['Flux'] = ogal['NeutralH']/49.8*numpy.power(ogal['LuminosityDistance'],-2)
            ogal['FluxDensity'] = ogal['Flux']/ogal['DeltaFrequency']
        gals.append(ogal)
        start_r = alist_distance
        totalNgals.append(len(gallist))
    totalNgals = numpy.array(totalNgals)
    db_gal = numpy.empty(numpy.sum(totalNgals),dtype=db_struct)
    first_gal = 0
    for i in range(len(gals)):
        db_gal[first_gal:first_gal+totalNgals[i]] = gals[i]
        first_gal += totalNgals[i]
    numpy.save('model_%s_%d.npy'%(dataname,file),db_gal)
    sys.stdout.flush()
    return


    # i = len(alist)-1
    # z = "%10.3f" % (z_from_a(alist[i]))
    
    # ngal_i,gal_i,pos_i,vR_i = readgal(float(z))
    # gallist = numpy.where((pos_i[:,0] >= start_r) & (pos_i[:,0] <= alist_distance))[0]
    # print "z = ",z,"a=",alist[i],"r = ",start_r,"-",alist_distance
    # start_r = alist_distance
    
                        
    # return


    # Rb_list = numpy.empty(len(fb_list),dtype = numpy.float32)
    # Rb_list[:] = cosmo.comoving_distance(z_from_nu(fb_list[:])).value*0.73

    # for i in range(len(Rb_list)-1):
    #     r_check = len(alist_distance)-1
    #     toggle = 0
    #     while (toggle==0) & (r_check >= 0):
    #         if alist_distance[r_check] > Rb_list[i]:
    #             toggle = 1
    #             break
    #         r_check -= 1
    #     gallist = numpy.where((pos[r_check][:,0] >= Rb_list[i]) & (pos[r_check][:,0] <= Rb_list[i+1]))[0]
    #     print len(gallist)

    # #track gals backward
    # for igal in gal[len(gal)-1]:
    #     id = igal['FileUniqueGalID']
    #     isnap = len(gal)-2
    #     while (id > -1) & (isnap > -1):
    #         listgal = gal[isnap][gal[isnap]['FileUniqueGalID'] == id]
    #         if len(listgal) == 0:
    #             id = -1
    #         isnap -= 1
def main():
     file = int(sys.argv[1])
     for i in range(len(model_names)):
         gen_lightcone(i,model_names[i],file)
if __name__ == "__main__":
    main()
