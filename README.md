# Vendor Management Project
This project is designed for managing vendors, purchase orders, and performance metrics.

## Setup Instructions
1. Clone the repository: git clone https://github.com/munamunna/VendorManagement.git
2. Create Virtual Environment:python -m venv venv
3.Activate Virtual Environment
4. Install dependencies: pip install -r requirements.txt
5. Run migrations: python manage.py migrate
6. Start the development server: python manage.py runserver
7.Access the API:
Open your browser and go to http://localhost:8000/api/ or use tools like Postman to interact with the API.
or
Open your browser and go to http://localhost:8000/swagger/ 

##User Types:

The project defines user types, including admin, customer, and vendor, allowing for role-based access control.

## API Endpoints
#register
=======
localhost:8000/api/register/
method:POST
data:{username,email,password}

#token
=======
localhost:8000/api/login/
method:POST
data:{username,password}




#Vendors
========
#Create a New Vendor:
====================
localhost:8000/api/vendors/
method:POST
data:{ name, contact details, address, unique vendor code.}
authentication:token

#List all Vendors:
=================
localhost:8000/api/vendors/
method:GET
authentication:token

#Retrieve a Specific Vendor's Details:
====================================
localhost:8000/api/vendors/{vendor_id}/
method:GET
authentication:token

#Update a Vendor's Details:
==========================
localhost:8000/api/vendors/{vendor_id}/
method:PUT
data:{ name, contact details, address, unique vendor code.}
authentication:token

#Delete a Vendor:
================
localhost:8000/api/vendors/{vendor_id}/
method:DELETE
authentication:token




#Purchase Orders
===============
#Create a Purchase Order:
=======================
localhost:8000/api/purchase_orders/
method:POST
data:{  po_number,vendor,order_date,delivery_date,items,quantity,status,quality_rating(optional),issue_date,acknowledgment_date}
authentication:token

#List all Purchase Orders:
==========================
localhost:8000/api/purchase_orders/
method:GET
Query Parameters: vendor (optional) to filter by vendor.

#Retrieve Details of a Specific Purchase Order:
==============================================
localhost:8000/api/purchase_orders/{po_id}/
method:GET

#Update a Purchase Order:
========================
localhost:8000/api/purchase_orders/{po_id}/
method:PUT
data:{po_number,vendor,order_date,delivery_date,items,quantity,status,quality_rating(optional),issue_date,acknowledgment_date}
authentication:token

#Delete a Purchase Order:
=======================
localhost:8000/api/purchase_orders/{po_id}/
method:Delete




#Vendor Performance Metrics
===============================================================
localhost:8000/api/vendors/{vendor_id}/performance/
method:GET
authentication:token
