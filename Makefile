FC=ifort
LIB= /share/apps/intel/composer_xe_2013_sp1.3.174/mkl/include
INC= -L/share/apps/intel/composer_xe_2013_sp1.3.174/mkl/lib/intel

all: libsphere create_dbstruct

create_dbstruct:
	cd scripts
	python create_dbstruct.py
	cd ..
libsphere: 
	$(FC) lib/sphere.f90 -o lib/libsphere.so -O3 -shared -fPIC -openmp -static -mkl -L$(LIB) -I$(INC)

clean:
	rm -f scripts/*.pyc
	rm -f lib/*.so
