import csv
import math

dict_BL = {}

def read(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    for i, line in enumerate(reader):
        B = line["B"]
        L = line["L"]
        magn_dec = line["magn_dec"]

        dict_BL[i] = {"B": line["B"], "L": line["L"], "H": line["H"], "year": line["year"], "magn_dec": line["magn_dec"]}
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
    if res_gamma > 0:
        res_gamma += 0.01
    else:
        res_gamma -= 0.01
    return (round(res_gamma, 2))

def bussol(magn_dec, gamma):
    corr_bussol = float(magn_dec) - gamma
    return corr_bussol

def my_print():
    print("B:", i[1]["B"], "L:", i[1]["L"])
    print("Магнитное склонение:", i[1]["magn_dec"])
    print("Сближение меридианов:", g)
    print("Поправка для буссоли", buss)
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
        my_print()


