import csv

dict_BL = {}


def read(f_obj):
    reader = csv.DictReader(f_obj, delimiter=',')
    for i, line in enumerate(reader):
        magn_azimut = line["magn_azimut"]
        true_azimuth = line["true_azimuth"]
        directions_angle = line["directions_angle"]
        magn_dec = line["magn_dec"]
        gamma_result = line["gamma_result"]

        dict_BL[i] = {"magn_dec": line["magn_dec"], "magn_azimut": line["magn_azimut"],
                      "true_azimuth": line["true_azimuth"], "directions_angle": line["directions_angle"],
                      "gamma_result": line["gamma_result"]}
    print(dict_BL)


def my_print():
    print("Магнитный азимут:", i[1]["magn_azimut"], ",", "Истинный азимут:", i[1]["true_azimuth"], ",",
          "Дирекционный угол:", i[1]["directions_angle"])


def calculate_parameters():
    if i[1]["magn_azimut"] != "-":
        true_azimuth = float(i[1]["magn_azimut"]) + float(i[1]["magn_dec"])
        correction_of_direction = float(i[1]["magn_dec"]) - float(i[1]["gamma_result"])
        direction_angle = float(i[1]["magn_azimut"]) + correction_of_direction
        print("Магнитный азимут равен: {0}°".format(i[1]["magn_azimut"]))
        print("Истинный азимут:", true_azimuth)
        print("Дирекционный угол:", round(direction_angle, 3))
        print("===============================")
    elif i[1]["true_azimuth"] != "-":
        magn_azim = float(i[1]["true_azimuth"]) - float(i[1]["magn_dec"])
        correction_of_direction = float(i[1]["magn_dec"]) - float(i[1]["gamma_result"])
        dir_angle = magn_azim + correction_of_direction
        print("Истинный азимут равен: {0}".format(i[1]["true_azimuth"]))
        print("Магнитный азимут равен:{0}".format(magn_azim))
        print("Дирекционный угол равен равен:{0}".format(dir_angle))
        print("+++++++++++++++++++++++++++++++")
    elif i[1]["directions_angle"] != "-":
        correction_of_direction = float(i[1]["magn_dec"]) - float(i[1]["gamma_result"])
        magn_azimuth = float(i[1]["directions_angle"]) - correction_of_direction
        true_azimuth = magn_azimuth + float(i[1]["magn_dec"])
        print("Дирекционный угол равен: {0}°".format(i[1]["directions_angle"]))
        print("Магнитный азимут равен: {0}".format(round(magn_azimuth, 3)))
        print("Истинный азимут равен: {0}".format(round(true_azimuth, 3)))
        print("################################")


if __name__ == "__main__":
    with open("data.csv") as f_obj:
        read(f_obj)
        for i in dict_BL.items():
            # my_print()
            calculate_parameters()
