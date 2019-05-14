# Project Title

Catalog App

## Getting Started

To use the application, extract project-assaf.zip
open the folder with the extracted files, and in the console type 'python someData.py'
a new file called 'catalog.db' will be created in the folder
now execute 'python project_catalog' to start the server on port 5000

## About the application

The application is an audio devices store (I took the product names from www.bestbuy.com)
You can see in the left side, the list of categories, choosing a category will show it's items on the right panel

### Things you can do

You can view and item under any category with no restrictions.
If you login to the application (using the link in the top right corner) you have more option available:
 1. edit any items
 2. delete any item
 3. create new item in a category (the item will be added to the category)

## Step taken to create the application

I used Python to develop the application, Flask to manage the REST server and to render the HTML templates and JSON endpoints,
Also made use of flask_oauthlib to manage the connection with google authorization server and to register users.
I used sqlalchemy in order to model the SQL tables in easier way to work with in my application.

## Author

Assaf Cohen
