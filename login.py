import requests


data = {
    "myurl": "http://portal.tku.edu.tw/aissinfo/emis/tmw0012.aspx",
    "ln": "zh_TW",
    "embed": "No",
    "logintype": "logineb",
    "username": "<學號>",
    "password": "<密碼>",
    "loginbtn": "登入"
}
s = requests.session()
s.post(url="https://sso.tku.edu.tw/NEAI/login2.do?action=EAI",data=data)
r = s.get("http://sso.tku.edu.tw/aissinfo/emis/TMWS030.aspx")
print(r.text)
