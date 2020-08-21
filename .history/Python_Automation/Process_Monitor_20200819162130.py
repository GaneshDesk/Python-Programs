import psutil

def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Python Automation Scipt : Process Monitor")

    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__=="__main__":
    main()