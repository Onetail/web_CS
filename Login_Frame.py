from PyQt5.QtWidgets import QShortcut,QLineEdit,QApplication,QLabel,QHBoxLayout,QVBoxLayout,QWidget,QPushButton,QComboBox
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
import Beautiful_FCS as FCS
import re
import Student_Dt_frame as sdf  # change application


class Application(QWidget):
	# close this application and new sdf
	close_signal = pyqtSignal()
	def __init__(self, parent = None):
		super(Application, self).__init__(parent)
		self.frame_ui()
		self.save()

	def frame_ui(self):
		self.resize(500,250)

		# label
		account = QLabel("學號", self)
		passwd = QLabel("密碼", self)

		account.setFont(FCS.Font_list[2])
		passwd.setFont(FCS.Font_list[2])

		# lineedit
		self.ac_line = QLineEdit()
		self.pw_line = QLineEdit()
		self.ac_line.setFont(FCS.Font_list[2])
		self.pw_line.setFont(FCS.Font_list[2])
		self.pw_line.setEchoMode(QLineEdit.Password)

		# button
		login_btn = QPushButton("登入", self)
		login_btn.clicked.connect(self.login_check)

		# combobox
		co_year = QComboBox()
		for i in range(1,7):
			co_year.addItem(str(i)+"年級")

		# event
		key_cz = QShortcut(QKeySequence("Ctrl+z"),self)
		key_cz.activated.connect(self.login_check)
		key_cw = QShortcut(QKeySequence("Ctrl+w"),self)
		key_cw.activated.connect(self.open_new_App)

		# layout
		ac_layout = QHBoxLayout()
		ac_layout.addStretch(1)
		ac_layout.addWidget(account)
		ac_layout.addWidget(self.ac_line)
		ac_layout.addStretch(1)
		
		pw_layout = QHBoxLayout()
		pw_layout.addStretch(1)
		pw_layout.addWidget(passwd)
		pw_layout.addWidget(self.pw_line)
		pw_layout.addStretch(1)

		choose_layout = QHBoxLayout()
		choose_layout.addStretch(1)
		choose_layout.addWidget(co_year)
		choose_layout.addStretch(1)
		
		bottomlayout = QHBoxLayout()
		bottomlayout.addStretch(1)
		bottomlayout.addWidget(login_btn)
		bottomlayout.addStretch(1)
		
		mainlayout = QVBoxLayout()
		mainlayout.addLayout(ac_layout)
		mainlayout.addLayout(pw_layout)
		mainlayout.addLayout(choose_layout)
		mainlayout.addLayout(bottomlayout)

		self.setLayout(mainlayout)
		self.setWindowTitle("Login")
		self.show()

	def login_check(self):
		# check account & passwd
		try:
			if re.search("^[\x30-\x39]{8,}$",self.ac_line.text()) != None :
				if re.search(r"^[\s\S]{6,}$",self.pw_line.text()) != None :
					self.setWindowTitle("學號: "+self.ac_line.text()+" 密碼: "+self.pw_line.text())
					
					# new Application
					self.open_new_App()

				else:
					self.pw_line.setText("")
					self.setWindowTitle("密碼錯誤!")
			else:
				self.setWindowTitle("帳號錯誤!")
				self.ac_line.setText("")
		except:
			print("\nerror")
			
	def save(self):
		return self.ac_line.text(), self.pw_line.text()
	def open_new_App(self):
		self.ui = sdf.Application()
		self.hide()
		self.close_signal.emit()
		self.close()
		self.ui.show()
