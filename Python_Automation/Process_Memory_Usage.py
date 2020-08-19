# Automation script which display all running processes.
# Display memory consumed by each process.


import psutil

def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024 * 1024)
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