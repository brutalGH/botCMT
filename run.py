import datetime,time,re
from datetime import datetime
import requests,json,random,rich,bs4,sys,os,time
from bs4 import BeautifulSoup
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol

x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'
ses = requests.Session()

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun)
jam = now.hour
menit = now.minute
detik = now.second
hari1 = now.strftime("%A")
date = str(hari1)+', '+str(tanggal)+'\n  • Jam '+str(jam)+' : '+str(menit)+' : '+str(detik)


def brut(u):
        for e in u :sys.stdout.write(e);sys.stdout.flush();time.sleep(0.02)

def banner():
	brut(f'{x}.....')
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	wel = '# BOT COMMENT TOOLS'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """
    
	pengembang1=nel(au,style="cyan")
	cetak(nel(pengembang1, title='v 3.144'))


#GENERATE TOKEN EAAB
def generate_token_eaag(cok): # Business Manager Token

    try:

        cookie = {'cookie':cok}

        with requests.Session() as xyz:

            url = 'https://business.facebook.com/business_locations'

            req = xyz.get(url,cookies=cookie)

            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')

            return(tok)

    except Exception as e:

        return('Cookies Invalid')
def atur():
	banner()
	pilih = input(f'{x} [ {h}• {x}] Comment Use Foto Y / T : ')
	banner()
	lah = input(f'{x} [ {h}• {x}] Input Jumlah Comment : ')
	tex = input(f'{x} [ {h}• {x}] Input Text comment   : ')
	tim = input(f'{x} [ {h}• {x}] Input Time Sleep     : ')
	ids = input(f'{x} [ {h}• {x}] Input Url            : ')
	if 'post' in ids:
		url = ids.split('/')[5]
		BOT(url,lah,tex,pilih,tim)

	if 'www' in ids:
		url = ids.split('/')[6]
		BOT(url,lah,tex,pilih,tim)

	elif 'photo.php' in ids:
		url = ids.split('/')[3].split('=')[1].replace('&id','')
		BOT(url,lah,tex,pilih,tim)

	elif 'fb://photo' in ids:
		url = ids.split('/')[3].split('?')[0]
		BOT(url,lah,tex,pilih,tim)

	elif 'videos' in ids:
		url = ids.split('/')[5]
		BOT(url,lah,tex,pilih,tim)

	elif 'groups' in ids:
		tok = ids.split('/')[4]
		tok1 = ids.split('/')[6]
		url = tok+'_'+tok1
		BOT(url,lah,tex,pilih,tim)
	else:
		print(f"{x} [ {m}• {x}] Belajar Lagi Tod")


	
###---[ LOGIN COOKIE ]---###
def login():
	banner()
	cookie = input(f"{x} [ {h}• {x}] Input Cookie : ")
	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
	find_token = re.search("(EAAG\w+)", data.text)
	ken=open("token.txt", "w").write(find_token.group(1))
	try:
		open('cookie.txt','w').write(cookie)
	except Exception as e:exit(f"{x} [ {m}• {x}] cookie invalid")


def BOT(url,lah,tex,pilih,tim):
	try:
		open('token.txt','r').read()
	except:
		login()
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	cook = {'cookie':cookie}
	url1 = url
	pesan = f'{tex}\n\n Comment Created On :\n  • '
	if 'y' in pilih:
		foto = input(f'{x} [ {h}• {x}] Input Url Foto       : ')
		for i in range(int(lah)):
			po = ses.post(f"https://graph.facebook.com/{url1}/comments/?&attachment_url={foto}&message={pesan}{date}&access_token={token}",cookies=cook).text
			if '{"id":' in po:
				print(f"{x} [ {h}• {x}] Send Comments Succes")
			elif 'Invalid' in po:
				print(f"{x} [ {m}• {x}] Terjadi Kesalahan, Login Ulang")
				time.sleep(5)
				login()
			else:
				print(f"{x} [ {m}• {x}] Send Comments Gagal")
			time.sleep(int(tim))
	else:
		for i in range(int(lah)):
			po = ses.post(f"https://graph.facebook.com/{url1}/comments/?&message={pesan}{date}&access_token={token}",cookies=cook).text
			if '{"id":' in po:
				print(f"{x} [ {h}• {x}] Send Comments Succes")
			elif 'Invalid' in po:
				print(f"{x} [ {m}• {x}] Terjadi Kesalahan, Login Ulang")
				time.sleep(5)
				login()
			else:
				print(f"{x} [ {m}• {x}] Send Comments Gagal")
			time.sleep(int(tim))

if __name__=='__main__':
	atur()