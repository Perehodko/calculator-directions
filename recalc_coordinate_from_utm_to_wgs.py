from pyproj import Proj
import numpy as np
from pandas import DataFrame
import numpy

core = (-44.6360, -23.2278)

print('\nSampling site lon %s, lat %s\n' % (core[0], core[1]))

x = (529025.00, 529114.00, 545227.00, 545582.00)
y = (7422210.00, 7422343.00, 7435702.00, 7435741.00)

df = DataFrame(numpy.c_[x, y], columns=['Meters East', 'Meters South'])
df

myProj = Proj("+proj=utm +zone=23K, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
lon, lat = myProj(df['Meters East'].values, df['Meters South'].values, inverse=True)

print(lon, lat)

UTMx, UTMy = myProj(lon, lat)
DataFrame(np.c_[UTMx, UTMy, lon, lat], columns=['UTMx', 'UTMy', 'Lon', 'Lat'])
print(UTMx, UTMy)
