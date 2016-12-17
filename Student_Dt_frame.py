from PyQt5.QtWidgets import QApplication, QWidget , QPushButton , QLabel, QHBoxLayout,QVBoxLayout
import Beautiful_FCS as FCS
import time

class Application(QWidget):

	def __init__(self):
		super().__init__()
		self.frame_ui()

	def frame_ui(self):

		self.resize(1024,768)
		self.setWindowTitle("主面板")

		# label
		account_label = QLabel("學號",self)
		passwd_label = QLabel("密碼",self)
		get_value = QLabel("已得學分",self)
		time = QLabel(self.time_now(),self)

		# button
		# layout
		toplayout = QHBoxLayout()
		centerlayout = QVBoxLayout()
		bottomlayout = QHBoxLayout()

		toplayout.addWidget(time)
		centerlayout.addWidget(account_label)
		centerlayout.addWidget(passwd_label)
		centerlayout.addWidget(get_value)
		mainlayout = QVBoxLayout()
		mainlayout.addLayout(toplayout)
		mainlayout.addLayout(centerlayout)
		mainlayout.addLayout(bottomlayout)
		self.setLayout(mainlayout)
		# show
		self.show()

	def time_now(self):
		stime = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
		return stime