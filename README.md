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
git clone
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
