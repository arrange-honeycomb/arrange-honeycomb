import codecs
import configparser
from hexy.hexy import get_spiral, cube_to_pixel
import os
from shutil import copyfile
import time


def arrange(ini_path=None, hex_radius=38, origin_x=1920 / 2, origin_y=1080 / 2):
    if ini_path is None:
        ini_path = os.path.join(
            os.path.expanduser("~"), "AppData", "Roaming", "Rainmeter", "Rainmeter.ini"
        )

    print("Opening ini file '{}'".format(ini_path))
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(ini_path, encoding="utf-16")

    print("Parsing Honeycombs")
    active_honeycombs = []
    for section in config:
        section_active = (
            "Active" in config[section] and config.getint(section, "Active") == 1
        )
        if "Honeycomb" in section and section_active:
            active_honeycombs.append(section)

    changed = False
    radius = 0
    spiral = get_spiral((0, 0, 0), radius_end=radius)
    while len(spiral) < len(active_honeycombs):
        radius += 1
        spiral = get_spiral((0, 0, 0), radius_end=radius)

    pixels = cube_to_pixel(spiral, hex_radius)
    for i, section in enumerate(active_honeycombs):
        pix = pixels[i]
        x, y = (
            int(origin_x + pix[0] - (hex_radius / 2)),
            int(origin_y + pix[1] - (hex_radius / 2)),
        )
        properly_placed = (
            config.getint(section, "WindowX") == x
            and config.getint(section, "WindowY") == y
        )
        if properly_placed:
            print("Not moving {}, it's already in the correct position".format(section))
        else:
            print("Moving {} to ({},{})".format(section, x, y))
            changed = True
            config[section]["WindowX"] = str(x)
            config[section]["WindowY"] = str(y)

    if changed:
        ini_backup_path = ini_path + "." + str(time.time()) + ".bak"
        print("Backing up ini file '{}' to '{}'".format(ini_path, ini_backup_path))
        copyfile(ini_path, ini_backup_path)

        print("Saving ini file.")
        with codecs.open(ini_path, "w", "utf-16") as configfile:
            config.write(configfile, space_around_delimiters=False)
    else:
        print("Nothing changed, move along, nothing to see here...")
