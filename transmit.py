import time
import serial

lora = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

message_count = 0  # Initialize message counter

while True:
    message_count += 1  # Increment message count for each new message
    message = f"Hello LoRa node, this is message {message_count}"  # Include count in the message
    b = bytes(message, 'utf-8')  # Convert message to bytes
    s = lora.write(b)  # Send the data to other lora
    print(f"Message {message_count} sent: {message}")  # Print the message with count
    time.sleep(0.2)  # Delay of 200ms


