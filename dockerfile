FROM python:3.11-slim

WORKDIR /app

COPY . /app/
RUN chmod +x ./boot.sh
RUN chmod +x ./entrypoint.sh
RUN ./boot.sh
ENTRYPOINT [ "./entrypoint.sh" ]