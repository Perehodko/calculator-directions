import csv
import math
from pyproj import Transformer
import pandas as ps
import argparse
import os

dict_BL = {}


# read data from csv file
def read(file_name):
    try:
        with open(file_name) as f_obj:
            reader = csv.DictReader(f_obj, delimiter=',')
            for i, line in enumerate(reader):
                dict_BL[i] = {"B": line["B"], "L": line["L"], "zone": line["zone"], "H": line["H"],
                              "year": line["year"],
                              "magn_dec": line["magn_dec"]}
        return dict_BL
    except Exception as e:
        print("Перепроверьте csv файл", e)


# convert str to degree
def convert(value):
    pos_angler = value.find("ᵒ")
    angler = value[:pos_angler]
    # find position of minute
    pos_minute = value.find("'")
    minute = value[pos_angler + 1:pos_minute]
    # convert data to degree
    degree = float(angler) + float(minute) / 60
    # print("degree", degree)
    return degree


# calculate the number of zone
def number_of_zone(L_r):
    zone_r = int((L_r / 6) + 1)
    return zone_r


# calculate axial meridian zone
def zero_l(zone_r):
    L0 = 6 * zone_r - 3
    return L0


# calculate meridian
def gamma(B, L, L0):
    radians_B = math.radians(B)
    res_gamma = (L - L0) * math.sin(radians_B)
    # if res_gamma > 0:
    #     res_gamma += 0.01
    # else:
    #     res_gamma -= 0.01
    # return (round(res_gamma, 2))
    return res_gamma


# calculate amedment of bussol
def bussol(magn_dec, gamma):
    corr_bussol = float(magn_dec) - gamma
    return corr_bussol


# convert coordinate to epsg code
def convert_coord(line_z, B, L):
    zone_dict = {"39": "epsg:32639", "31": "epsg:32631", "51": "epsg:32651", "52": "epsg:32652", "42": "epsg:32642",
                 "53": "epsg:32653"}
    if line_z in zone_dict:
        # print(zone_dict[line_z])
        global epsg
        epsg = zone_dict[line_z]

    transformer = Transformer.from_crs("epsg:4326", epsg)
    b = transformer.transform(B, L)
    return b


# write result of calculate to csv file
def writer_to_csv(list_gamma):
    df = ps.read_csv("data.csv", sep=",", engine="python")
    df['gamma_result'] = list_gamma
    df.to_csv("data.csv", index=False)


# print beautiful result
def my_print():
    print("B:", i[1]["B"], "L:", i[1]["L"])
    print("X:", round(res_flat_coord[0]), "Y:", round(res_flat_coord[1]), "зона - ", epsg)
    print("H:", i[1]["H"], "м")
    print("Год:", i[1]["year"])
    print("Магнитное склонение:", i[1]["magn_dec"])
    print("Сближение меридианов:", round(g, 3))
    print("Поправка для буссоли", round(buss, 3))
    # print("zone",zone_r)
    print("\n")


# check exists file
def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f


list_gamma = []
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read file name form Command line.")
    parser.add_argument("-f", "--file_name", dest="filename", required=True, type=validate_file,
                        help="input file", metavar="FULL_PATH_TO_FILE")
    args = parser.parse_args()
    filename = args.filename
    read(filename)
    for i in dict_BL.items():
        # print(i[1]["B"])
        B_r = convert(i[1]["B"])
        L_r = convert(i[1]["L"])
        zone_r = number_of_zone(L_r)
        g = gamma(B_r, L_r, zero_l(zone_r))
        list_gamma.append(round(g, 3))
        buss = bussol(i[1]["magn_dec"], g)
        res_flat_coord = convert_coord(i[1]["zone"], B_r, L_r)
        my_print()
    writer_to_csv(list_gamma)
    # print(list_gamma)
