SERVER = server
SERVER_PATH = ./Server2

SERVER2 = server2
SERVER2_PATH = ./Server2


build/server:
	docker build -t $(SERVER) ./Server

run/server:
	docker run -p 80:80 -p 443:443 $(SERVER_PATH)

stop/server:
	docker stop -t $(SERVER)


build/server2:
	docker build -t $(SERVER2) $(SERVER2_PATH)

run/server2:
	docker run -p 80:80 -p 443:443 $(SERVER2)

stop/server2:
	docker stop -t $(SERVER2)