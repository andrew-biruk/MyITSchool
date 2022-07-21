import os

MEM = []  # acts like buffer


def file_manage():
    """terminal file observer and mover"""

    def display():
        show_dir()
        action()

    def show_dir():
        """shows contents of current directory"""
        folders = sorted(["\t" + i for i in os.listdir() if os.path.isdir(i)])
        files = sorted(["\t" + i for i in os.listdir() if os.path.isfile(i)])

        print("Location " + os.getcwd() + ":")
        if folders:
            print(" Folders:")
            print(*folders, sep="\n")
        if files:
            print(" Files:")
            print(*files, sep="\n")
        if not folders and not files:
            print("\t* Empty folder *")

    def action():
        """branches execution depending on commands"""
        cmd = input("> ").split()

        if cmd[0] == "exit":
            return
        elif cmd[0] == "go":
            chdir(cmd)
        elif cmd[0] == "back":
            os.chdir("..")
        elif cmd[0] == "make":
            os.makedirs(cmd[1])
        elif cmd[0] == "sel":
            select(cmd)
        elif cmd[0] == "put":
            if MEM:
                put(MEM)
            else:
                print("No files to move")

        display()

    def memorize(extension, files=None):
        """memorizes one file or number of files"""
        if files:
            memory = [os.getcwd() + "/" + i for i in files]
        else:
            memory = [os.getcwd() + "/" + i for i in os.listdir() if i.endswith("." + extension)]
        return memory

    def select(cmd):
        """selects all files of specific extension or one given file"""
        global MEM
        if cmd[1] == "all":
            MEM = memorize(cmd[-1])
        else:
            MEM = memorize(cmd[-1], files=cmd[1:])

    def chdir(cmd):
        """changes directory or creates new if it's not present"""
        way = cmd[-1]
        if os.path.exists(way):
            os.chdir(way)
        else:
            cmd = input("Directory not exist - create? (Y/n) > ")
            if cmd in "Yy":
                os.makedirs(way)

    def put(lst):
        """pasts files from memory to current directory"""
        for i in lst:
            os.rename(i, os.getcwd() + "/" + i.split("/")[-1])
        lst.clear()

    display()


file_manage()
