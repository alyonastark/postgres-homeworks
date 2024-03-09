"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

#создаем соединение с базой данных
connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Miracle13/'
)

#прописываем пути к файлам
file_path_customers = os.path.join('north_data', 'customers_data.csv')
file_path_employees = os.path.join('north_data', 'employees_data.csv')
file_path_orders = os.path.join('north_data', 'orders_data.csv')

#Выполянем запросы к бд
try:
    with connect:
        with connect.cursor() as cursor:
            with open(file_path_customers, 'r', newline='', encoding='cp1251') as file:
                customers_data = csv.DictReader(file)
                for row in customers_data:
                    cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                   (row['customer_id'], row['company_name'], row['contact_name']))
            with open(file_path_employees, 'r', newline='', encoding='cp1251') as file:
                employees_data = csv.DictReader(file)
                for row in employees_data:
                    cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                   (row['employee_id'], row['first_name'],
                                    row['last_name'], row['title'],
                                    row['birth_date'], row['notes']))
            with open(file_path_orders, 'r', newline='', encoding='cp1251') as file:
                orders_data = csv.DictReader(file)
                for row in orders_data:
                    cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                   (row['order_id'], row['customer_id'], row['employee_id'],
                                    row['order_date'], row['ship_city']))
finally:
    connect.close()
