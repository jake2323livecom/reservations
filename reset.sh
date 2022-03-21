docker-compose down -v
docker rmi reservations_web
docker rmi reservations_nginx
docker build . -t reservations_web
docker build nginx -t reservations_nginx
docker-compose up -d 
