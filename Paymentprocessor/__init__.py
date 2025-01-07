import logging
import json
import azure.functions as func
import pymysql

def connect_to_db():
    return pymysql.connect(
        host='your-database-host',
        user='your-username',
        password='your-password',
        database='your-database'
    )

def process_payment(event_data):
    logging.info(f"Processing payment: {event_data}")

    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO payments (payment_id, amount, status, timestamp) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                event_data['payment_id'],
                event_data['amount'],
                event_data['status'],
                event_data['timestamp']
            ))
            connection.commit()
    finally:
        connection.close()

def main(event: func.EventGridEvent):
    logging.info('Processing event: %s', event.get_json())
    event_data = event.get_json()

    if 'payment_id' in event_data:
        process_payment(event_data)
    else:
        logging.error("Invalid event data: no payment_id found")