import os

def move_file(command: str):
    commands, file_in, file_out = command.split()
    directory, file_out = file_out.rsplit("/", 1)
    parent_directory = os.path.dirname(os.getcwd())
    os.chdir(parent_directory)

    res_path = ""
    for path in directory.split("/"):
        res_path += path + "/"
        os.mkdir(res_path)

    file_path = os.path.join(res_path, file_out)
    with open(file_in, "r") as file_in, open(file_path, "w") as file_out:
        file_out.write(file_in.read())


move_file("mv file.txt first_dir/second_dir/third_dir/forth_dir/file2.txt")