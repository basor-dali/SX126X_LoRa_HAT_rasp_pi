import serial
import time

def send_message_via_lora(serial_port, message):
    """Send a message via LoRa using the specified serial port."""
    # Append a newline character to the message
    message_with_newline = message + b'\n'
    serial_port.write(message_with_newline)
    print("Message sent via LoRa:", message_with_newline.hex())

def main():
    # Setup the serial connection to LoRa module
    lora_serial = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    # Hardcoded payload for RTCM Type 1005 message
    # This is a simplified example and may not represent actual valid RTCM data
    hardcoded_payload = bytes.fromhex('D300040E0001234C00000001567800000002ABCD0000')

    try:
        while True:
            # Send the hardcoded payload via LoRa
            send_message_via_lora(lora_serial, hardcoded_payload)

            # Wait for 0.2 seconds before sending the next message
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        lora_serial.close()
        print("Serial port closed.")

if __name__ == "__main__":
    main()
