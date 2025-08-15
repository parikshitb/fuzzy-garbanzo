import logging
import json

def main(event_foo: list):
    for msg in event:
        try:
            payload = json.loads(msg)
            logging.info(f"Received fallback IoT message: {payload}")
        except Exception as e:
            logging.warning(f"Raw message: {msg}, error: {e}")
            
    