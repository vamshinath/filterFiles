#!/usr/python3
import sys,os,shutil

names=[]

def fileOrganizer(allFiles):

    if not os.path.isdir("FILTER"):
        os.mkdir("FILTER")
    
    for dr in allFiles.keys():
        try:
            os.mkdir(dr)
        except Exception as e:
            k=0
        ffiles = allFiles.get(dr)
        for fl in ffiles:
            try:
                print(fl)
                shutil.move(fl,dr+"/"+fl.split("/")[-1])
            except Exception as e:
                k=0
        try:
            shutil.move(dr,"FILTER/"+dr)
        except Exception as e:
            k=0
    

def scanFiles(second=False):
    files=[]
    for root,drs,fls in os.walk("."):
        for fl in fls:
            if second == True and not "9351" in fl:
                continue
            try:
                if os.path.isfile(fl):
                    fullfl=os.path.abspath(os.path.join(root,fl))
                    files.append(fullfl)
            except Exception as e:
                print(e)
    return files

def loadNames():
    global names

    with open("/home/vamshi/names.txt","r") as fl:
        for ln in fl:
            names.append(ln[:-1])

def mainEngine(files):

    pqueue={}

    for name in names[::-1]:
        namefiles=[]
        for fl in files:
            exactfl = fl.split("/")[-1]
            if name in exactfl.lower():
                namefiles.append(fl)
                files.remove(fl)
        pqueue[name]=namefiles
    
    fileOrganizer(pqueue)


def main():

    os.chdir(sys.argv[1])

    loadNames()

    files = scanFiles()

    mainEngine(files)

    os.system("find . -type d -empty -delete")


if __name__ == "__main__":
    main()