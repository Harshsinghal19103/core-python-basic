import re
import os


def Correctgmail():
    pathdir = os.path.dirname(__file__)
    input_path = os.path.join(pathdir, "..", "files", "gmail.txt")
    output_path =os.path.join(pathdir, "..", "files", "correct_gmail.txt")

    input_file = open(input_path, "r")
    output_file = open(output_path, "w")

    for lines in input_file:
        if (re.search("gmail.com", lines)):
            output_file.write(lines)
    input_file.close()
    output_file.close()


Correctgmail()
