from azure.iot.device import IoTHubDeviceClient, Message, X509
import os
import time
import json
import random

print(os.getcwd())
print(os.listdir())

IOTHUB_HOSTNAME = "plan-a-iothub0.azure-devices.net"
DEVICE_ID = "first-device-self-signed"
x509 = X509(
    cert_file="/Users/parikshit/Tech/car/device.cert.pem",
    key_file="/Users/parikshit/Tech/car/device.key",
    pass_phrase=None
)

# SAS code
#cstr = "HostName=plan-a-iothub0.azure-devices.net;DeviceId=first-device-key-authN;SharedAccessKey=Q8f7UipckwrD+PlFxjP8ZT4NF6rnz1njE/PAIcx5epo="
#client = IoTHubDeviceClient.create_from_connection_string(cstr)

# X509 code
client = IoTHubDeviceClient.create_from_x509_certificate(
    x509 = x509,
    hostname = IOTHUB_HOSTNAME,
    device_id = DEVICE_ID
)

client.connect()
# for i in range(10):
#     msg = Message(f'{{"temp":{55+i}}}')
#     print(f"Sending message: {msg}")
#     client.send_message(msg)
#     time.sleep(2)
for i in range(10):
    temp = random.randint(50, 80)
    body = {
        "temperature":temp,
        "message_number":i
    }
    msg = Message(json.dumps(body))
    msg.custom_properties["temperature"] = str(temp)
    print(f"Sending message {i}: temp = {temp}")
    client.send_message(msg)
    time.sleep(2)
client.disconnect()
