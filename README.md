# IoT-Based-Gas-Level-Monitoring-System
IoT Gas Level & Leakage Monitor using Blynk 🚀
An IoT-based solution to monitor LPG cylinder levels in real-time, detect gas leaks, and receive instant alerts on your smartphone using the Blynk IoT platform.

📝 Overview
This project solves two common household problems: unexpectedly running out of cooking gas and the potential danger of gas leaks. By using an ultrasonic sensor to measure the gas level and an MQ-2 sensor for leak detection, the system provides real-time data directly to a custom dashboard on the Blynk app.

The raspberry pico w microcontroller acts as the brain, processing sensor data and using its built-in Wi-Fi to communicate with the Blynk Cloud. This ensures you are always informed, whether you're at home or away.

✨ Key Features
📊 Real-Time Level Monitoring: View the current gas percentage on a gauge in the Blynk app.

⚠️ Low-Level Alerts: Receive an instant push notification when the gas level drops below a preset threshold (e.g., 20%).

🚨 Gas Leakage Detection: An MQ-2 sensor detects dangerous gases like LPG and methane, triggering an immediate alert.

📱 Remote Access: Monitor your cylinder from anywhere in the world through the Blynk app.

⚙️ Simple Setup: Built with common, low-cost hardware and easy-to-configure software.

🛠️ Hardware & Software
Hardware Required
Microcontroller: raspberry pico w
Here’s a list of the Raspberry Pi Pico W main specs:

1) RP2040 microcontroller with 2MB flash
2) CPU: Dual-core Arm Cortex-M0+ at 133MHz
3) 264kB multi-bank high-performance SRAM
4) 2MB onboard QSPI Flash
5) 2.4GHz wireless interfaces (802.11n) using the Infineon CYW43439 (on the W models)
6) Micro-USB B port (for power and programming)
7) 3-pin ARM Serial Wire Debug (SWD) port
8) 40 pins

Leakage Sensor: MQ-2 Gas Sensor Module

Connectivity: Jumper Wires, Breadboard

Power: Micro-USB Cable

Software Required
Thonny IDE: To program the raspberry pico w.

Blynk App: For the user interface and notifications (available on iOS and Android).

Libraries: Blynk Library for Arduino.
