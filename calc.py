import csv
import math
from pyproj import Transformer

dict_BL = {}

def read(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    for i, line in enumerate(reader):
        B = line["B"]
        L = line["L"]
        magn_dec = line["magn_dec"]
        zone = line["zone"]

        dict_BL[i] = {"B": line["B"], "L": line["L"], "zone": line["zone"], "H": line["H"], "year": line["year"], "magn_dec": line["magn_dec"], "hight": ["H"]}
        # print(dict_BL)

def convert(value):
    pos_angl = value.find("ᵒ")
    angler = value[:pos_angl]
    # pos minute
    pos_minute = value.find("'")
    minute = value[pos_angl + 1:pos_minute]
    # only degree
    degree = float(angler) + float(minute) / 60
    # print("degree", degree)
    return (degree)

def zone(L_r):
    zone_r = int((L_r / 6) + 1)
    return zone_r

def zero_l(zone_r):
    L0 = 6 * zone_r - 3
    return L0

def gamma(B, L, L0):
    radians_B = math.radians(B)
    res_gamma = (L - L0)*math.sin(radians_B)
    # if res_gamma > 0:
    #     res_gamma += 0.01
    # else:
    #     res_gamma -= 0.01
    # return (round(res_gamma, 2))
    return res_gamma


def bussol(magn_dec, gamma):
    corr_bussol = float(magn_dec) - gamma
    return corr_bussol

def convert_coord(line_z, B, L):
    zone_dict = {"39": "epsg:32639", "31": "epsg:32631", "51": "epsg:32651", "52": "epsg:32652", "42": "epsg:32642",
                 "53": "epsg:32653"}
    if line_z in zone_dict:
        # print(zone_dict[line_z])
        epsg = zone_dict[line_z]

    transformer = Transformer.from_crs("epsg:4326", epsg)
    b = transformer.transform(B, L)
    return b
    # print(b)

def my_print():
    print("B:", i[1]["B"], "L:", i[1]["L"])
    print("X:", round(res_flat_coord[0]), "Y:", round(res_flat_coord[1]))
    print("H:", i[1]["H"], "м")
    print("Год:", i[1]["year"])
    print("Магнитное склонение:", i[1]["magn_dec"])
    print("Сближение меридианов:", round(g, 3))
    print("Поправка для буссоли", round(buss, 3))
    # print("zone",zone_r)
    print("\n")

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        read(f_obj)
    for i in dict_BL.items():
        # print(i[1]["B"])
        B_r = convert(i[1]["B"])
        L_r = convert(i[1]["L"])
        zone_r = zone(L_r)
        g = gamma(B_r, L_r, zero_l(zone_r))
        buss = bussol(i[1]["magn_dec"], g)
        res_flat_coord = convert_coord(i[1]["zone"], B_r, L_r)
        my_print()
