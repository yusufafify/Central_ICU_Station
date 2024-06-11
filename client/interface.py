from PyQt5 import QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
import functions
#from mplwidget import MplWidget
import pyqtgraph
#from classes import channelLine
import threading




def initConnectors(self):
   plot=self.findChild(pyqtgraph.PlotWidget,"Graph")
   plot2=self.findChild(pyqtgraph.PlotWidget,"Graph_2")
   plot3=self.findChild(pyqtgraph.PlotWidget,"Graph_3")
   value=self.findChild(QtWidgets.QLineEdit,"CurrentValue")
   value2=self.findChild(QtWidgets.QLineEdit,"CurrentValue_2")
   value3=self.findChild(QtWidgets.QLineEdit,"CurrentValue_3")
   status=self.findChild(QtWidgets.QLineEdit,"Status")
   status2=self.findChild(QtWidgets.QLineEdit,"Status_2")
   status3=self.findChild(QtWidgets.QLineEdit,"Status_3")


   plotref=plot.plot([0],[0])
   plotref2=plot2.plot([0],[0])
   plotref3=plot3.plot([0],[0])
   my_thread = threading.Thread(target=functions.getdataandplot, args=(plotref,plotref2,plotref3,value,value2,value3,status,status2,status3))

    # Start the thread
   my_thread.start()

   
   