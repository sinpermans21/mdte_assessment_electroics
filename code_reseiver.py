import time
import board
import busio
import neopixel
import list_nums  # Imports your custom segment mapping script

# Configure your NeoPixel Strip on GP14
PIXEL_PIN = board.GP14
NUM_PIXELS = 25   # Adjust this if you have multiple digits chained together
BRIGHTNESS = 0.3  # Set brightness level (0.0 to 1.0)

# Initialize the NeoPixel strip object
pixels = neopixel.NeoPixel(
    PIXEL_PIN, 
    NUM_PIXELS, 
    brightness=BRIGHTNESS, 
    auto_write=False  # list_nums explicitly handles pixels.show()
)

# Initialize UART on GP0 (TX) and GP1 (RX) at 9600 baud
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# Clear the display immediately at startup
list_nums.clear(pixels)
pixels.show()

print("System Initialized. Awaiting UART data...")

while True:
    # Simulate occasional listening by waiting 5 seconds
    time.sleep(5)
    
    # Check how many bytes are waiting in the buffer
    bytes_waiting = uart.in_waiting
    if bytes_waiting > 0:
        # Read absolutely everything currently in the buffer
        raw_data = uart.read(bytes_waiting)
        try:
            # Decode bytes to text
            text_data = raw_data.decode("utf-8")
            
            # Split the text by newline and filter out empty strings
            lines = [line for line in text_data.split("\n") if line.strip()]
            
            if lines:
                # Grab the very last element in the list (the newest transmission)
                latest_number = lines[-1].strip()
                print("Latest Received:", latest_number)
                
                # Update the NeoPixel display using your list_nums logic
                
                list_nums.draw_number(pixels, latest_number, color=(255, 0, 0)) 
                
        except Exception as e:
            print("Decoding error:", e)
    else:
        print("No data waiting.")
