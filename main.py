from mcstatus import JavaServer
import time
import subprocess


server = None
suspend_time = 1200 #20 mins
counter = 0
inc = 5
port = 25565

while True:
	try:
		server = JavaServer("localhost", port)
		server.status()
		break
	except Exception as e:
		print(f"A server was not found on port {port}. Trying again in {inc} seconds...")
		time.sleep(inc)

while True:
	time.sleep(inc)

	t1 = time.time()
	counter += inc
	status = server.status()
	num_players = status.players.online
	print(f"{num_players} online. sleeping in {suspend_time - counter}")
	if num_players > 0:
		counter = 0

	if counter > suspend_time and num_players < 1:
		counter = 0
		subprocess.run(['sudo', 'systemctl', 'suspend'], check=True)
		continue

	t2 = time.time()
	counter -= (t2 - t1)

#print(f"{status.players.online} players online")

