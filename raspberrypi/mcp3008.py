from gpiozero import MCP3008

# Create an MCP3008 object on channel 0 (CH0)
pot = MCP3008(channel=0)

try:
    while True:
        voltage = pot.value * 3.3  # Convert from ratio (0.0 to 1.0) to voltage
        print(f"Potentiometer Voltage: {voltage:.2f} V")

except KeyboardInterrupt:
    print("Stopped by user")

