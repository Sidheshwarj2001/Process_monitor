import psutil

def processDisplay():
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)

            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listProcess

def main():
    print("Marvellous Infosystem : python Automation and machine learning")
    print("Process monitor with memory usage")

    listProcess = processDisplay()

    for ele in listProcess:
        print(ele)

if __name__ == '__main__':
    main()