import serial
import time

def main():
    # Setup the serial connection
    lora_serial = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    print("Starting LoRa Receiver...")
    message_count = 0  # Initialize message counter

    try:
        while True:
            # Process all available messages in the buffer
            while lora_serial.in_waiting > 0:
                data = lora_serial.readline()
                try:
                    # Decode bytes to string and strip newline characters
                    message = data.decode().strip()
                    print("Received message:", message)
                    message_count += 1  # Increment message count for each successful receive
                except UnicodeDecodeError:
                    print("Received an unreadable message")

            # Optional: very short sleep to prevent 100% CPU utilization, can be adjusted or removed
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Program terminated by user.")
        print(f"Total messages received: {message_count}")  # Display total message count on exit
    finally:
        lora_serial.close()
        print("Serial port closed.")
        print(f"Total messages received: {message_count}")  # Display total message count on exit

if __name__ == "__main__":
    main()
