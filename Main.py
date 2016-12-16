import Login_Frame
import sys
import Login_Web

app = Login_Frame.QApplication(sys.argv)
login = Login_Frame.Application()
app.exec_()
studentid, password = login.save()
Login_Web.login_to_grade_inquiry(studentid, password)
