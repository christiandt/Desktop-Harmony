from PyQt4 import QtCore, QtGui
from error import Error
from activitySelect import ActivitySelect

class UserPref(QtGui.QDialog):

    def __init__(self):
        super(UserPref, self).__init__()
        title = "Desktop Harmony - Preferences"
        self.setWindowTitle(str(title))
        self.resize(300, 50)

        self.layout = QtGui.QGridLayout(self)

        #username input
        self.userNameInput = QtGui.QLineEdit('', self)
        self.userNameInput.setStyleSheet("font: 20pt")
        self.userNameInput.setFixedHeight(30)
        self.layout.addWidget(self.userNameInput, 0, 1, 1, 2)
        userLabel = QtGui.QLabel('Username:')
        self.layout.addWidget(userLabel, 0, 0)

        #password input
        self.passwordInput = QtGui.QLineEdit('', self)
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordInput.setStyleSheet("font: 20pt")
        self.passwordInput.setFixedHeight(30)
        self.layout.addWidget(self.passwordInput, 1, 1, 1, 2)
        userLabel = QtGui.QLabel('Password:')
        self.layout.addWidget(userLabel, 1, 0)

        #Remember checkbox
        self.rememberBox = QtGui.QCheckBox()
        self.rememberBox.setChecked(True)
        self.layout.addWidget(self.rememberBox, 2, 1, 1, 1)
        rememberLabel = QtGui.QLabel('Remember:')
        self.layout.addWidget(rememberLabel, 2, 0)

        #OK buton
        self.okbutton = QtGui.QPushButton(self)
        self.okbutton.setText("OK")
        self.okbutton.setMinimumWidth(50)
        self.okbutton.setMinimumHeight(45)
        self.layout.addWidget(self.okbutton, 3, 1, 1, 1)
        QtCore.QObject.connect(self.okbutton, QtCore.SIGNAL("clicked()"), self.signIn)

        #Cancel buton
        self.cancelButton = QtGui.QPushButton(self)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setMinimumWidth(50)
        self.cancelButton.setMinimumHeight(45)
        self.layout.addWidget(self.cancelButton, 3, 2, 1, 1)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)

        self.setLayout(self.layout)


    def signIn(self):
        username = str(self.userNameInput.text())
        password = str(self.passwordInput.text())
        if True:
            self.activityWindow = ActivitySelect()
            self.accept()
        else:
            self.error = Error("Invalid UN or PW")

    def cancel(self):
        self.accept()

