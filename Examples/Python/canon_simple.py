import socket
import time

# LC2 IP address and port
UDP_IP = "192.168.2.252"
UDP_PORT = 1339



print ("ISSI :: LC2 Python3 Script Example\n")


# Command list
MESSAGES = ["ping","setZoom=135"]


# UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setblocking(1)

sock.settimeout(5)
flagDone = False

# Loop on command list
for i in range(len(MESSAGES)): # LC2 command loop
	print ("Sent:", MESSAGES[i])
	start = time.time()

	sock.sendto(MESSAGES[i].encode(), (UDP_IP, UDP_PORT))
	try:
		while flagDone == False:
			data, addr = sock.recvfrom(1024)
			#if data: break
			#print("received: {}".format(data))
			print ("Received:", data.decode("utf-8"))
			if "zoomDone" in data.decode("utf-8"):
				flagDone = True
			end = time.time()
			print(end - start, " seconds")
			
	except  socket.error:
	    print("")
	flagDone = False

