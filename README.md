# A Rest API operating queries on Northwind dataset.
This documentation shows how to run the code and test the API.

# Technologies
1. Language - Python
2. Web framework - Flask
3. Database – MySQL

# Creating Virtual Environment
•
Install the virtualenv package
“ pip3 install virtualenv”
•
Create the virtual environment
“ virtualenv mypython”
•
Activate the virtual environment
“ source mypython/bin/activate”

# Dependencies
Install dependencies from requirements.txt using:
"pip install -r requirements.txt"

# Unit test case
Run unittest cases using:
"python testcases.py"

# Running

Run app using:
"python app.py"
Open “http://localhost:5000/” URL to test the app in the Postman.Routes
1. "http://localhost:5000/customers"
a. In this route, select the POST method then the user can INSERT in Customers Table by passing
JSON Object in the body.
Example:
{
"Address": "Amazing Road",
"City": "Durgapur",
"CompanyName": "ABC Pvt. ltd",
"ContactName": "Kumar",
"ContactTitle": "Accounting Manager",
"Countary": "India",
"CustomerID": "DEMO",
"FAX": "26.47.15.11",
"Phone": "26.47.15.10",
"PostalCode": "51100",
"Region": null
}
b. "http://localhost:5000/customers/<customer_id>"
To UPDATE in Customers table enter the customerID (e.g. VINET) in URL then select the PUT
method and pass the JSON in the body.
Example:
{
"Address": "Fun Place",
"City": "Patna",
"CompanyName": "NULL",
"ContactName": "Kumar sanu",
"ContactTitle": "Accounting Manager",
"Countary": "India",
"CustomerID": "DEMO",
"FAX": "26.47.15.11",
"Phone": "26.47.15.10",
"PostalCode": "51100",
"Region": null
}
c. To SELECT all columns from the Customers table enter the CustomerID in URL and select the
GET method to fetch all data in JSON format.2. "http://localhost:5000/products"
a. In this route, select the POST method then the user can INSERT in Products Table by passing
JSON Object in the body.
Example:
{
"CategoryID": 2,
"Discontinued": 0,
"ProductID": 98,
"ProductName": "Maggie",
"QuantityPerUnit": "15 - 625 g packets",
"ReorderLevel": 5,
"SupplierID": 7,
"UnitPrice": 11.9000,
"UnitsInStock": 29,
"UnitsOnOrder": 4
}
b. "http://localhost:5000/products/<product_id>"
To UPDATE in Products table enter the ProductID (e.g. 5) in URL then select the PUT method and
pass the JSON in the body.
Example:
{
"CategoryID": 1,
"Discontinued": 0,
"ProductID": 98,
"ProductName": "Yipee",
"QuantityPerUnit": "20 - 800 g packets",
"ReorderLevel": 3,
"SupplierID": 5,
"UnitPrice": 9.9000,
"UnitsInStock": 19,
"UnitsOnOrder": 1
}
c. To SELECT all columns from the Products table enter the ProductID in URL and select the GET
method to fetch all data in JSON format.
3."http://localhost:5000/orderhistory/<customer_id>"To get Order history of the given customer to enter the CustomerID in URL and select GET method
this will fetch all the Orders done by that particular customer
