## Installation
Clone this git repository:
```
git clone https://github.com/manishpal022/pizza_project.git
```
Create a python virtual enviroment for python3 and activate it(you can skip this part)
```
pip install virtualenv
```
```
virtualenv venv
```
(for windows)
```
./venv/Scripts/activate
```

(for Mac/Linux)
```
source ./venv/Scripts/activate
```

Go to the project folder:

```
cd pizza_project
```
Install the requirements:
```
pip install -r requirements.txt
```

## Create Superuser
```
python manage.py createsuperuser  (for windows, Mac, Linux)
```
```
winpty python manage.py createsuperuser   (if running in gitbash)

```
**Input :** (name, email, password1, password2)

Login with above credentials : http://127.0.0.1:8000/admin/

## Setup POSTGRESQL database
We should have postgresql install already. Below is the configuration for postgresql I set in settings.py(line 81-89). You can change as per yours.

**For POSTGRESQL**
```
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'pizza_db',
'USER': 'postgres',
'PASSWORD': '123456',
'HOST': 'localhost'
```
**For SQLITE**
```
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
```

## Running
Run the migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
This will start the webserver on http://127.0.0.1:8000/.

## Documentation
The API endpoints are:
Endpoint	Description

| Endpoint | Description |
| --- | --- |
| `/customer_orders/` | to list the orders from a customer |
| `/customer_orders/` | to create a new order |
| `/customer_orders/<id>/` | to retrieve order by identifier(id) |
| `/customer_orders/<id>/` | to update and delete an order |
| `/customer_orders/?status=<status>&customer_name=<customer_name>/` | to filter either by status or customer_name or both |
| `/admin/order_app/pizzaorder/` | to change status of any order(admin-page) |

Note: 

Only admin can change the status of delivery from admin page(although, we can create another API for pizza owner end).

Customer can delete order until order is in 'Open' status.

Customer cannot update order if status set to 'Delivered'. 

Customer able to order the same flavor of pizza but with different sizes multiple times.

## Tests
To run the tests:
```
python manage.py test
```
