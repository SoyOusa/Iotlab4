# Iotlab4 : ESP32 → MQTT → Node-RED → InfluxDB → Grafana Dashboard

# 🌡️ Lab: IoT Environmental Monitoring with ESP32 and BMP280
# 📘 Overview

This lab demonstrates how to build an IoT-based environmental monitoring system using an ESP32 microcontroller and a BMP280 sensor. The ESP32 reads temperature, pressure, and altitude data from the BMP280 sensor and publishes it via MQTT. The data is then collected by Node-RED, stored in InfluxDB, and visualized in real-time on a Grafana dashboard. This lab introduces the complete IoT data pipeline from sensor to visualization.

# 🎯 Objectives

By the end of this lab, you will be able to:

_Connect and configure a BMP280 sensor with an ESP32 using I2C.

_Publish sensor data to an MQTT broker.

_Set up Node-RED to subscribe to MQTT messages and forward data to InfluxDB.

_Store sensor data in InfluxDB for time-series analysis.

_Visualize the data in Grafana dashboards in real-time.

_Understand the complete IoT data flow from sensing to visualization.

# ⚙️ Detailed Explanation

1. ESP32 + BMP280:
The ESP32 reads temperature, pressure, and altitude from the BMP280 sensor over I2C.

2. MQTT Communication:
The ESP32 publishes data as JSON messages to a specified MQTT topic on a broker (test.mosquitto.org).

3. Node-RED Integration:
Node-RED subscribes to the MQTT topic, parses the JSON, and sends it to InfluxDB.

4. InfluxDB Storage:
InfluxDB stores the sensor readings as time-series data, enabling historical analysis and querying.

5. Grafana Dashboard:
Grafana connects to InfluxDB to visualize temperature, pressure, and altitude in real-time charts and graphs.

# Wiring Photo:
![BMP280_wire](https://github.com/user-attachments/assets/09ccee94-089c-4e05-97ac-4f20a70bcf83)

# Video Link:
https://youtu.be/kjQOxmatHuw?si=6wRx77SUOjmgIGeS
