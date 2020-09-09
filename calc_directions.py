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
        magn_dec = line["magn_dec"]

        dict_BL[i] = {"magn_dec" : line["magn_dec"], "magn_azimut": line["magn_azimut"], "true_azimuth": line["true_azimuth"], "directions_angle": line["directions_angle"]}
    print(dict_BL)

def my_print():
    print("Магнитный азимут:", i[1]["magn_azimut"], ",", "Истинный азимут:", i[1]["true_azimuth"], ",", "Дирекционный угол:", i[1]["directions_angle"])


def calculate_parameters():
    if i[1]["magn_azimut"] != "-":
        true_azimuth = float(i[1]["magn_azimut"]) +  float(i[1]["magn_dec"])
        correction_of_direction = float(i[1]["magn_dec"]) - ()
        print("Магнитный азимут равен: {0}°".format(i[1]["magn_azimut"]))
        print("Истинный азимут:", true_azimuth)
    elif i[1]["true_azimuth"] != "-":
        print("Истинный азимут не равен 0")
    elif i[1]["directions_angle"] != "-":
        print("Дирекционный угол не равен 0")


if __name__ == "__main__":
    with open("data.csv") as f_obj:
        read(f_obj)
        for i in dict_BL.items():
            # my_print()
            calculate_parameters()