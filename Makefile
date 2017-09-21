FC=ifort
LIB= /share/apps/intel/composer_xe_2013_sp1.3.174/mkl/include
INC= -L/share/apps/intel/composer_xe_2013_sp1.3.174/mkl/lib/intel

libsphere: 
	$(FC) lib/shere.f90 -o lib/sphere.so -O3 -shared -fPIC -openmp -static -mkl -L$(LIB) -I$(INC)
