import numpy

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

for x in db_struct:
    print x
