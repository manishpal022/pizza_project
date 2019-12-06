## Installation
Clone this git repository:
```
git clone https://github.com/manishpal022/pizza_project.git
```
Create a python virtual enviroment for python3 and activate it.

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
python manage.py createsuperuser
```
input name, password
Login with above credentials : http://127.0.0.1:8000/admin/

## Running
Run the migrations:
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

| Command | Description |
| --- | --- |
| `/customer_orders/` | to list the orders from a customer |
| `/customer_orders/` | to create a new order |
| `/customer_orders/<id>/` | to retrieve order by identifier(id) |
| `/customer_orders/<id>/` | to update and delete an order |
| `/customer_orders/?status=<status>&customer_name=<customer_name>/` | to filter either by status or customer_name or both |
| `http://127.0.0.1:8000/admin/order_app/pizzaorder/` | to change status of any order(admin-page) |

Note: 

Only admin can change the status of delivery from admin page(although, we can create another API for pizza owner end).

Customer can delete order until order in Open status.

Customer cannot update order if status set to delivered. 

## Tests
To run the tests:
```
python manage.py test
```
