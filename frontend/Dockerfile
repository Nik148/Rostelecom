FROM nginx:1.20-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY register.html /etc/nginx/html/
COPY bootstrap.min.css /etc/nginx/html/



