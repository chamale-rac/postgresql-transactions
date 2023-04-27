# postgresql-transactions
## Implementing a PC Inventory Management

This repository contains Python code for working with a PostgreSQL database. The code allows you to perform the following operations:

Find PCs: Given a speed and RAM, the code queries the pc table in the database to find all PCs that match the given speed and RAM.

Remove PC: Given a model number, the code removes the corresponding PC from both the pc table and the product table.

Decrease Price: Given a model number, the code decreases the price of the corresponding PC in the pc table by 100.

Insert PC: Given information about a new PC (manufacturer, model number, speed, RAM, disk size, and price), the code inserts a new row into both the pc table and the product table.

The code uses a configuration file (config.json) to connect to the PostgreSQL database. The psycopg2 library is used to interact with the database.

To run the code, simply execute python main.py and follow the prompts. You will be presented with a menu of options to choose from. Choose the option that corresponds to the operation you want to perform, and enter any required input when prompted.

Remember to modify the config.json file with the correct credentials for your own connection.

The schema and test data used in this example is contained in the schema.sql file.
