import psutil

def DisplayProcess():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Marvellous Infostystems : Python Automation and Machine Learning")
    print("Process Monitor")

    listprocess = DisplayProcess()

    for ele in listprocess:
        print(ele)

    print(psutil.cpu_times())

if __name__ == '__main__':
    main()