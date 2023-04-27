import json
import psycopg2

# load the config.json file that contains the database connection information
with open('config.json', 'r') as f:
    config = json.load(f)


# Connect to the database
connection = psycopg2.connect(
    host=config['db_host'],
    port=config['db_port'],
    database=config['db_database'],
    user=config['db_user'],
    password=config['db_password']
)


# Define the functions
def find_pcs(speed, ram):
    """Locate PCs with the given speed and RAM."""

    # Start a transaction
    connection.begin()

    # Execute the query
    cursor = connection.cursor()
    cursor.execute("""
        SELECT model, price
        FROM pc
        WHERE speed = %s
        AND ram = %s
    """, (speed, ram))

    # Fetch the results
    results = cursor.fetchall()

    # Commit the transaction
    connection.commit()

    # Return the results

    cursor.close()
    connection.close()
    return results


def remove_pc(model_number):
    """Remove the PC with the given model number."""

    # Start a transaction
    connection.begin()

    # Execute the query
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM pc
        WHERE model = %s
    """, (model_number,))

    # Fetch the results
    results = cursor.fetchall()

    # Commit the transaction
    connection.commit()

    cursor.close()
    connection.close()

    # Return the results
    return results


def decrease_price(model_number):
    """Decrease the price of the PC with the given model number by $100.00."""

    # Start a transaction
    connection.begin()

    # Execute the query
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE pc
        SET price = price - 100
        WHERE model = %s
    """, (model_number,))

    # Fetch the results
    results = cursor.fetchall()

    # Commit the transaction
    connection.commit()

    cursor.close()
    connection.close()

    # Return the results
    return results


def insert_pc(manufacturer, model_number, speed, ram, disk, price):
    """Insert a new PC into the database."""

    # Start a transaction
    connection.begin()

    # Execute the query
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO product (manufacturer, model, type)
        VALUES (%s, %s, %s)
    """, (manufacturer, model_number, 'PC'))

    cursor.execute("""
        INSERT INTO pc (model, speed, ram, disk, price)
        VALUES (%s, %s, %s, %s, %s)
    """, (model_number, speed, ram, disk, price))

    # Fetch the results
    results = cursor.fetchall()

    # Commit the transaction
    connection.commit()

    cursor.close()
    connection.close()

    # Return the results
    return results
