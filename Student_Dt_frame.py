from PyQt5.QtWidgets import QApplication, QWidget 
import Beautiful_FCS as FCS


class Application(QWidget):

	def __init__(self):
		super().__init__()
		self.frame_ui()

	def frame_ui(self):
		self.resize(1024,768)
		self.setWindowTitle("主面板")
		self.show()