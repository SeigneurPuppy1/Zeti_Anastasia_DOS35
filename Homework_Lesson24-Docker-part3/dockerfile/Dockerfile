FROM ubuntu:20.04

RUN apt-get update && \
apt-get install -y \
curl \
nginx

RUN mkdir -p /app/static/

WORKDIR /app/static/

COPY nginx.conf /etc/nginx/nginx.conf

COPY static/ /app/static/

EXPOSE 8080

CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
