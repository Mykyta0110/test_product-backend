up:
	docker compose -f docker-compose-local.yaml up --build -d 

down: 
	docker compose -f docker-compose-local.yaml down && docker prune --force