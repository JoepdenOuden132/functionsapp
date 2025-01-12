import logging
import json
import azure.functions as func


def main(event: func.EventGridEvent):
    logging.info('Processing event: %s', event.get_json())
    event_data = event.get_json()
    if 'payment_id' in event_data:
        process_payment(event_data)
    else:
        logging.error("Invalid event data: no payment_id found")


def process_payment(event_data):
    logging.info("Processing payment event data...")
    payment_id = event_data.get('payment_id')
    amount = event_data.get('amount')
    status = event_data.get('status')
    logging.info(f"Received payment data: Payment ID: {payment_id}, Amount: {amount}, Status: {status}")
    logging.info(f"Payment {payment_id} is being processed...")
    logging.info(f"Payment {payment_id} processed successfully.")