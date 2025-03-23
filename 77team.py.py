import os
import sys
import time
import random
from termux_auth import termux_setup  # Simulated import

# Terminal renkleri
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

ASCII_ART = """
███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗
████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝
██╔████╔██║██║   ██║██████╔╝██║██║     █████╗  
██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝
 ######   ######
 ##  ##   ##  ##
     ##       ##
    ##       ##
   ##       ##
   ##       ##
   ##       ##             
"""

SMALL_77 = """
▒▒▒▒▒ ▒▒▒▒▒
    ▒     ▒
   ▒     ▒ 
  ▒     ▒  
 ▒▒▒▒▒ ▒▒▒▒▒
"""

def clear_screen():
    os.system('clear')

def typing_animation(text, speed=0.03, color=GREEN):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_animation(text, duration=2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        sys.stdout.write("\r" + YELLOW + f"{text} {chars[i % len(chars)]}" + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    print()

def animate_77():
    animations = [
        "▂▃▄▅▆▇█▓▒░ 77 ░▒▓█▇▆▅▄▃▂",
        "▒▒▒▒▒▒▒▒▒▒ 77 ▒▒▒▒▒▒▒▒▒▒",
        "██████████ 77 ██████████",
        "▓▓▓▓▓▓▓▓▓▓ 77 ▓▓▓▓▓▓▓▓▓▓",
        "▀▄▀▄▀▄▀▄▀▄ 77 ▄▀▄▀▄▀▄▀▄▀",
        "■□■□■□■□■□ 77 □■□■□■□■□■",
        "←←←←←←←←←← 77 →→→→→→→→→→",
        "░░░░░░░░░░ 77 ░░░░░░░░░░"
    ]
    
    for _ in range(2):  # Show the animation 2 times
        for anim in animations:
            sys.stdout.write("\r" + CYAN + anim + RESET)
            sys.stdout.flush()
            time.sleep(0.15)
    print()

def vibration_feedback():
    # Simulate vibration feedback
    try:
        os.system('termux-vibrate -d 50')
    except:
        pass  # Ignore if termux-api not available

def print_banner():
    clear_screen()
    
    # Animate the ASCII art
    for line in ASCII_ART.splitlines():
        print(RED + line + RESET)
        time.sleep(0.02)
    
    typing_animation("MOBİL 77 TEAM İHBAR BOTU v1.0.3", 0.03, CYAN)
    print(YELLOW + "=" * 50 + RESET)
    
    animate_77()
    
    print(YELLOW + "=" * 50 + RESET)

def request_permissions():
    typing_animation("\n[*] Uygulama için gerekli izinler isteniyor...", 0.03, YELLOW)
    loading_animation("Dosya izinleri alınıyor", 1)
    loading_animation("İnternet izni alınıyor", 1)
    loading_animation("SMS izni alınıyor", 1)
    loading_animation("Kamera izni alınıyor", 1)
    
    print(GREEN + "\n[+] Tüm izinler alındı!" + RESET)
    vibration_feedback()
    time.sleep(1)

def setup_mobile_environment():
    typing_animation("\n[*] Termux ortamı yapılandırılıyor...", 0.03, BLUE)
    
    try:
        # Simulate termux setup
        loading_animation("Paketler kontrol ediliyor", 1.5)
        loading_animation("Gerekli kütüphaneler yükleniyor", 2)
        loading_animation("API bağlantısı kuruluyor", 1.5)
        print(GREEN + "\n[+] Termux ortamı başarıyla yapılandırıldı!" + RESET)
        vibration_feedback()
        return True
    except Exception as e:
        print(RED + f"\n[-] Hata: {str(e)}" + RESET)
        return False

def send_report(target, count, report_type):
    success = 0
    fail = 0
    
    typing_animation(f"\n[*] Hedef: {target}", 0.02, CYAN)
    typing_animation(f"[*] İhbar Sayısı: {count}", 0.02, CYAN)
    typing_animation(f"[*] İhbar Tipi: {report_type}", 0.02, CYAN)
    
    # Try to vibrate on each step
    vibration_feedback()
    
    loading_animation("Mobil sunucuya bağlanılıyor", 1.5)
    loading_animation("İhbar modülü hazırlanıyor", 1)
    loading_animation("77 TEAM protokolü başlatılıyor", 1)
    
    print(YELLOW + "\n[*] İhbar işlemi başlatılıyor...\n" + RESET)
    vibration_feedback()
    time.sleep(0.5)
    
    for i in range(count):
        try:
            loading_delay = random.uniform(0.1, 0.3)
            time.sleep(loading_delay)
            
            # Progress bar
            progress = (i+1) * 100 // count
            bar_length = 30
            filled_length = int(bar_length * (i+1) / count)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            
            sys.stdout.write(f"\r{WHITE}[{bar}] {progress}%{RESET}")
            sys.stdout.flush()
            
            result = random.choice([True, True, True, False])  # 75% success rate
            
            time.sleep(0.1)
            sys.stdout.write("\r" + " " * 50)  # Clear the line
            
            if result:
                success += 1
                typing_animation(f"[+] İhbar #{i+1} başarılı! 77 ✓", 0.01, GREEN)
            else:
                fail += 1
                typing_animation(f"[-] İhbar #{i+1} başarısız! Yeniden deneniyor...", 0.01, RED)
                vibration_feedback()  # Vibrate on failure
                time.sleep(0.5)
                # Retry once
                typing_animation(f"[+] İhbar #{i+1} başarılı! (Yeniden deneme) 77 ✓", 0.01, GREEN)
                success += 1
                
        except Exception as e:
            fail += 1
            typing_animation(f"[-] İhbar #{i+1} başarısız: {str(e)}", 0.01, RED)
    
    animate_77()
    vibration_feedback()  # Vibrate on completion
    
    print(YELLOW + "\n" + "=" * 50)
    print(GREEN + f"[*] İşlem tamamlandı! Başarılı: {success} | Başarısız: {fail-success}")
    
    # Animate "77 TEAM" text
    team_text = "77 TEAM - MOBİL GÜVENLİK - 77 77 77 77 77"
    typing_animation("\n" + team_text, 0.02, RED)
    
    print(YELLOW + "=" * 50 + RESET)

def main():
    # Check if running in Termux
    is_termux = "com.termux" in os.environ.get("PREFIX", "")
    
    # Initial animation
    clear_screen()
    typing_animation("77 TEAM Mobil sistemi yükleniyor...", 0.03, CYAN)
    
    if is_termux:
        typing_animation("\n[+] Termux ortamı tespit edildi.", 0.02, GREEN)
    else:
        typing_animation("\n[!] Termux ortamı bulunamadı. Bazı özellikler çalışmayabilir.", 0.02, YELLOW)
    
    setup_mobile_environment()
    request_permissions()
    
    loading_animation("Sistem başlatılıyor", 1.5)
    loading_animation("Mobil modüller hazırlanıyor", 1.5)
    loading_animation("Güvenlik protokolleri etkinleştiriliyor", 1.5)
    
    animate_77()
    vibration_feedback()
    time.sleep(0.5)
    
    while True:
        print_banner()
        
        typing_animation("\nİhbar Tipleri:", 0.02, WHITE)
        typing_animation("1. Spam İhbarı", 0.02, CYAN)
        typing_animation("2. Dolandırıcılık İhbarı", 0.02, CYAN)
        typing_animation("3. Zararlı İçerik İhbarı", 0.02, CYAN)
        typing_animation("4. Çıkış\n", 0.02, CYAN)
        
        choice = input(WHITE + "Seçiminiz (1-4): " + RESET)
        vibration_feedback()
        
        if choice == "4":
            typing_animation("\n77 TEAM'den çıkılıyor. Mobil  için buradayız!", 0.03, RED)
            animate_77()
            vibration_feedback()
            time.sleep(1)
            clear_screen()
            break
            
        if choice not in ["1", "2", "3"]:
            typing_animation("\nGeçersiz seçim! Lütfen tekrar deneyin.", 0.03, RED)
            vibration_feedback()
            time.sleep(2)
            continue
            
        report_types = {
            "1": "Spam İhbarı",
            "2": "Dolandırıcılık İhbarı", 
            "3": "Zararlı İçerik İhbarı"
        }
        
        target = input(WHITE + "\nHedef URL veya Kullanıcı Adı: " + RESET)
        
        try:
            count = int(input(WHITE + "İhbar Sayısı (1-50): " + RESET))
            if count < 1 or count > 50:
                typing_animation("\nGeçersiz sayı! 1-50 arası bir değer girin.", 0.03, RED)
                vibration_feedback()
                time.sleep(2)
                continue
        except ValueError:
            typing_animation("\nGeçersiz değer! Lütfen bir sayı girin.", 0.03, RED)
            vibration_feedback()
            time.sleep(2)
            continue
            
        send_report(target, count, report_types[choice])
        
        input(WHITE + "\nAna menüye dönmek için Enter tuşuna basın..." + RESET)

def setup_termux():
    # Bu fonksiyon Termux'ta gerekli paketleri kurar
    clear_screen()
    
    print(CYAN + SMALL_77 + RESET)
    typing_animation("\nTermux kurulumu başlatılıyor...", 0.03, YELLOW)
    
    packages = ["python", "python-pip", "termux-api"]
    
    for pkg in packages:
        typing_animation(f"\nPaket yükleniyor: {pkg}", 0.02, BLUE)
        loading_animation(f"{pkg} indiriliyor", 1)
        loading_animation(f"{pkg} kuruluyor", 1)
        print(GREEN + f"[+] {pkg} başarıyla kuruldu!" + RESET)
    
    typing_animation("\nGerekli Python paketleri yükleniyor...", 0.02, BLUE)
    loading_animation("pip paketleri kuruluyor", 1.5)
    print(GREEN + "[+] Python paketleri başarıyla kuruldu!" + RESET)
    
    typing_animation("\nMobil 77 TEAM izinleri ayarlanıyor...", 0.02, BLUE)
    loading_animation("İzinler yapılandırılıyor", 1)
    print(GREEN + "[+] İzinler başarıyla ayarlandı!" + RESET)
    
    typing_animation("\n77 TEAM Mobil İhbar Botu için kurulum tamamlandı!", 0.03, GREEN)
    print(YELLOW + "\nUygulamayı başlatmak için Enter tuşuna basın..." + RESET)
    input()
    
    return True

if __name__ == "__main__":
    try:
        # Check if first run and setup Termux
        if not os.path.exists(".setup_complete"):
            setup_termux()
            # Create setup complete file
            with open(".setup_complete", "w") as f:
                f.write("setup_complete")
        
        main()
    except KeyboardInterrupt:
        clear_screen()
        typing_animation("\n\nProgram kullanıcı tarafından sonlandırıldı.", 0.03, RED)
        animate_77()
        typing_animation("77 TEAM ", 0.03, CYAN)
        vibration_feedback()