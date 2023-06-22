import time
import random

print("CodingBy-Kamikaze Vip Panel")
print("\n")
key = "nMkKPreÜÜFALfsa"


keys = input("keyini gir : ")
print("\n")


if keys ==key:
    time.sleep(4)
    print("Giriş başarılı lütfen bekleyin..")
    time.sleep(3)
    print("""
 __      ___         _____  _  _              _ 
 \ \    / (_)       |  __ \| || |            | |
  \ \  / / _ _ __   | |__) | || |_ _ __   ___| |
   \ \/ / | | '_ \  |  ___/|__   _| '_ \ / _ \ |
    \  /  | | |_) | | |       | | | | | |  __/ |
     \/   |_| .__/  |_|       |_| |_| |_|\___|_|
            | |                                 
            |_|                                                          """)
    time.sleep(5)

    print("""1: ad sorgu
2: tc sorgu
3: adres sorgu
4: discord token sorgu
5: insta sorgu
""")
    secim = int(input("bir seçim yapın: "))
    
    if secim ==1:
        input("ad soyadı giriş: ")
        time.sleep(2)
        print("sorgulanıyor...")
        time.sleep(4)
        n = random.randint(1,3)
        
        
        if n ==1:
            print("hata 400 Http Error 400- Bad Request")
            time.sleep(1)
        elif n==2:
            print("Error : You dont have permission to acces on this server")
            time.sleep(1)
        elif n==3:
            print("errorCode")
            time.sleep(1)
    
    if secim ==2:
            input("tc giriş: ")
            time.sleep(2)
            print("sorgulanıyor...")
            time.sleep(4)
            n = random.randint(1,3)
            if n ==1:
                print("hata 400 Http Error 400- Bad Request")
                time.sleep(1)
            elif n==2:
                print("Error : You dont have permission to acces on this server")
                time.sleep(1)
            elif n==3:
                print("errorCode")
                time.sleep(1)

    if secim ==3:
        input("adres giriş: ")
        time.sleep(2)
        print("sorgulanıyor...")
        time.sleep(4)
        n = random.randint(1,3)
        if n ==1:
            print("hata 400 Http Error 400- Bad Request")
            time.sleep(1)
        elif n==2:
            print("v : You dont have permission to acces on this server")
            time.sleep(1)
        elif n==3:
            print("errorCode")
            time.sleep(1)

    if secim ==4:
        input("discord id giriş: ")
        time.sleep(2)
        print("sorgulanıyor...")
        time.sleep(4)
        n = random.randint(1,3)
        if n ==1:
            print("hata 400 Http Error 400- Bad Request")
            time.sleep(1)
        elif n==2:
            print("Error : You dont have permission to acces on this server")
            time.sleep(1)
        elif n==3:
            print("errorCode")
            time.sleep(1)

    if secim ==5:
        input("insta kullanıcı adı giriş: ")
        time.sleep(2)
        print("sorgulanıyor...")
        time.sleep(4)
        n = random.randint(1,3)
        if n ==1:
            print("hata 400 Http Error 400- Bad Request")
            time.sleep(1)
        elif n==2:
            print("Error : You dont have permission to acces on this server")
            time.sleep(1)
        elif n==3:
            print("errorCode")
            time.sleep(1)

else:
    print("yanlış key girişi!")
    time.sleep(1)
    
