#!/usr/bin/python3

import os


def cleanup(text):

    text = text.replace("Coopyright (C) 1916", "Copyright (C) 2016")
    text = text.replace("\t", "    ")
    text = text.replace("//", "#")
    return text

os.chdir("./ugly")
for local_file in os.listdir("."):
    with open(local_file, "r") as f:
        text = f.read()
        clean_text = cleanup(text)

        # print(clean_text)

        filename, extension = os.path.splitext(local_file)

        new_file = filename + "_cleaned" + extension

        with open(new_file, "w") as f2:
            f2.write(clean_text)