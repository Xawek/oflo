import os
import random


def get_user_input():
    print('Hi you in "OFLO"\n"one file - lots objects"\n'
          'possibly would be available at:"https://github.com/Xawek"\n'
          'When I was too lazy to create five folders and 2-3 files'
          '\noh damn, I said folders instead of directories ^_^')
    target_dir = input("Enter path to target directory: ")
    dir_name = input("Enter a base name for directories: ")
    dir_count = int(input("Enter the number of directories: "))
    file_name = input("Enter a base name for files: ")
    min_files = int(input("Enter the minimum number of files: "))

    while True:
        max_files = int(int(input("Enter maximum number of files: ")))
        if max_files >= min_files:
            break
        print('Error: max number of files'
              ' must be greater or equal'
              ' min number of files')

    print(f"\nIn target directory /{target_dir} "
          f"will be created {dir_count} directory"
          f"with files in quantities from {min_files} to {max_files}.\n")

    confirmation = input("Press 'y' button or input 'yes' to continue, "
                         "any else to abort: ")
    if confirmation.lower() in ['y', 'yes']:
        return target_dir, dir_name, dir_count, file_name, min_files, max_files
    return exit()


def create_files(directory, files_count, name_file):
    for i in range(1, files_count + 1):
        new_file_name = f"{name_file}{i}.txt"
        with open(os.path.join(directory, new_file_name), "w") as file:
            file.write("Test file.\n")
    return files_count


def create_objects(target_directory, dir_name, dir_count,
                   file_name, min_files, max_files):
    directories_created = 0
    files_created = 0
    print("start")
    for i in range(1, dir_count + 1):
        directory = f"/{target_directory}/{dir_name}{i}"
        os.makedirs(directory, exist_ok=True)
        files_settings = random.randint(min_files, max_files)
        files_count = create_files(directory, files_settings, file_name)
        files_created = files_created + files_count
        directories_created += 1
    print(f"Directory created: {directories_created}")
    print(f"File created: {files_created}")
    print("done")


def main():
    user_input = get_user_input()
    create_objects(*user_input)


if __name__ == "__main__":
    main()
