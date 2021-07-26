# Software Developer Assessment Test

This test is an exercise for Holberton School students, and consist in create a web application
focused on a retailer company.

## The Backend

The app have to handle the process of a user creating an order for a retailer company. That is made by a series of endpoints:
We have 4 separate entities that connect to each other: users, orders, shipping, and payments, each one has to save information 
about the domain of each table.

![data_img](https://github.com/dondropo/retailer_company/blob/master/README_imgs/data.png)

All the database have to be created using MySQL, also creating all the relations and conditionals.
The required outgoing end points are (well just a single endpoint "orders" with multiple options and the login endpoint to get the login token):

**login** here you send username and password in order to obtain a token to keep working with the other endpoint.

**orders/#orderid** - pass the order id and get the formatted JSON with the required information.

**orders/[order_ids]** - pass multiple order IDs in string format, separated by comma (,) and return the info of those orders.

**orders/date-start - date-end** - pass two dates and return the ids of the orders between those dates

**orders/shipping/{key=string}** return all orders with the given key (city, state, country) and string as value.

**orders/user_id** return orders from that specific user.

**users/all** list all users basic info

**users/user_id** list the orders from the given user id

**orders/search term -** search for the term given in multiple parts of the order, and return the results

Ordering is received as a parameter, but ordering must be done in the code (not in the queries). And use the standard ordering and searching algorithms.

You are responsible for also building the endpoint that will save all the information for a new user and a new order (quick tip, shipping and payment must have an order, users are independent)

You should document your architecture selection in the README the reasons and why that architecture fits your project. (You are free to use any architecture or patterns you want)

For this you are limited to use:

- Python (Django, Flask, Django rest framework or Fast API)
- MySQL or Postgres.
- You must implement and follow TDD.

## The Front End

You will build a front end for your Rest API, you can use React or plain HTML, CSS and JavaScript (Recommended the later). The design is up to you, but should allow me to see all the above endpoints. This should be a separate project and repository.

You have to include 4 views.

- Login, to get the token a login into the system
- Search: here you have a search box, filters and links, order by, etc.
- Orders list. (result from previous search, could be the same view)
- Order details (for when you select an order)

## DevOps

Your projects should be easily deployed and integrated to one of the major vendors (AWS, Azure, Google Cloud, Heroku) And the configuration files should be included in the repository.

Your system should integrate basic CD (Continuous Deployment), deployment can be done automatically from GitHub or GitLab to your cloud vendor.

## Expected output for an order includes
- order_id
- customer_id
- customer_name
- gov_id
- order_date
- last_payment_date
- order status
- shipping_info
- totals
- user_information

## Author
Alejandro Rusca Moreno