def count_words(fp):
    # open file at filepath 'fp' in 'read' mode
    with open(file=fp, mode="r") as f:
        # read the file content
        data = f.read()
        # split the file content into a list of words
        # using 'whitespace' as delimiter
        words = data.split()
    # return the word count
    return len(words)


def copy_file_content(read_fp, write_fp):
    # open file at filepath 'read_fp' in 'read' mode
    with open(read_fp, "r") as rf:
        # read the file content
        data = rf.read()
    # open file at filepath 'write_fp' in 'write' mode
    with open(write_fp, "w") as wf:
        # write file content to file
        wf.write(data)


def remove_newline(fp):
    # open file at filepath 'fp' in 'read' mode
    with open(fp, "r") as f:
        # read file content
        # remove all newline characters
        data = f.read().replace("\n", "")
    # open file at filepath 'fp' in 'write' mode
    with open(fp, "w") as f:
        # write edited file content to file
        f.write(data)
