# Raspberry Pi Pico Oscilloscope

A USB oscilloscope built around the Raspberry Pi Pico (RP2040).

The oscilloscope measures bipolar DC and AC voltages using an
analog front-end consisting of an LM358 op-amp, voltage divider,
and level-shifting circuit.

Data is sampled by the Pico ADC and streamed to a PC for display
and analysis.

## Demo

<img width="539" height="403" alt="Screenshot 2026-06-28 at 12 27 44 AM" src="https://github.com/user-attachments/assets/6448ff41-f4bb-485f-a152-5a37cebbc47b" />


## Features

- Real-time waveform display
- Measures positive and negative voltages
- USB streaming to computer
- ~1 MΩ input impedance
- Analog front-end protection
- Open-source hardware and software

## Hardware Overview

The system consists of:

1. Raspberry Pi Pico
2. Analog front-end
3. USB communication interface
4. Display software

Input Signal
     │
     ▼
Voltage Divider
     │
     ▼
Level Shift Circuit
     │
     ▼
LM358 Buffer
     │
     ▼
Pico ADC
     │
     ▼
USB Streaming
     │
     ▼
Computer GUI

The voltage divider attenuates the input signal
to keep it within the ADC operating range.

A 2.4 V reference voltage is generated using
a resistor divider and buffered by an op-amp.

The reference voltage is combined with the
input signal to shift negative voltages into
the ADC measurement range.

The second LM358 stage is configured as a voltage
follower. It isolates the high-impedance divider
network from the Pico ADC.

The software uses the inverse transfer function
to convert ADC readings back to actual voltages.

## Schematic

<img width="2308" height="3264" alt="Schematics" src="https://github.com/user-attachments/assets/e9c20b28-e5c6-4485-9291-40fe4a69366c" />

<img width="4032" height="3024" alt="IMG_0681" src="https://github.com/user-attachments/assets/be430096-3143-4dec-b404-6580c4a98573" />


## Firmware

The Pico firmware:

1. Samples the ADC
2. Converts samples to digital values
3. Streams data over USB serial
4. Sends data to the PC application

git clone ...
cd firmware
...

## Signal Processing

ADC values are converted into voltages using:

Vin = (Vadc - 1.65)/0.284

The resulting waveform is plotted in real time.

## Calibration

1. Connect a known voltage source.
2. Measure the ADC reading.
3. Adjust software scaling constants.
4. Verify readings at ±5 V.

## Limitations

- Not isolated from USB ground.
- Maximum safe input approximately ±6 V.
- LM358 bandwidth limits high-frequency performance.
- ADC resolution limited to 12 bits.

## Future Work

- Switchable voltage ranges
- Input over-voltage protection
- Triggering system
- FFT spectrum analyzer
- External ADC
- Differential inputs
- Web-based interface

## Lessons Learned

This project required understanding:

- Voltage dividers
- Level shifting
- ADC operation
- Op-amp buffering
- USB communication
- Signal processing

The most important lesson was learning why
high-impedance measurement circuits require
buffer amplifiers before ADC sampling.
