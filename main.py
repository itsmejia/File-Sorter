import os, shutil, json

json_string = '''
        {
            "has-set-up": false,
            "source-directory": "",
            "destination-directory": "",
            "rules": {
            },
            "ignore-files": [],
            "group-numbered-files": true
        }
'''

data = json.loads(json_string)

def set_up():
    print("Welcome to File Sorter! Lets get you set up.")
    print("What folder would you like to sort? (ex: C:/Users/name/Documents/)")
    input_src_path = input()
    print("Where would you like to have the files sorted to? (ex: C:/Users/name/Documents/Organized Files/)")
    input_sort_path = input()
    data["source-directory"] = input_src_path
    data["destination-directory"] = input_sort_path
    print("Great! The main part has been set up. Lets move on to the small details.")
    print("What file types would you like to sort? (eg: .png, .jpg, .pdf, .kra, .zip, .exe, .csv)")
    print('Format as: ".png Images"')
    print("Where .png represents the file type and Images represents the folder name.")
    print("Type 'done' when you are finished.")
    done = False
    while not done:
        user_input = input()
        if user_input == "done":
            done = True
        else:
            user_input = user_input.split()
            data["rules"][user_input[0]] = user_input[1]
    print("Now, any files you want us to ignore? (eg. veryimportantdocument.pdf)")
    print("Type 'done' when you are finished.")
    done_two = False
    while not done_two:
        user_input = input()
        if user_input == "done":
            done_two = True
        else:
            data["ignore"].append(user_input)
    print("Now just say yes or no!")
    print("Would you like to group numbered files into a folder? (eg. file1, file2, file3)")
    user_input = input()
    if user_input == "yes":
        data["group-numbered-files"] = True
    data["has-set-up"] = True
    print("Great! You are all done!")

    with open("config.json.gitignore", "w") as config_file:
        json.dump(data, config_file, indent=4)

with open("config.json.gitignore", "r") as config_file:
    data = json.load(config_file)
    if not data["has-set-up"]:
        set_up()

path = data["source-directory"]

file_name = os.listdir(path) # names all the files in that path

folder_names = list(data["rules"].values())
print(folder_names)

# creates the folders if they don't exist
for loop in range(len(folder_names)):
    if not os.path.exists(path + "/" + folder_names[loop]):
        os.makedirs((path + "/" + folder_names[loop]))

# moves the files into correct folders
for file in file_name:
    for rule in data["rules"]:
         if rule in file and file not in data["ignore-files"]:
             folder_name = data["rules"][rule]
             if not os.path.exists(path + "/" + folder_name + "/" + file):
                 print(path + "/" + file, path + "/" + folder_name + "/" + file)
                 shutil.move(path + "/" + file, path + "/" + folder_name + "/" + file)
                 e=3
             else:
                 print("File already exists in destination folder.")
