import utm
import csv
import math

dict_BL = {}

def read(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    for i, line in enumerate(reader):
        B = line["B"]
        L = line["L"]

        dict_BL[i] = {"B": line["B"], "L": line["L"]}
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

def to_utm(lat, lon):
    z = utm.from_latlon(lat, lon)
    print(z[0], z[1], z[2])
    # return z[0], z[1]

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        read(f_obj)
    for i in dict_BL.items():
        B_res = convert(i[1]["B"])
        L_res = convert(i[1]["L"])
        to_utm(B_res, L_res)
