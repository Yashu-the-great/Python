import os,shutil


def get_extension(file:str) -> str:
    file = file.split(".")
    return file[len(file)-1]
def move_to_file(file:str, ext:str):
    try:
        if os.path.isdir(ext):
           shutil.move(file,ext)
        else:
            os.mkdir(ext)
            shutil.move(file,ext)
    except:
        pass

def main():
    directory = os.getcwd()
    for file in os.listdir(directory):
        ext = get_extension(file)
        move_to_file(file,ext)
if __name__ == "__main__":
    main()
    