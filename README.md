## Инструкция к запуску проекта
```
docker-compose build
docker-compose up
```
## Ошибки
```
Error starting userland proxy: listen tcp4 0.0.0.0:15672: bind: address already in use
```
При данной ошибке нужно освободить указанный порт

Если вы на Linux, то вам поможет данная команда
```
sudo fuser -k 15672/tcp
```
