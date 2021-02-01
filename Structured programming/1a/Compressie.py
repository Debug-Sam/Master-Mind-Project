
def compression(file):
    new_file = ""
    with open(file, "r") as f:
        for line in f:
            no_spaces = line.replace(" ", "")
            new_file += no_spaces


        f.close()
    new_file.replace("\n", "")

    with open(file, "w") as f:
        f.write(new_file)

        f.close()

    print("Compression completed")

compression("test.txt")