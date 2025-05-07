# Используем официальный Python образ
FROM nginx:alpine

COPY nginx-service.conf /etc/nginx/conf.d/nginx-service.conf

CMD ["nginx", "-g", "daemon off;"]