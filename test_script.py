import os
import random

directories_created = 0
files_created = 0


def create_files(directory, files_count):
    for i in range(1, files_count + 1):
        file_name = f"file{i}.txt"
        with open(os.path.join(directory, file_name), "w") as file:
            file.write("Test file.\n")
    return files_count


print("start")
for i in range(1, 6):
    directory = f"/opt/export{i}"
    os.makedirs(directory, exist_ok=True)
    files_count = create_files(directory, random.randint(2, 3))
    files_created = files_created + files_count
    directories_created += 1
print(f"Directory created: {directories_created}")
print(f"File created: {files_created}")
print("done")
