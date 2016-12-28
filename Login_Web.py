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
    gradeurl = 'http://sso.tku.edu.tw/aissinfo/emis/TMWS030.aspx'
    s.get(gradeurl, allow_redirects=False)
    url = "http://sso.tku.edu.tw/aissinfo/emis/TMWS030_result.aspx" # 進入最終爬蟲頁面
    data2 = {
        "yr": year,
        "sem": sem,
        "Quar": "0"
    }
    r = s.get(url, params=data2, allow_redirects=False)
    r.encoding = 'utf-8'
    content = BeautifulSoup(r.text, "lxml")
    print(content)
    file = codecs.open("grade.html", "w", "utf-8")  # 暫存到grade.html
    file.write(r.text)