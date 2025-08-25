"""
This is the login module. It will open the login dialog!
"""


from PySide6.QtWidgets import QDialog
from ui.ui_logindialog import Ui_loginDialog

class LoginDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_loginDialog()
		self.ui.setupUi(self)

