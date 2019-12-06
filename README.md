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
| `/customer_orders/<id>` | to retrieve order by identifier(id) |
| `/customer_orders/<id>/` | to update and delete an order |
| `/customer_orders/?status=<status>&customer_name=<customer_name>/` | to filter either by status or customer_name or both |
| `/modify/<pizza id>/` | to update and delete an order |

An automatic generated interactive API documentation can be found under http://127.0.0.1:8000/docs/ if the server is running.

## Tests
To run the tests:
```
python manage.py test
```
