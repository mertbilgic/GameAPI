# GameAPI

Bilgisayar oyunları satan temel e-ticaret işlemlerini yapan bir REST-API

**Dependencies:** Python 3.8.3, Pip, Virtualenv

### Create virtual environment 

```sh
git clone https://github.com/mertbilgic/GameAPI.git
cd gameapi
virtualenv venv
```

### Install depedencies

```sh
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Start

```sh
$ python manage.py runserver
```
##### Authentication
API'ımıza ait end-point'leri kullanabilmek için authentication işlemi yapılmalıdır.

Üç adet ön tanımlı kullanımız bulunmaktadır.

User One | user1@example.com
User Two | user2@example.com
User Three | user3@example.com
Acces ve refresh token'a erişime için aşağıdaki komutu çalıştırınız.
```sh
# POST /api/token/
curl -X POST 'http://127.0.0.1:8000/api/token/' \
-H 'Content-Type: application/json' \
-d '{
    "username":"User One",
    "email":"user1@example.com"
}'
```

##### Hello World
API'ımızı token ile test ederek başlayalım.Root-endpoint'imize istek atabilmek için daha önce aldığımız token'a ihtiyacımız bulunmaktadır.
Terminali açalım ve aşağıdaki komutu girelim.

```sh
# GET /
curl -X GET 'http://127.0.0.1:8000/' \
-H 'Authorization: Bearer **TOKEN**'

{"message":"Hello, world"}
```

##### Search
Search işlemi büyük/küçük harf duyarlı değildir.Anahtar kelimeyi içeren sonuçları kullanıcıya döner.Bu özellik sadece oyun aramayı destekler.
Kullanıcı bir oyun aramak istediğinde aşağıdaki şekilde bir istekte bulanabilir.

Örneğin bir oyunu name özelliği ile aranmak isterse search_fields=name şeklinde, aradığı keyword'ü ise search=One şeklinde belirtilmelidir.Benzeri arama işlemleri category ve year özellikleri içinde yapılabilir.

```sh
# GET api/search
curl -X GET 'http://127.0.0.1:8000/api/search?search=One&search_fields=name' \
-H 'Authorization: Bearer **TOKEN**'
[
  {
    "name":"One on One",
    "year":"1984",
    "category":"Basketbol"
  }
]

```
#### List
Listeleme özelliği sadece category özelliğini desteklemektedir.Kullanıcı bir kategoriye ait bilgileri listelemek isterse category=futbol şeklinde query string eklemelidir.Belirtilen keyword büyük/küçük harf duyarlı değildir kullanıcı kategori ismini tam vermesi beklenir.

```sh
# GET api/list
curl -X GET 'http://127.0.0.1:8000/api/list?category=futbol' \
-H 'Authorization: Bearer **TOKEN**' 
[
    {
        "name": "Kick Off II",
        "year": "1990",
        "category": "Futbol"
    },
    {
        "name": "Emlyn Hughes International Soccer",
        "year": "1988",
        "category": "Futbol"
    }
]
```
#### Add To Cart
Kullanıcı sepete ürün eklemek için almak istediği item id isi belirtip ürünü sepete ekleyebilir.
```sh
# POST /api/v1/addtocart/
curl -X POST 'http://127.0.0.1:8000/api/v1/addtocart/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer **TOKEN**' \
--data-raw '{
    "item_id" : 5
}'
{
    "pk": 16,
    "username": "User Three",
    "items": [
        {
            "item_name": "One on One",
            "year": "1984",
            "quantity": 2
        }
    ],
    "ordered": false,
    "ordered_date": "2021-06-29T20:20:21.726564Z"
}
```
#### Checkout
Kullanıcı siparişini checkout etmek istediğinde aşağıdaki gibi /api/v1/checkout end-point'ine istek atmalıdır.
```sh
# GET /api/v1/checkout/
curl -X POST 'http://127.0.0.1:8000/api/v1/checkout/' \
-H 'Authorization: Bearer  **TOKEN**'

{
    "message": "Success checkout order",
    "pk": 17,
    "email": "user3@example.com",
    "items": [
        {
            "item_name": "One on One",
            "year": "1984",
            "quantity": 2
        }
    ],
    "ordered": true,
    "ordered_date": "2021-06-29T20:49:32.218503Z"
}

```
#### Order History
Kullanıcıya ait eski siparişlerin listelenmesi için /api/v1/orderhistory/ end-point'ine istek atmalıdır.
```sh
# POST /api/v1/orderhistory/
curl -X GET 'http://127.0.0.1:8000/api/v1/orderhistory/' \
-H 'Authorization: Bearer **TOKEN**'

[
    {
        "username": "User Three",
        "email": "user3@example.com",
        "items": [
            {
                "item_name": "One on One",
                "year": "1984",
                "quantity": 13
            }
        ],
        "start_date": "2021-06-29T20:20:21.727272Z",
        "ordered_date": "2021-06-29T20:20:21.726564Z",
        "ordered": true
    },
    {
        "username": "User Three",
        "email": "user3@example.com",
        "items": [
            {
                "item_name": "One on One",
                "year": "1984",
                "quantity": 2
            }
        ],
        "start_date": "2021-06-29T20:49:32.219573Z",
        "ordered_date": "2021-06-29T20:49:32.218503Z",
        "ordered": true
    }
]
```
#### Product List
Tüm ürünleri listelemek için /api/v1/productlist/ end-point'ine istek atmalıdır.
```sh
# GET /api/v1/productlist/
curl -X GET 'http://127.0.0.1:8000/api/v1/productlist/' \
-H 'Authorization: Bearer **TOKEN**'
[
    {
        "name": "Kick Off II",
        "year": "1990",
        "category": "Futbol"
    },
    {
        "name": "Emlyn Hughes International Soccer",
        "year": "1988",
        "category": "Futbol"
    },
    ...
    ... 
```
#### Refresh Token
Access token refresh edilmek istendiğinde aşağıdaki komut kullanılabilir
```sh
# GET /api/v1/productlist/
curl -X POST 'http://127.0.0.1:8000/api/token/refresh/' \
-H 'Content-Type: application/json' \
-d '{
    "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNTA4Njg5OCwianRpIjoiNzQyNDIwYjliZDFlNGY1MGI4ZDI1YmNkM2QyOTg5ODciLCJ1c2VyX2lkIjo0fQ.XCDcIO6WNrUy1AF3p4noB5r6bkEBYUGP8mCqDORTY54"
}'
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1MDAwOTIwLCJqdGkiOiI2YTY0N2Y1MGNmYjM0NGUxODQxMDY3MDg2ZDBjOWU1YSIsInVzZXJfaWQiOjR9.Khu3y4ZwgHhlFuneSxS9fHGzFswjXlAgjbthoBTEMGQ"
}
```