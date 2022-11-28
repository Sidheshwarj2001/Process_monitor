import os
import psutil
import time
from sys import *

def ProcessDisplay(log_Dir = "sid"):
    listProcess = []

    if not os.path.exists(log_Dir):
        try:
            os.mkdir(log_Dir)
        except:
            pass

    seperator = "-"*80
    log_path = os.path.join(log_Dir,"sid%s.log"%(time.time()))

    f= open(log_path,'w')
    f.write(seperator + '\n')
    f.write("sid process logger "+time.ctime()+'\n')
    f.write(seperator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombiesProcess):
            pass

        for element in listProcess:
            f.write('%s\n' %element)

def main():
    print("_______Marvellous Infosystem by sid________")
    print("Application Name is : " , argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of Arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=='-H'):
        print("This script is used log records of running process")
        exit()

    if(argv[1]== '-u' or argv[1]=='-U'):
        print("Usage : ApplicationName Absulate path_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception as e:
        print("Error : Invalid Input",e)

if __name__ == '__main__':
    main()