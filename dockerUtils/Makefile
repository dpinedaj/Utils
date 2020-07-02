postgres:
	docker-compose -f postgres-compose.yml up 

zeppelin_build:
	docker build -f zeppelinUtil.Dockerfile -t zeppelin .

zeppelin_up:
	docker run -p 8080:8080 zeppelin

