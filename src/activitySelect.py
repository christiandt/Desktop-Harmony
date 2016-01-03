from sys import exit
from controller import Controller
from PyQt4 import QtCore, QtGui

class ActivitySelect(QtGui.QDialog):

    def __init__(self, controller):
        super(ActivitySelect, self).__init__()

        self.controller = controller

        self.activities = dict()
        self.setActivities()
        
        title = "Desktop Harmony"
        self.setWindowTitle(str(title))
        self.resize(300, 380)

        self.layout = QtGui.QGridLayout(self)

        #listWidget
        self.list = QtGui.QListWidget()
        activityList = list(self.activities)
        self.list.addItems(activityList)
        self.list.setStyleSheet("font: 18pt")
        self.list.setSpacing(3)
        self.layout.addWidget(self.list, 1, 0, 1, 2)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Start")
        self.selectbutton.setStyleSheet("font: 15pt")
        self.selectbutton.setMinimumWidth(20)
        self.selectbutton.setMinimumHeight(50)
        self.layout.addWidget(self.selectbutton, 2, 0)
        QtCore.QObject.connect(self.selectbutton, QtCore.SIGNAL("clicked()"), self.activityStarted)

        #logoutbutton
        self.logoutbutton = QtGui.QPushButton(self)
        self.logoutbutton.setText("Log out")
        self.logoutbutton.setStyleSheet("font: 15pt")
        self.logoutbutton.setMinimumWidth(5)
        self.logoutbutton.setMinimumHeight(50)
        self.layout.addWidget(self.logoutbutton, 2, 1)
        QtCore.QObject.connect(self.logoutbutton, QtCore.SIGNAL("clicked()"), self.logOut)

        self.setLayout(self.layout)
        self.show()


    def setActivities(self):
        global activities
        for activity in self.controller.get_activities():
            self.activities[activity['label']] = activity['id']

    def activityStarted(self):
        activityID = int(self.activities[str(self.list.currentItem().text())])
        self.controller.start_activity(activityID)

    def logOut(self):
        self.controller.disconnect()
        exit(0)