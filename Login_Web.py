import requests


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
    s.post(url="https://sso.tku.edu.tw/NEAI/login2.do?action=EAI", data=data) # Post_url
    r = s.get("http://sso.tku.edu.tw/aissinfo/emis/TMWS030.aspx") # 需要顯示的url
    print(r.text)
