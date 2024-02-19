import os


def save_result(filename, channel):
    folder_name = "./result"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        pass

    with open(f"./result/{filename}", "w") as file:
        for matrix in channel:
            lines = 0
            for comp in matrix:
                if lines == 10:
                    file.write("\n")
                    lines = 0
                else:
                    file.write(str(comp) + ", ")
                    lines += 1
            file.write("\n")
