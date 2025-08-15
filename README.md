# About
## D2C
1. A device is registered in `Azure IoT Hub`.
2. authN via `X509`.
3. Messages in JSON are sent to the device usnig `azure.iot.device` package.
4. In `Azure IoT Hub`, `routing query` is used to filter the messages.
  -  Filtered  messages(messages that pass the  `routing query` condition) are **sent to** the `Azure service bus queue`.
  -  For the messages that fail the `routing query` condition, an `Azure Function` is  created **to read from** `Azure IoT Hub`(`Azure Event Hub` hosted internally to `AzureIoT Hub`).
# Auzre Resources Used
1. IoT Hub
2. Function App
3. Service Bus
# Next
1. Use `Azure Data Explorer`.
