#Importing the necessary modules to run this script
import platform, psutil, os
#Getting the CPU name and setting a variable for it
CPU = platform.processor()
#Getting the amount of Physical Cores
pCores = str(psutil.cpu_count(logical=False))
#Getting the amount of Virtual Cores
vCores = str(psutil.cpu_count(logical=True))
#Attempting to get the CPU usage in a percent, always returns 0.0 though..
CPUsage = str(psutil.cpu_percent())
#Getting the total memory installed.
totalMem = str(psutil.virtual_memory())
#Getting used and available storage space
disk = psutil.disk_usage('/')

print("Your CPU is %s" % CPU + ". It has %s" % pCores + " physical cores and %s" % vCores + " virtual cores. Your RAM information is %s" % totalMem + ".")
print("You have used %s" % disk.used + " bytes of %s total bytes" % disk.total)
