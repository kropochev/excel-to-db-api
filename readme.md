# Excel to database API

## Установка
Клонировать этот репозиторий `git clone https://github.com/kropochev/excel-to-db-api.git`

## Запуск с помощью Docker-Compose
1. Проверить, что `Docker` работает локально
2. Создать образ `docker-compose build`
3. Запустить `docker-compose up`

## Загрузка файлов
```
curl --location --request POST 'http://127.0.0.1:8000/api/upload/' \
--form 'bills_file=@"bills.xlsx"' \
--form 'clients_file=@"client_org.xlsx"'
```

## Получение списка клиентов
`curl --location --request GET 'http://127.0.0.1:8000/api/clients/'`

### Пример ответа
```
{
    "client1": {
        "organizations": [
            "OOO Client1Org1"
        ],
        "sum": 543798
    },
    "client2": {
        "organizations": [
            "OOO Client2Org1"
        ],
        "sum": 14777
    }
}
```
# Получение списка счетов с фильтром по клиентам

`curl --location --request GET 'http://127.0.0.1:8000/api/bills/?client=client1'`

# Получение списка счетов с фильтром по организации

`curl --location --request GET 'http://127.0.0.1:8000/api/bills/?organization=OOO Client1Org1'`
