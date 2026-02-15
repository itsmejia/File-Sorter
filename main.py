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


def organize():
    path = data["source-directory"]

    file_name = os.listdir(path) # names all the files in that path

    folder_names = list(data["rules"].values())

    # creates the folders if they don't exist
    for loop in range(len(folder_names)):
        if not os.path.exists(path + "/" + folder_names[loop]):
            os.makedirs((path + "/" + folder_names[loop]))
            print("Created folder: " + folder_names[loop])

    # moves the files into correct folders
    for file in file_name:
        for rule in data["rules"]:
            if rule in file and file not in data["ignore-files"]:
                folder_name = data["rules"][rule]
                if not os.path.exists(path + "/" + folder_name + "/" + file):
                    shutil.move(path + "/" + file, path + "/" + folder_name + "/" + file)
                else:
                    print("File already exists in destination folder.")

print("Commands:")
print("organize - organize files")
print("setup - resetup the program and prefrences")
print("srcfolder - change the source folder")
print("destfolder - change the destination folder")
print("addrule - add a new rule for sorting files")
print("currentrules - view current rules for sorting files")
print("addignore - add a file to the ignore list")
print("currentignore - view current ignore list")
print("removerule - remove a rule from the sorting rules")
print("removeignore - remove a file from the ignore list")

while True:
    user_input = input()
    user_input = user_input.lower()
    if user_input == "organize":
        organize()
    elif user_input == "setup":
        set_up()
    elif user_input == "srcfolder":
        print("Enter the new source folder path:")
        new_src = input()
        data["source-directory"] = new_src
        with open("config.json.gitignore", "w") as config_file:
            json.dump(data, config_file, indent=4)
    elif user_input == "destfolder":
        print("Enter the new destination folder path:")
        new_dest = input()
        data["destination-directory"] = new_dest
        with open("config.json.gitignore", "w") as config_file:
            json.dump(data, config_file, indent=4)
    elif user_input == "addrule":
        print("Eg. .png Images")
        print("type done when done")
        done = False
        while not done:
            user_input = input()
            if user_input == "done":
                done = True
                print("Rule(s) added.")
            else:
                user_input = user_input.split()
                folder_name = ""
                for i in range(1, len(user_input)):
                    folder_name += user_input[i] + " "
                folder_name = folder_name.strip()
                data["rules"][user_input[0]] = folder_name
                with open("config.json.gitignore", "w") as config_file:
                    json.dump(data, config_file, indent=4)
    elif user_input == "currentrules":
        print("Current sorting rules:")
        for rule, folder in data["rules"].items():
            print(f"{rule} -> {folder}")
    elif user_input == "addignore":
        print("Enter the file name to ignore:")
        print("type done when done")
        done = False
        while not done:
            ignore_file = input()
            if ignore_file == "done":
                done = True
            else:
                data["ignore-files"].append(ignore_file)
                with open("config.json.gitignore", "w") as config_file:
                    json.dump(data, config_file, indent=4)
    elif user_input == "currentignore":
        print("Current ignore list:")
        for ignore in data["ignore-files"]:
            print(ignore)
    elif user_input == "removerule":
        print("Enter the rule pattern to remove (e.g., .pdf)")
        rule_to_remove = input()
        if rule_to_remove in data["rules"]:
            del data["rules"][rule_to_remove]
            with open("config.json.gitignore", "w") as config_file:
                json.dump(data, config_file, indent=4)
            print(f"Rule {rule_to_remove} removed.")
        else:
            print("Rule not found.")
    elif user_input == "removeignore":
        print("Enter the file name to remove from ignore list:")
        ignore_to_remove = input()
        if ignore_to_remove in data["ignore-files"]:
            data["ignore-files"].remove(ignore_to_remove)
            with open("config.json.gitignore", "w") as config_file:
                json.dump(data, config_file, indent=4)
            print(f"File {ignore_to_remove} removed from ignore list.")
        else:
            print("File not found in ignore list.")
