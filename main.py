import machine
import utime

# Setup ADC on Pin 26
adc = machine.ADC(26)

# Your measured hardware circuit baseline (V)
offset = 1.62 

# Correct Pico ADC coefficient (3.3V reference / 65535 max 16-bit value)
coefficient = 3.3 / 65535

while True:
    raw = adc.read_u16()
    
    # Calculate the raw voltage input
    voltage = raw * coefficient
    
    # Alternative choice: If you want the web graph to center around 0V, 
    # you can uncomment the line below to subtract your hardware offset:
    # voltage = (raw * coefficient) - offset
    
    # Force a clean standard Unix newline character break for Web Serial API
    print(voltage, end='\n') 
    
    # 0.01s delay = 100Hz sampling rate
    utime.sleep(0.01)
