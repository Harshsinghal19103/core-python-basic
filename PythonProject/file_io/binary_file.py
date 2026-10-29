import shutil

source = "C:/Users/Lenovo/Downloads/download.jpg"
target = "../files/new_image.png"

shutil.copyfile(source, target)

print(source + " is copied to " + target)


