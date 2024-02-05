import time
import serial

lora = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

message = "Hello LoRa node"  # Define your message here
b = bytes(message, 'utf-8')
message_count = 0  # Initialize the message counter

while True:
    s = lora.write(b)  # Send the data to other lora
    message_count += 1  # Increment the message count
    print(f"Message {message_count} sent: {message}")  # Include the message count in the print statement
    time.sleep(0.2)  # Delay of 200ms


