build:
	docker-compose build

start:
	docker-compose up

restart:
	docker-compose stop website && docker-compose start website

shell:
	docker-compose exec website bash

sync-media:
	rsync -avz --delete epix:/volumes/xrsouthsea/media/ volumes/media/

sync-db:
	docker-compose up -d mysql; \
	ssh epix "docker exec mysql bash -c 'mysqldump -u root --password=\$$MYSQL_ROOT_PASSWORD xrsouthsea'" > xrsouthsea.sql; \
	docker-compose exec mysql bash -c 'mysql -u root --password=$$MYSQL_ROOT_PASSWORD -e "DROP DATABASE xrsouthsea;"'; \
	docker-compose exec mysql bash -c 'mysql -u root --password=$$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE xrsouthsea;"'; \
	docker cp xrsouthsea.sql xr-southsea-mysql:/tmp/; \
	docker exec xr-southsea-mysql bash -c 'mysql -u root --password=$$MYSQL_ROOT_PASSWORD xrsouthsea < /tmp/xrsouthsea.sql'; \
	docker exec xr-southsea-mysql bash -c 'rm /tmp/xrsouthsea.sql'; \
	docker-compose stop mysql
