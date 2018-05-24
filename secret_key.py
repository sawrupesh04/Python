import os


def open_file():
    path = os.listdir(r"C:\Users\user\Desktop\HackerRank\prank")
    print(path)

    # get the current working directory by using getcwd keyword
    current_dir = os.getcwd()
    print(current_dir)

    # change current working directory by using chdir keyword
    os.chdir(r"C:\Users\user\Desktop\HackerRank\prank")
    change_dir = os.getcwd()
    print(change_dir)

    # rename th folder name
    for save_file in path:
        os.rename(save_file, save_file.strip("0123456789"))

    os.chdir(current_dir)






open_file()
