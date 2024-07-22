
docker build -t datalogger . -and docker run -p 8000:8000 --network=mongo-network -it datalogger