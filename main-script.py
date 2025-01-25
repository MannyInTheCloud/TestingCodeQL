import os
from datetime import datetime
from posixpath import split
import shutil

# This variable needs to be changed to the path where the pictures and videos you want to organize are.
# Remember to add a \ to every \ . This is the only way it will accept a path. Example: C:\\Users\\Testing\\Sample
path_to_run = "H:\\<user>\\foldername\\foldername"
# You can limit the type of files that you organize with the list below.
extensions_accepted = [".jpg", ".png", ".mp4"]

# Changes to the directory to run this script
os.chdir(path_to_run)
# Prints a list of files in the path chosen
print(os.listdir(path_to_run))

for file in os.listdir(path_to_run):
    print(file)
    if file[-4:] in extensions_accepted:
        print("this is a picture or a movie")
        all_stats = (os.stat(file))
        date_modified = all_stats.st_mtime
        date_converted = datetime.fromtimestamp(date_modified)
        # print(date_converted)
        string = str(date_converted)
        test = string[:10].split("-")
        # print(test)
        year = test[0]
        month = test[1]
        day = test[2]
        #print("The year is " + year)
        if year not in os.listdir(path_to_run):
            os.mkdir(year)
        #print(path_to_run + "\\" + file)
        current_path_of_file = os.getcwd() + "\\" + file
        new_location = path_to_run + "\\" + year
        # print(current_path_of_file)
        # print(new_location)
        shutil.move(current_path_of_file, new_location)
