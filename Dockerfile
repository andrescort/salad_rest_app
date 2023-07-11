# Utiliza la imagen base de Alpine Linux 3.18.2
FROM alpine:3.18.2

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de sistema necesarias
RUN apk update \
  && apk add --no-cache py3-pip \
  && rm /etc/apk/repositories

# Copia los archivos de la aplicación a la imagen
COPY . /app


# RUN install requerimients
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

# Ejecuta la aplicación de Flask
CMD ["python3", "/app/run.py"]
