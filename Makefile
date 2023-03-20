include .secrets
include .settings

build/proxy:
	docker build -t proxy ./proxy

build/server/%:
	docker build -t server$(basename $*) ./server$(basename $*)

build/client:
	docker build -t client ./client

run/client:
	docker run --rm --name client \
	-e SERVER_NETWORK_URL=$(SERVER_NETWORK_URL) \
	-e PROXY_NETWORK_URL=$(PROXY_NETWORK_URL) \
	-e HOST=$(HOST) \
	--network=mynetwork \
	-p 8080:8080 client \

run/proxy:
	docker run --rm --name proxy \
	-e SERVER_NETWORK_URL=$(SERVER_NETWORK_URL) \
	-e HOST=$(HOST) \
	--network=mynetwork \
	-p 80:80 proxy \

run/server/%:
	docker run --rm --name server$(basename $*) \
	--network=mynetwork \
	-e DB_PASSWORD=$(DB_PASSWORD) \
	-e DB_USER=$(DB_USER) \
	-e DB_HOST=$(DB_HOST) \
	-e DB_NAME=$(DB_NAME) \
	-e HOST=$(HOST) \
	-p 443:443 server$(basename $*)

restart/proxy:
	make stop/proxy; make build/proxy; make run/proxy

stop/last:
	docker stop $(docker ps -q -n 1)

stop/all:
	docker stop $(docker ps -aq)

stop/%:
	docker stop $(basename $*)

show/server/%:
	docker exec server$(basename $*) mysql -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME) -e "SELECT * FROM users"
