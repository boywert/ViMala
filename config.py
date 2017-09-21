import numpy

gadget2msun=1.e10
boxsize = 480.279
hubble_h = 0.683
OmegaM = 0.315

db_struct = numpy.dtype([
    ('PosX'                      , numpy.float32),
    ('PosY'                      , numpy.float32),
    ('PosZ'                      , numpy.float32),
    ('PosR'                      , numpy.float32),
    ('PosTheta'                  , numpy.float32),
    ('PosPhi'                    , numpy.float32),
    ('VelX'                      , numpy.float32),
    ('VelY'                      , numpy.float32),
    ('VelZ'                      , numpy.float32),
    ('VelR'                      , numpy.float32),
    ('VelTheta'                  , numpy.float32),
    ('VelPhi'                    , numpy.float32),
    ('StellarMass'               , numpy.float32),
    ('ColdGas'                   , numpy.float32),
    ('Healpix'                   , numpy.int32),
    ('LuminosityDistance'        , numpy.float32),
    ('Redshift'                  , numpy.float32),
    ('NeutralH'                  , numpy.float32),
    ('DeltaFrequency'            , numpy.float32),
    ('FluxDensity'               , numpy.float32),
    ('Flux'                 , numpy.float32)
])

firstfile = 0
lastfile = 511
zlistfile = "/scratch/01937/cs390/data/snap_z2.txt"
z3listfile = "/scratch/01937/cs390/data/snap_z3.txt"
config = {}
tau_e = 0.067
delta_tau_e = 0.016
model_names = ["sage_w1","lgal_w1","lgal_planck"]

model_labels = ["SAGE (WMAP-1)", "L-Galaxies (WMAP-1)", "L-Galaxies (Planck-1)" ]

model_paths = ["/lustre/HI_FAST/SAM_test/MR/SAGE_output","/lustre/HI_FAST/SAM_test/MR/LGAL_output_W1","/lustre/HI_FAST/SAM_test/MR/LGAL_output_W1_PLANCK1"]
struct_file = []
for p in model_paths:
    struct_file.append(p+"/inputs/LGalaxyStruct.py")
struct_file[0] = "/lustre/HI_FAST/SAM_test/LGAL-tools/HI_FAST/sage_struct.py"
struct_file[1] = "/lustre/HI_FAST/SAM_code/LGAL/AuxCode/awk/LGalaxyStruct.py"
struct_file[2] = "/lustre/HI_FAST/SAM_code/LGAL/AuxCode/awk/LGalaxyStruct.py"
model_plot_colors = ['#1b9e77','#d95f02','#7570b3']
model_plot_patterns = ['-','-','-']
model_xfrac_path = ["/scratch/01937/cs390/data/CSFR/no_reionization/wmap7/SEMNUM/3410.00/",
        "/scratch/01937/cs390/data/CSFR/okamoto/wmap7/SEMNUM/3410.00/",
        "/scratch/01937/cs390/Hybrid/xfrac/3410.01/",
            "/scratch/01937/cs390/data/CSFR/no_reionization_infall/wmap7_test/SEMNUM/3410.00/",
            "/scratch/01937/cs390/data/CSFR/okamoto_infall/wmap7_test/SEMNUM/3410.00/",
            "/scratch/01937/cs390/Hybrid/xfrac/3410.03/"]
model_fesc = [3410,3410,3410,3410,3410,3410]
use_model = [False,False,True]
xfrac_doubleflag = [0,0,0,0,0,0]
