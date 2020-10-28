import csv
import argparse
import os

dict_BL = {}


def read(filename):
    try:
        with open(filename) as f_obj:
            reader = csv.DictReader(f_obj, delimiter=',')
            for i, line in enumerate(reader):
                dict_BL[i] = {"magn_dec": line["magn_dec"], "magn_azimut": line["magn_azimut"],
                              "true_azimuth": line["true_azimuth"], "directions_angle": line["directions_angle"],
                              "gamma_result": line["gamma_result"]}
                # print(dict_BL)
            return dict_BL
    except Exception as e:
        print("Recheck of csv file:", e, type(e))


def my_print():
    print("Магнитный азимут:", i[1]["magn_azimut"], ",", "Истинный азимут:", i[1]["true_azimuth"], ",",
          "Дирекционный угол:", i[1]["directions_angle"])


def calculate_parameters():
    if i[1]["magn_azimut"] != "-":
        magn_azimuth = float(i[1]["magn_azimut"])
        magn_dec = float(i[1]["magn_dec"])
        gamma_rez = float(i[1]["gamma_result"])
        true_azimuth = magn_azimuth + magn_dec
        correction_of_direction = magn_dec - gamma_rez
        direction_angle = float(magn_azimuth) + correction_of_direction
        beautiful_print(magn_azimuth, true_azimuth, direction_angle)
    elif i[1]["true_azimuth"] != "-":
        true_azimuth = float(i[1]["true_azimuth"])
        magn_dec = float(i[1]["magn_dec"])
        magn_azimuth = true_azimuth - magn_dec
        gamma_rez = float(i[1]["gamma_result"])
        correction_of_direction = magn_dec - gamma_rez
        direction_angle = magn_azimuth + correction_of_direction
        beautiful_print(magn_azimuth, true_azimuth, direction_angle)
    elif i[1]["directions_angle"] != "-":
        direction_angle = float(i[1]["directions_angle"])
        magn_dec = float(i[1]["magn_dec"])
        gamma_result = float(i[1]["gamma_result"])
        correction_of_direction = magn_dec - gamma_result
        magn_azimuth = direction_angle - correction_of_direction
        true_azimuth = magn_azimuth + magn_dec
        beautiful_print(magn_azimuth, true_azimuth, direction_angle)


def beautiful_print(magn_azimuth, true_azimuth, direction_angle):
    print("Магнитный азимут равен: {0}°".format(magn_azimuth))
    print("Истинный азимут: {0}°".format(true_azimuth))
    print("Дирекционный угол равен равен: {0}°".format(round(direction_angle, 3)))
    print("\n")


# check exists file
def validate_file(file):
    if not os.path.exists(file):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(file))
    return file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read file name form Command line.")
    parser.add_argument("-f", "--file_name", dest="filename", required=True, type=validate_file,
                        help="input file", metavar="FULL_PATH_TO_FILE")
    args = parser.parse_args()
    filename = args.filename
    read(filename)
    for i in dict_BL.items():
        calculate_parameters()
