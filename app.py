"""This programme works on Customers, Products and Order Table"""

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Northwind'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def get():
    """This will return home page"""

    return {'status': 'SUCCESS', 'data': 'Hello World!'}


@app.route('/customers/<customer_id>', methods=['GET', 'PUT'])
def index(customer_id):
    """This part will do select and update operation on customers table """
    cur = mysql.connection.cursor()
    if request.method == 'GET':
        select_query = "select * from Customers where CustomerID = '{}' ".format(
            customer_id)
        cur.execute(select_query)
        data = cur.fetchall()
        if bool(data):
            row_headers = [x[0] for x in cur.description]
            json_data = []
            for result in data:
                json_data.append(dict(zip(row_headers, result)))
            cur.close()
            return (jsonify(json_data[0]), 200)
        return ({'status': 'FAILED', 'data': 'No Customer Found'},
                404)

    details = request.get_json()

    company_name = details['CompanyName']
    contact_name = details['ContactName']
    contact_title = details['ContactTitle']
    address = details['Address']
    city = details['City']
    region = details['Region']
    postal_code = details['PostalCode']
    country = details['Countary']
    phone = details['Phone']
    fax = details['FAX']

    try:
        cur.execute("""UPDATE Customers SET CompanyName=(%s),
            ContactName=(%s), ContactTitle=(%s),
            Address=(%s), City=(%s), Region=(%s), PostalCode=(%s),
            Countary=(%s), Phone=(%s), FAX =(%s)
            where CustomerID = (%s)""",
                    [
                        company_name,
                        contact_name,
                        contact_title,
                        address,
                        city,
                        region,
                        postal_code,
                        country,
                        phone,
                        fax,
                        customer_id,
                    ])
        mysql.connection.commit()
        return ({'status': 'SUCCESS'}, 200)
    except Exception as err:
        print('Oops Error while updating:{}'.format(err))
        return ({'status': 'FAILED', 'data': '{}'.format(err)}, 404)
    finally:
        cur.close()


@app.route('/customers', methods=['POST'])
def select():
    """This part will do insert operation on customers table """
    details = request.get_json()

    customers_id = details['CustomerID']
    company_name = details['CompanyName']
    contact_name = details['ContactName']
    contact_title = details['ContactTitle']
    address = details['Address']
    city = details['City']
    region = details['Region']
    postal_code = details['PostalCode']
    countary = details['Countary']
    phone = details['Phone']
    fax = details['FAX']
    cur = mysql.connection.cursor()
    try:
        cur.execute("""INSERT INTO Customers (CustomerID, CompanyName,ContactName,
            ContactTitle,Address,City,Region,PostalCode,Countary,Phone,FAX)
            VALUES (%s, %s, %s,%s,%s,%s,%s, %s,%s,%s,%s)""",
                    [
                        customers_id,
                        company_name,
                        contact_name,
                        contact_title,
                        address,
                        city,
                        region,
                        postal_code,
                        countary,
                        phone,
                        fax,
                    ])

        mysql.connection.commit()
        return ({'status': 'SUCCESS'}, 200)
    except Exception as err:
        print('Oops() Error while inserting:{}'.format(err))
        return ({'status': 'FAILED', 'data': '{}'.format(err)}, 404)
    finally:
        cur.close()


@ app.route('/products/<product_id>', methods=['GET', 'PUT'])
def product(product_id):
    """This part will do select and update operation on products table """
    cur = mysql.connection.cursor()
    if request.method == 'GET':
        select_query = 'select * from Products where ProductID = {} '.format(
            product_id)
        try:
            cur.execute(select_query)
            data = cur.fetchall()
            if bool(data):
                row_headers = [x[0] for x in cur.description]
                json_data = []
                for result in data:
                    json_data.append(dict(zip(row_headers, result)))
                cur.close()
                return (jsonify(json_data[0]), 200)
            return ({'status': 'FAILED', 'data': 'No Product Found'
                     }, 404)
        except OSError:

            # Returns a system-related error

            return ({'status': 'FAILED',
                     'data': 'Something Wrong! Please retry after sometime.'
                     }, 500)
    elif request.method == 'PUT':

        details = request.get_json()

        product_name = details['ProductName']
        supplier_id = details['SupplierID']
        category_id = details['CategoryID']
        quantity_per_unit = details['QuantityPerUnit']
        unit_price = details['UnitPrice']
        units_in_stock = details['UnitsInStock']
        units_on_order = details['UnitsOnOrder']
        reorder_level = details['ReorderLevel']
        discontinued = details['Discontinued']

        try:
            cur.execute("""UPDATE Products SET ProductName=(%s),
            SupplierID=(%s), CategoryID=(%s),
                QuantityPerUnit=(%s), UnitPrice=(%s), UnitsInStock=(%s),
                 UnitsOnOrder=(%s),
                ReorderLevel=(%s), Discontinued=(%s)
                where ProductID = (%s)""",
                        [
                            product_name,
                            supplier_id,
                            category_id,
                            quantity_per_unit,
                            unit_price,
                            units_in_stock,
                            units_on_order,
                            reorder_level,
                            discontinued,
                            product_id,
                        ])
            mysql.connection.commit()
            return ({'status': 'SUCCESS'}, 200)
        except Exception as err:
            print('Oops Error while updating:{}'.format(err))
            return ({'status': 'FAILED', 'data': '{}'.format(err)}, 400)
        finally:
            cur.close()


@ app.route('/products', methods=['POST'])
def process():
    """This part will do insert operation on customers table """
    details = request.get_json()

    products_id = details['ProductID']
    product_name = details['ProductName']
    supplier_id = details['SupplierID']
    category_id = details['CategoryID']
    quantity_per_unit = details['QuantityPerUnit']
    unit_price = details['UnitPrice']
    units_in_stock = details['UnitsInStock']
    units_on_order = details['UnitsOnOrder']
    reorder_level = details['ReorderLevel']
    discontinued = details['Discontinued']

    cur = mysql.connection.cursor()
    try:
        cur.execute("""INSERT INTO Products (ProductID,
        ProductName, SupplierID,CategoryID, QuantityPerUnit,
        UnitPrice, UnitsInStock , UnitsOnOrder, ReorderLevel,
        Discontinued) VALUES (%s, %s,%s,%s,%s,%s, %s,%s,%s,%s)""",
                    [products_id,
                     product_name,
                     supplier_id,
                     category_id,
                     quantity_per_unit,
                     unit_price,
                     units_in_stock,
                     units_on_order,
                     reorder_level,
                     discontinued
                     ])
        mysql.connection.commit()
        return ({'status': 'SUCCESS'}, 200)
    except Exception as err:
        print('Oops Error while inserting:{}'.format(err))
        return ({'status': 'FAILED', 'data': '{}'.format(err)}, 400)
    finally:
        cur.close()


@ app.route('/orderhistory/<customer_id>', methods=['GET'])
def orders(customer_id):
    """This part will display Order history of given customerid"""
    query = "select * from Orders where CustomerID = '{}' ".format(customer_id)
    try:
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if bool(data):
            row_headers = [x[0] for x in cur.description]
            json_data = []
            for result in data:
                json_data.append(dict(zip(row_headers, result)))
            cur.close()
            return (jsonify(json_data), 200)
        return ({'status': 'FAILED', 'data': 'No Orders Found'},
                404)
    except OSError:  # Returns a system-related error

        return ({'status': 'FAILED',
                 'data': 'Something Wrong! Please retry after sometime.'
                 }, 500)


if __name__ == '__main__':
    app.run(debug=True)
