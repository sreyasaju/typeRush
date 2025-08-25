"""
This is the signup module. It will open the signup dialog!
"""


from PySide6.QtWidgets import QDialog
from ui.ui_registerdialog import Ui_registerDialog

class RegisterDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_registerDialog()
		self.ui.setupUi(self)
