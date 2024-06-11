from random import randint
import requests
import time
import winsound



patient=[]
patient2=[]
patient3=[]



def getdataandplot(graph1,graph2,graph3,value1,value2,value3,status1,status2,status3):
    global patient
    global patient2
    global patient3

    while True:
        try:
            response = requests.get('http://192.168.100.5:5000/data')
            response = response.json()

            patient=list(response['patient1'])
            patient2=list(response['patient2'])
            patient3=list(response['patient3'])

            value1.setText(str(patient[-1]))
            value2.setText(str(patient2[-1]))
            value3.setText(str(patient3[-1]))

            checkstatus(patient,graph1,status1)
            checkstatus(patient2,graph2,status2)
            checkstatus(patient3,graph3,status3)

            graph1.getViewBox().setXRange(min=0, max=max(patient))
            graph2.getViewBox().setXRange(min=0, max=max(patient2))
            graph3.getViewBox().setXRange(min=0, max=max(patient3))



        except Exception as e:
            print(e)

        time.sleep(1)





def checkstatus(array,plot,status):
    if array[-1]> 100 or array[-1] < 60:
        # Play an alarm sound
        plot.setData(list(range(len(array))), array, pen='r')  # Change the color of the graph to red
        status.setStyleSheet("background-color:red; color:black")
        status.setText("Danger")

        winsound.Beep(2500, 1000)

    elif array[-1]>80:
        plot.setData(list(range(len(array))), array, pen='y')  # Change the color of the graph to red
        status.setStyleSheet("background-color:yellow; color:black")
        status.setText("Warning")
    else:
        plot.setData(list(range(len(array))), array, pen='g')  # Change the color of the graph to green
        status.setStyleSheet("background-color:Green; color:black")
        status.setText("Safe")
