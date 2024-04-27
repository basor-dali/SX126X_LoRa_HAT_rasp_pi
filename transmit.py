import serial
import struct
import time

def generate_rtcm_type_1005_payload():
    # Example data for RTCM Type 1005 message
    station_id = 1234
    itrf_year = 13  # Last two digits
    flags = 0b1011  # GPS, Galileo active, Reference Station Indicator active
    x = int(3650728.49 * 10000)
    y = int(1400891.95 * 10000)
    z = int(5000000.00 * 10000)

    # Pack data into bytes
    # Note: Adjust the format string as per the actual bit lengths and order
    payload = struct.pack('>HBBBIIIBIIBII', 0xD300, station_id, itrf_year, flags, x, 0, y, 0, z, 0)
    return payload

def send_message_via_lora(serial_port, message):
    """Send a message via LoRa using the specified serial port."""
    serial_port.write(message)
    print("Message sent via LoRa:", ' '.join(f'{byte:02X}' for byte in message))

def main():
    # Setup the serial connection to LoRa module
    lora_serial = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    try:
        while True:
            # Generate RTCM Type 1005 payload
            rtcm_payload = generate_rtcm_type_1005_payload()

            # Send the payload via LoRa
            send_message_via_lora(lora_serial, rtcm_payload)

            # Wait for 0.2 seconds before sending the next message
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        lora_serial.close()
        print("Serial port closed.")

if __name__ == "__main__":
    main()


