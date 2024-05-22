import serial
import os

# Define serial port settings
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Adjust the port based on your setup
    baudrate=9600,         # Adjust baud rate if needed
    timeout=1              # Set timeout to prevent blocking indefinitely
)

# Define file path
file_path = 'received_data.txt'

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    open(file_path, 'a').close()

# Open the file in append mode
with open(file_path, 'a') as file:
    while True:
        # Read data from serial port
        data = ser.readline().decode('utf-8').strip()
        
        # Print received data to console
        print("Received data:", data)

        # If data is received, append it to the file
        if data:
            # Write data to file
            file.write(data + '\n')
            file.flush()  # Flush the buffer to ensure immediate write to the file
