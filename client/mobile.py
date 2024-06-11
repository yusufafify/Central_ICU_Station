import requests
import random
import time

while True:
    # Generate a random number
    random_number = random.randint(50, 120)
    
    try:
        # Send the random number to the server
        # change ip address find address of network using ipconfig/all under LAN find IPv4 address take that place it in place of ip and leave 5000 this is the port
        requests.post('http://your network ip address and port number/data', json={'patientId': 'patient1', 'heartRate': random_number})
    except requests.exceptions.ConnectionError:
        print('Failed to connect to the server')
    print(random_number)
    time.sleep(1)