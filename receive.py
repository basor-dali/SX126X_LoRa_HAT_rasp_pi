import serial

lora = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while True:
    if lora.in_waiting > 0:  # Check if data is available
        data_read = lora.readline()  # read data from LoRa
        print(data_read.decode().rstrip('\n'))  # Print the received message
