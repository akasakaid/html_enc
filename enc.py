try:
    import requests,os,sys
    from requests.exceptions import *
    from bs4 import BeautifulSoup as bs
except ImportError:exit('module not installed\nsend command\npip3 install -r requirements.txt')

r = requests.Session()
url1 = 'https://www.smartgb.com/free_encrypthtml.php?do=crypt'
url2 = 'https://www.smartgb.com/free_encrypthtml.php'

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

def enc(file):
    try:
        a = r.get(url2,headers=headers).text
        b = bs(a,'html.parser')
        ch = b.find('input',attrs={'type':'hidden','name':'ch'})['value']
        data = {'h':file,'s':'extended','ch':ch,'Skicka':'Encrypt HTML'}
        c = r.post(url1,headers=headers,data=data)
        d = bs(c.text,'html.parser')
        ot = d.find('form').text
        with open('result.html','w') as hs:
            hs.write(str(ot))
        print('complete ^-^')
        print('saved as result.html')
    except ConnectionError:exit('connection error !!')
    except KeyboardInterrupt:exit()
    except Exception as e:exit('error :',e)

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('HTML ENCRYPTER'.center(30))
    print('POWERED : SMARTGB.COM'.center(30))
    print('AkasakaID'.center(30))
    print('Black Coder Crush'.center(30))
    print(' ')
    nenen = input('input html file name >>> ')
    op = open(nenen).read()
    enc(op)
except FileNotFoundError:exit(f'\nfile {nenen} not found')
