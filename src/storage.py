from PyQt4.QtCore import QSettings

class Storage:

	def __init__(self):
		self.settings = QSettings('Christian Dancke Tuen', 'Desktop Harmony')

	def write_settings(self, username, password, ip, port):
		self.settings.setValue('username', str(username))
		self.settings.setValue('password', str(password))
		self.settings.setValue('ip', str(ip))
		self.settings.setValue('port', str(port))
		del self.settings

	def remove_settings(self):
		self.settings.clear()

	def read_settings(self):
		username = self.settings.value('username')
		password = self.settings.value('password')
		ip = self.settings.value('ip')
		port = self.settings.value('port')
		return username, password, ip, port

	def read_username(self):
		if self.settings.contains('username'):
			return str(self.settings.value('username', type=str))
		else:
			return ""

	def read_password(self):
		if self.settings.contains('password'):
			return str(self.settings.value('password', type=str))
		else:
			return ""

	def read_ip(self):
		if self.settings.contains('ip'):
			return str(self.settings.value('ip', type=str))
		else:
			return ""

	def read_port(self):
		if self.settings.contains('port'):
			return str(self.settings.value('port', type=str))
		else:
			return "5222"
