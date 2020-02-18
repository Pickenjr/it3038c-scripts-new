import socket, sys

#hosts = ["www.uc.edu" , "www.google.com" , "www.bing.com"]
#print("Working from host: "+ socket.fqdn())
#for h in hosts:
#   print(h + ": "+ socket.gethostbyname(h))

def gethostnameByIP(h)
try:
    hostname = str(sys.argv[1])
    ip = socket.gethostbyname(hostname)
    print(hostname + " has an IP of "+ ip)
except:
    print("Oops, something is wrong with that host.")