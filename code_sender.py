import time
import board
import busio

# Initialize UART on GP4 (TX) and GP5 (RX) at 9600 baud
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

number_to_send = 9


while True:
    # Convert number to string and add a newline character
    message = str(number_to_send) + "\n"
    # Encode string to bytes and transmit
    uart.write(bytes(message, "utf-8"))
    print("Sent:", number_to_send)
    time.sleep(2)
