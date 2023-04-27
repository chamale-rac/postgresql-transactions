'''
CREATE TABLE product
(
    manufacturer VARCHAR(255),
    model        VARCHAR(255),
    type         VARCHAR(255),
    PRIMARY KEY (model)
);

CREATE TABLE pc
(
    model VARCHAR(255) REFERENCES product (model),
    speed FLOAT,
    ram   FLOAT,
    disk  FLOAT,
    price FLOAT,
    PRIMARY KEY (model)
);
'''


import json
import psycopg2


def read_config():
    with open('config.json') as f:
        return json.load(f)


def connect_to_db():
    conn = psycopg2.connect(**read_config()['db'])
    conn.autocommit = False  # Disabling autocommit to enable transactions
    return conn, conn.cursor()


def find_pcs(speed, ram):
    with connect_to_db()[1] as cursor:
        query = 'SELECT model, speed, ram, disk, price FROM pc WHERE speed = %s AND ram = %s'
        cursor.execute(query, (speed, ram))
        records = cursor.fetchall()

        for model, speed, ram, disk, price in records:
            print(
                f'Model: {model}, Speed: {speed}, RAM: {ram}, Disk: {disk}, Price: {price}')


def model_exists(model_number, cursor):
    query = 'SELECT model FROM product WHERE model LIKE %s'
    cursor.execute(query, (model_number,))
    return cursor.fetchone()


def remove_pc(model_number):
    conn, cursor = connect_to_db()
    product = model_exists(model_number, cursor)
    if product:
        try:
            query = 'DELETE FROM product WHERE model = %s'
            cursor.execute(query, (model_number,))
            print(f'Deleted PC with model number {model_number}')
            conn.commit()  # Commit the transaction
        except:
            conn.rollback()  # Rollback the transaction on error
            print('Error deleting PC, transaction rolled back')
    else:
        print(f'PC with model number {model_number} does not exist')


def decrease_price(model_number):
    # TODO probably add a constraint to dont decrease the price below 0
    conn, cursor = connect_to_db()
    product = model_exists(model_number, cursor)
    if product:
        try:
            query = 'UPDATE pc SET price = price - 100 WHERE model = %s'
            cursor.execute(query, (model_number,))
            print(f'Decreased price of PC with model number {model_number}')
            conn.commit()  # Commit the transaction
        except:
            conn.rollback()  # Rollback the transaction on error
            print('Error decreasing price, transaction rolled back')
    else:
        print(f'PC with model number {model_number} does not exist')


def insert_pc(manufacturer, model_number, speed, ram, disk, price):
    conn, cursor = connect_to_db()
    product = model_exists(model_number, cursor)
    if product:
        print(f'PC with model number {model_number} already exists')
    else:
        try:
            query = 'INSERT INTO product VALUES (%s, %s, %s)'
            cursor.execute(query, (manufacturer, model_number, 'PC'))
            query = 'INSERT INTO pc VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(query, (model_number, speed, ram, disk, price))
            print(f'Inserted PC with model number {model_number}')
            conn.commit()  # Commit the transaction
        except:
            conn.rollback()  # Rollback the transaction on error
            print('Error inserting PC, transaction rolled back')


'''
if __name__ == "__main__":
    find_pcs(2.5, 8)
    # decrease_price('FakeModel')
    remove_pc('FakeModel')
    # insert_pc('FakeManufacturer', 'FakeModel', 2.5, 8, 100, 1000)
'''


if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Find PCs")
        print("2. Remove PC")
        print("3. Decrease Price")
        print("4. Insert PC")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            speed = float(input("Enter speed: "))
            ram = float(input("Enter RAM: "))
            find_pcs(speed, ram)
        elif choice == "2":
            model_number = input("Enter model number: ")
            remove_pc(model_number)
        elif choice == "3":
            model_number = input("Enter model number: ")
            decrease_price(model_number)
        elif choice == "4":
            manufacturer = input("Enter manufacturer: ")
            model_number = input("Enter model number: ")
            speed = float(input("Enter speed: "))
            ram = float(input("Enter RAM: "))
            disk = float(input("Enter disk size: "))
            price = float(input("Enter price: "))
            insert_pc(manufacturer, model_number, speed, ram, disk, price)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
