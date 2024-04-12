docker.install:
	docker compose build --force-rm

docker.run:
	docker compose up -d  # Start containers in detached mode

docker.import.model: docker.run
	docker compose exec ollama ollama pull gemma:2b
