DOCKER_IMAGE_NAME = iot_mts_service

docker-build-service:
	docker build \
		--file=Dockerfile \
		-t $(DOCKER_IMAGE_NAME):latest \
		.

docker-run-service:
	docker run \
		--rm \
		-p 8000:8000 \
		-p 1883:1883 \
		$(DOCKER_IMAGE_NAME):latest