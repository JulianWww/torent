import torent, os, logging, jpe_types, pickle, time, threading, socket


#crate logger
if True:
    log = logging.getLogger(__name__)

    syslog = logging.FileHandler("log.log")
    log.addFilter(jpe_types.paralel.threadInharitanceFilter())

    formatter = logging.Formatter('in thread %(threadName)s: %(message)s')
    syslog.setFormatter(formatter)
    log.setLevel(logging.WARN)
    log.addHandler(syslog)


    os.system("cls")
name = socket.gethostname()
print(socket.gethostbyname(name))
ip = socket.gethostbyname(name)


s = torent.comunicator(1000, name=None, log=log)
print(torent.decriptUUIDname(s.name))



c = torent.comunicator(1001, name="client_n", log=log)
c.connect(ip, port=1000)

c2 = torent.comunicator(1002, name="client_y", log=log)
c2.connect(ip, port=1000)

c3 = torent.comunicator(1003, name="client_j", log=log)
c3.connect(ip, port=1000)

def x(client, *args, **kwargs):
    print("ran x from client", client.name)
    log.fatal(f"x ran with args {args} from client {client}")


c.addDataPoint("x", x)
c2.addDataPoint("x", x)
s.addDataPoint("x", x)

print(1)
s.finischSetup()


print("_"*20)
c3.postInit()
print("got conections")



print("server",   s.connections.keys())
print("client_n", c.connections.keys())
print("client_y", c2.connections.keys())
print("client_j", c3.connections.keys())



time.sleep(1)

c3.execute("x", 1,5, time.time())