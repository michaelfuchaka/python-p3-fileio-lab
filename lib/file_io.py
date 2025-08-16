def write_file(file_name, file_content):
 with open(f"{file_name}.txt", "w") as f:
         f.write(file_content)


pass


def append_file(file_name, append_content):
        with open(f"{file_name}.txt", "a") as f:
          f.write(append_content)
        pass

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
    pass
