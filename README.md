# Central ICU Station Heart Rate Simulation

This project simulates a central ICU station for measuring and visualizing heart rates. It consists of a server with a local datastore and four clients. One client functions as a monitor to fetch and visualize data from the server, while the other three clients send heart rate data to the server. All components are connected through the local network using the network's IP address. The project is implemented with a Python client and a Node.js server.

## Purpose
Integration between various medical modalities is essential to
improve quality of healthcare. In ICU, medical personnel are overloaded, and
patients are in critical situation. One of the critical medical cases is
“Hypotension” (a case of decrease in blood pressure and increase in heart rate –
sometimes accompanied with sweating-), in this case, one of the physiological
parameters to indicate hypertension is the heart rate.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Screen Shots](#screenshots)



## Introduction

This project aims to simulate the functionality of a central ICU station by:

- Collecting heart rate data from multiple clients.
- Storing this data on a local server.
- Visualizing the data on a monitor client.

The setup mimics a real-world ICU environment where patient data is collected from various devices and displayed on a central monitor for medical personnel.

## Features

- **Multi-client setup:** Three clients can send heart rate data from any device (laptop or mobile) connected to the local network.
- **Data visualization:** One client fetches and visualizes the heart rate data from the server.
- **Local network communication:** All components communicate over the local network IP address.
- **Cross-platform compatibility:** Clients can run on different devices as long as they are connected to the same local network.

## Architecture

- **Server:** A Node.js application that stores and serves heart rate data.
- **Clients:**
  - **Monitor Client:** Fetches data from the server and visualizes it.
  - **Data Sending Clients:** Send heart rate data to the server.

### Diagram

```plaintext
  +-------------------+       +-------------------+
  |   Monitor Client  |<----->|      Server       |
  | (Visualization)   |       |   (Node.js)       |
  +-------------------+       +--------+----------+
                                   ^  ^  ^
                                   |  |  |
    +-------------------+          |  |  |
    |  Data Client 1    |----------+  |  |
    | (Python)          |             |  |
    +-------------------+             |  |
                                      |  |
    +-------------------+             |  |
    |  Data Client 2    |-------------+  |
    | (Python)          |                |
    +-------------------+                |
                                         |
    +-------------------+                |
    |  Data Client 3    |----------------+
    | (Python)          |
    +-------------------+
```
## Prerequisites
- Server:
     - Node.js (v14.x or later)
     - npm (v6.x or later)
     - Nodemon
- Clients:
     - Python (3.8 or later)
     - Required Python libraries (requests, pyqtgraph, PyQt5, etc.)

## Installation
1- clone the repository
```
git clone https://github.com/yusufafify/Central_ICU_Station.git
```
2- navigate to the server dir and install the dependencies
```
cd server
npm install
```
3- Start the server:
```
npm start
```
4- navigate to the client dir and create a virtual environment and activate it
- for windows:
```
python -m venv .venv
.venv\Scripts\activate
```
- for linux:
```
python3 -m venv .venv
source .venv/bin/activate
```
4- install the required libraries
```
pip install -r requirements.txt
```
## Screenshots
![Screenshot 2024-06-11 094802](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/6138d75a-10ae-46e7-8042-2ba5c0e5355a)
![Screenshot 2024-06-11 095010](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/ef183d83-724a-4f13-bb31-5e6bfe3bb812)
![Screenshot 2024-06-11 095029](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/2147bd59-7d08-4d5d-80ee-9e566bce30a4)
![Screenshot 2024-06-11 095048](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/3ac15288-bf57-47f5-bb35-4457a8258986)
![Screenshot 2024-06-11 095147](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/b806faf7-10a8-4cb3-bf00-8998ff84d3b9)
![Screenshot 2024-06-11 095218](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/bdcef4a7-436a-4633-a13b-92a23c0d48f7)
![Screenshot 2024-06-11 095243](https://github.com/yusufafify/Central_ICU_Station/assets/115397064/309216f1-7dbc-4a31-8bc0-d398302f8e53)

## Team Members:

| Name           | GitHub Username          |
|----------------|--------------------------|
| Youssef Afify       | [Youssef Afify](https://github.com/yusufafify)       |
| Youssef Awad  | [Youssef Awad](https://github.com/Youssef-Awad2004)     |
| Tarek Waleed  | [Tarek Waleed](https://github.com/Tarek-Waleed)     |
| Alia Tarek  | [Alia Tarek](https://github.com/aliatarek)     |
| Hamsa Saber | [Hamsa Saber](https://github.com/hamsasaber)     |
