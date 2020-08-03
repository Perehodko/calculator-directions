from pyproj import Transformer

transformer = Transformer.from_crs("epsg:4326", "epsg:32639" )
a = transformer.transform(63.216666667, 52.9)
print(a)
