import time
import serial

lora = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

message = "Hello LoRa node"  # Default msg to be published
b = bytes(message, 'utf-8')

while True:
    s = lora.write(b)  # Send the data to other lora
    print("Message sent:", message)
    time.sleep(0.2)  # Delay of 200ms

