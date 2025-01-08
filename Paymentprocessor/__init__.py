import logging
import json
import azure.functions as func
import pymysql

def main(event: func.EventGridEvent):
    logging.info('Processing event: %s', event.get_json())
    event_data = event.get_json()

    if 'payment_id' in event_data:
        process_payment(event_data)
    else:
        logging.error("Invalid event data: no payment_id found")
