**Тестовое задание**

*Подготовка проекта к запуску*

    pip install -r requirements.txt
    
    python manage.py makemigrations
    
    python manage.py migrate
    
    python manage.py runserver
    
    
*END-POINTs*

**[GET]  http://<domain>/api/resources**

пример ответа:

    {
    "resources": [
        {
            "id": 1,
            "title": "Ресурс 1",
            "amount": 10,
            "unit": "kg",
            "price": 150,
            "date": "2021-04-05",
            "cost": 1500
        },
        {
            "id": 2,
            "title": "Ресурс 2",
            "amount": 16,
            "unit": "liter",
            "price": 100,
            "date": "2021-03-11",
            "cost": 1600
        },
        {
            "id": 3,
            "title": "Ресурс 3",
            "amount": 95,
            "unit": "gramm",
            "price": 1500,
            "date": "2021-03-20",
            "cost": 142500
        },
        {
            "id": 4,
            "title": "res_3",
            "amount": 1000,
            "unit": "kg",
            "price": 12,
            "date": "2021-03-20",
            "cost": 12000
        }
    ],
    "total_count": 4
    }
    
    status 200
    
    
    
**[POST] http://<domain>/api/resources**

пример запроса:

    {
    "title": "res_3",
    "amount": 1000,
    "unit":  "kg",
    "price": 12,
    "date": "2021-03-20"
    }
    
ответ:

    status 200
    
    
**[PUT] http://<domain>/api/resources**

пример запроса:

     {
        "id": 5,
        "title": "Русурс 4",
        "amount": 1000,
        "unit":  "kg",
        "price": 12,
        "date": "2021-03-20"
     }   
    
    
ответ:

    status 200,
           Object does not exist status 400
    
    
**[DELETE] http://<domain>/api/resources**

пример запроса:

    {
    "id": 5
    }
    
ответ:

    status 200, 
           400
           
           
**[GET] http://<domain>/api/total_cost**

пример ответа:

    {
        "total_cost": 145600
    }
    
    status 200