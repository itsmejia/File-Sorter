import os, shutil

path = r"C:/Users/nneka/Downloads/"

file_name = os.listdir(path) # names all the files in that path

folder_names = [
    'image files',
    'zip files',
    'krita files', 
    'csv files', 
    'pdf files',
    'program files'
    ]

# creates the folders if they don't exist
for loop in range(len(folder_names)):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))

# moves the files into correct folders
for file in file_name:
    if ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".kra" in file and not os.path.exists(path + "krita files/" + file):
        shutil.move(path + file, path + "krita files/" + file)
    elif ".zip" in file and not os.path.exists(path + "zip files/" + file):
        shutil.move(path + file, path + "zip files/" + file)
    elif ".exe" in file and not os.path.exists(path + "program files/" + file):
        shutil.move(path + file, path + "program files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    else:
        print("File not moved.")