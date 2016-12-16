from PyQt5.QtWidgets import *
import Beautiful_FCS as FCS
import re


class Application(QWidget):
	
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

		# button
		login_btn = QPushButton("登入", self)
		login_btn.clicked.connect(self.login_check)

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
		
		bottomlayout = QHBoxLayout()
		bottomlayout.addStretch(1)
		bottomlayout.addWidget(login_btn)
		bottomlayout.addStretch(1)
		
		mainlayout = QVBoxLayout()
		mainlayout.addLayout(ac_layout)
		mainlayout.addLayout(pw_layout)
		mainlayout.addLayout(bottomlayout)

		self.setLayout(mainlayout)
		self.setWindowTitle("Login")
		self.show()

	def login_check(self):
		try:
			if re.search("^[\x30-\x39]{8,}$",self.ac_line.text()) != None :
				if re.search(r"^[\s\S]{6,}$",self.pw_line.text()) != None :
					self.setWindowTitle("學號: "+self.ac_line.text()+" 密碼: "+self.pw_line.text())
				else:
					self.setWindowTitle("密碼錯誤!")
			else:
				self.setWindowTitle("帳號錯誤!")
		except:
			print("\nerror")
			
	def save(self):
		return self.ac_line.text(), self.pw_line.text()
	