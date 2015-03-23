import os

def createfolders(name, startpath):
    ## Creates basic project folders based on given project name and path
    folderlist = ["bin","docs",name,"tests"]
    os.chdir(startpath)
    if not os.path.exists(name):
        os.mkdir(name)
        os.chdir(startpath + '\\' + name)
    for folder in folderlist:
        if not os.path.exists(folder):
            os.mkdir(folder)

def createfiles(name,startpath):
    ## Creates basic files in project folders based on given project name
    open("__init__.py","a")
    os.chdir(startpath + "\\" + name + "\\tests")
    open(name + " tests.py","a")
    open("__init__.py","a")

def __main__(name, startpath):
    ##Calls functions to create folders and files based on given project name and path
    createfolders(name,startpath)
    createfiles(name,startpath)

__main__("test1","C:\python34\projects")

