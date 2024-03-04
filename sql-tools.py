import os
import time
import datetime
import requests
from googlesearch import search

class hacking:
    def __init__(self):
        self.date = datetime.datetime.now().strftime('%d %B %Y')
        self.github = 'https://github.com/sidabutar1337'
    def dork(self,query,number):
        for i in search(query,lang=id,num_results=number):
            print(i)
    def scan_vuln(self,target):
        try:
            exploit = f'{target}%27'
            response = requests.get(exploit)
            if response.status_code == 200:
                time.sleep(5)
                print('scanning!!')
                if 'error' in response.text.lower():
                    print(f'{target} vulnerable!!')
                    print('get hacking!!')
                else:
                    print(f'{target} tidak vulnerable!!')
                    print('try again!!')
            else:
                print('check koneksi internet anda!!') 
        except requests.exception.RequestException as e:
            print(f'error:{e}')
    def main(self):
        print('wait...')
        time.sleep(2)
        print("author tidak bertanggung jawab atas penyalahgunaan program hacking!!")
        time.sleep(3)
        open_github = os.system(f'{self.github}')
        print(open_github)
        print('=========HACKING=MENU==========')
        print('|1.Google Dork                |')
        print('|2.Scan SQL Injection         |')
        print('===============================')
        print('|Author:ZeusSec1337           |')
        print('|Github:sidabutar1337         |')
        print('===============================')
        try:
            calender = f'calender:{self.date}'
            print(calender)
            menu = int(input('pilih: '))
            if menu == 1:
                query = input('input dork: ')
                max_search = int(input('max: '))
                self.dork(query,max_search)
            elif menu == 2:
                url = input('input url: ')
                self.scan_vuln(url)
            else:
                print('pilihan tidak ada')
                return self.main()
        except ValueError:
            print('kesalahan karakter!!')
            return self.main()                                   
if __name__=='__main__':
    sidabutar1337 = hacking()
    sidabutar1337.main()                
            
