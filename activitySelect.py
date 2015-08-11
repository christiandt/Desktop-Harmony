from sys import exit
from PyQt4 import QtCore, QtGui

class ActivitySelect(QtGui.QDialog):

    def __init__(self):
        super(ActivitySelect, self).__init__()

        self.activities = dict()
        self.setActivities()
        
        self.chats = dict()
        title = "Desktop Harmony"
        self.setWindowTitle(str(title))
        self.resize(300, 380)

        self.layout = QtGui.QGridLayout(self)

        #listWidget
        self.list = QtGui.QListWidget()
        activityList = list(self.activities)
        self.list.addItems(activityList)
        self.list.setStyleSheet("font: 25pt")
        self.list.setSpacing(3)
        self.layout.addWidget(self.list, 1, 0, 1, 2)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Start")
        self.selectbutton.setMinimumWidth(20)
        self.selectbutton.setMinimumHeight(50)
        self.layout.addWidget(self.selectbutton, 2, 0)
        QtCore.QObject.connect(self.selectbutton, QtCore.SIGNAL("clicked()"), self.activityStarted)

        #logoutbutton
        self.logoutbutton = QtGui.QPushButton(self)
        self.logoutbutton.setText("Log out")
        self.logoutbutton.setMinimumWidth(5)
        self.logoutbutton.setMinimumHeight(50)
        self.layout.addWidget(self.logoutbutton, 2, 1)
        QtCore.QObject.connect(self.logoutbutton, QtCore.SIGNAL("clicked()"), self.logOut)

        self.setLayout(self.layout)
        self.show()


    def setActivities(self):
        global activities
        self.activities = {"Watch TV":12345, "Play Games":12346, "Watch Movies":12347, "Watch AppleTV":12348, "Watch FireTV":12349, "Watch WDTV":12350, "SONOS":12351, "Power OFF":12352}

    def activityStarted(self):
        activityID = self.activities[str(self.list.currentItem().text())]
        print activityID

    def logOut(self):
        exit(0)