import csv
import math
import calc

dict_BL = {}

def read(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    for i, line in enumerate(reader):
        magn_azimut = line["magn_azimut"]
        true_azimuth = line["true_azimuth"]
        directions_angle = line["directions_angle"]

        dict_BL[i] = {"magn_azimut": line["magn_azimut"], "true_azimuth": line["true_azimuth"], "directions_angle": line["directions_angle"]}
    print(dict_BL)

def correction_directions():
    # CD =
    pass

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        read(f_obj)