from gpiozero import MCP3008
import time

# Create an MCP3008 object on channel 0 (CH0)
ldr = MCP3008(channel=1)

try:
    while True:
        print(f"Photoresistor Value {ldr.value}")
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user")

