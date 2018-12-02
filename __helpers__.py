def get_file_content(path):
    with open(path, "r+t") as f:
        for line in f:
            yield line
