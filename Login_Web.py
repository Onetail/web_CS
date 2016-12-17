import requests
import codecs
from bs4 import BeautifulSoup

def login_to_grade_inquiry(studentid, password):
    data = {
        "myurl": "http://portal.tku.edu.tw/aissinfo/emis/tmw0012.aspx",  # 登入成績網站
        "ln": "zh_TW",
        "embed": "No",
        "logintype": "logineb",
        "username": studentid,
        "password": password,
        "loginbtn": "登入"
    }
    s = requests.session()
    s.post(url="https://sso.tku.edu.tw/NEAI/login2.do?action=EAI", data=data)  # Post_url
    year = str(103)  # 暫設103年
    sem = str(1)  # 暫設第一學期
    url = "http://sso.tku.edu.tw/aissinfo/emis/TMWS030_result.aspx?yr=" + year + "&sem=" + sem + "&Quar=0"
    print(url)
    r = s.get(url)  # 需要顯示的url
    file = codecs.open("grade.html", "w", "utf-8")  # 暫存到grade.html
    file.write(r.text)