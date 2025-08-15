import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.function_name(name="TrgProcessFromIoTEventHub")
@app.event_hub_message_trigger(
    arg_name="events",
    event_hub_name="iothub-ehub-plan-a-iot-56088407-9d74b8dbb9",
    connection="IotHubConnection",
    cardinality="many",
    consumerGroup="$Default"
)
#def main(event: func.EventHubEvent):
#    for msg in event:
#        logging.info(f"Message: {msg.get_body().decode()}")

def main(events):
    for event in events:
        body = event.get_body().decode('utf-8')
        logging.info(f"Received message: {body}")