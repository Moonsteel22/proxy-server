# proxy-server

# Сервер-посредник для интеграции с различными источниками данных.

Вся логика по интеграции сосредоточена в src/integration/logic. Можно считать, что это доменный слой, независимый от фреймворка, орм, базы.

В 1,2 tasks - лежат задачи по простому числу и парсингу кодов сайтов

### API


``` api/v1/gas-stations/{id} - Станция АЗС. Включает услуги и цены на топливо ```

### Разворачивание

1. Клонируйте ветку

``` git clone https://github.com/Moonsteel22/proxy-server.git ```

2. Запустите контейнеры

``` docker-compose up -d ```

3. Создайте суперпользователя для доступа к админке

``` docker exec -it proxy_server_backend_1 poetry run python manage.py createsuperuser ```

### Запуск периодических задач по доставанию данных

1. Нажмите +add напротив Periodic tasks

![image](https://user-images.githubusercontent.com/60964414/227889554-a640f6db-7db6-463b-9e3b-0a770f64e885.png)

2. Выберите название и нужную задачу 
![image](https://user-images.githubusercontent.com/60964414/227889875-76f15cf2-c374-40c9-8970-cbf67cd9797a.png)

3. Добавьте периодичность

![image](https://user-images.githubusercontent.com/60964414/227890160-531dbef4-13f5-45cc-90ad-72416ae71bff.png)

![image](https://user-images.githubusercontent.com/60964414/227890246-87aad82b-fc3a-4aca-84a6-8b609e5e6b9a.png)

4. Сохраните задачу и запустите

![image](https://user-images.githubusercontent.com/60964414/227890429-2a595c00-eb02-40e7-9be5-1dfa13db0bf6.png)




