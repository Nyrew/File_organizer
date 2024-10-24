import os
import shutil

path = input("Enter Path: ")

# Convert the path to an absolute path
path = os.path.abspath(path)

# Check if the path exists
if not os.path.exists(path):
    print("The path does not exist.")
    exit()

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(os.path.join(path, extension)):
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    else:
        os.makedirs(os.path.join(path, extension))
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        

print("Files organized successfully.")