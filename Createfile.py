import os

file_name = (input("Enter File Name :"))
file_path = "/mnt/sdcard/"

with open(os.path.join(file_path, file_name), "w") as f:
    f.write(input("Enter Your Word :"))

print("File Create Successfully...")