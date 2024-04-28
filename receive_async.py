import asyncio
import serial_asyncio
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def read_serial(loop):
    try:
        # Attempt to open the serial connection
        reader, _ = await serial_asyncio.open_serial_connection(url='/dev/ttyAMA0', baudrate=9600)
        logging.info("Serial connection opened.")
        
        while True:
            try:
                # Read data until a newline character is found
                data = await reader.readuntil(b'\n')
                # Decode the data
                message = data.decode().strip()
                logging.info(f"Received message: {message}")
            except asyncio.IncompleteReadError:
                logging.error("Incomplete read from serial port, possible data corruption or connection issue.")
            except UnicodeDecodeError:
                logging.error("Error decoding message, data might be corrupted.")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {str(e)}")
                break  # Exit the loop on unexpected errors

    except serial_asyncio.serial.SerialException as e:
        logging.critical(f"Serial connection could not be established: {str(e)}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred during setup: {str(e)}")

async def main():
    loop = asyncio.get_event_loop()
    try:
        await read_serial(loop)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    finally:
        loop.close()
        logging.info("Event loop closed.")

if __name__ == "__main__":
    asyncio.run(main())
