import os
import re

input_text = input("Enter Pattern name :")

str1 = input_text + "+\w"
print(str1)


def get_filepaths(directory):
    present_file = []

    for root, dir, files in os.walk(directory):
        for filename in files:
            if (re.findall(str1, filename)):
                present_file.append(filename)

    return present_file


full_file = get_filepaths("E:\python programs\TopGear\File io\OS check")
print(full_file)
print(len(full_file))


import os


input_text = input("Enter Pattern name :")


def get_filepaths(directory):
    filtered_data = []
    present_count = {}
    new_data={}
    for root, dir, files in os.walk(directory):
        for filename in files:

            filepath = os.path.join(root, filename)
            #file_paths.append(filepath)
            f = open(filepath,"r")
            str_list = f.read().split()
            ctr = str_list.count(input_text)
            present_count[filename] = ctr

    for key, value in present_count.items():

        if value > 0:
            new_data[key] = value
    return new_data,present_count


file_input_count,present_count = get_filepaths("E:\python programs\TopGear\File io\OS check")

print(len(file_input_count))
print(file_input_count)
print(present_count)
