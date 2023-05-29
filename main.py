from CryptoPriceX import *

banner = """        
       ______                     __          ____         _             _  __        
      / ____/_____ __  __ ____   / /_ ____   / __ \ _____ (_)_____ ___  | |/ /        
     / /    / ___// / / // __ \ / __// __ \ / /_/ // ___// // ___// _ \ |   /         
    / /___ / /   / /_/ // /_/ // /_ / /_/ // ____// /   / // /__ /  __//   |          
    \____//_/    \__, // .___/ \__/ \____//_/    /_/   /_/ \___/ \___//_/|_|          
                /____//_/                                                                         
                                                                                                                      
_________________________________________________________________________________
-------------------------------- [CryptoPriceX] ---------------------------------
    Request the price of the crypto you want with the currency pair you want !

 © Valmar Corporation - Jpiix Underground Corporation - 2023         Version 2.2
---------------------------------------------------------------------------------
"""


# ~~~~~~~~~~~ Main ~~~~~~~~~~~ #

def main():
    print(banner)
    
    time.sleep(1)
    print("\n# ~~~~~~~~~~~~~~ Crypto Monnaies ~~~~~~~~~~~~~~~ #")
    for sigle, nom in cryptos.items():
        print(  sigle + " - " + nom)
    print("# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #")
    
    print("\n# ~~~~~~~~~~~~ Fiduciaires Monnaies ~~~~~~~~~~~~ #")
    for sigle, nom in fiduciaires.items():
        print(  sigle + " - " + nom)
    print("# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #")
    
    time.sleep(1)
    crypto = input("\n[default:BTC]   Which crypto do you want ? ")
    if crypto == "":
        crypto = "BTC"
    else:
        crypto = crypto.upper()
    while crypto not in ["BTC", "ETH", "LTC", "BCH", "ADA", "XLM", "DOGE", "EOS"]:
        print("Please enter a valid crypto : BTC, ETH or LTC...")
        crypto = input("\n[default:BTC]   Which crypto do you want ? ")
        if crypto == "":
            crypto = "BTC"
        else:
            crypto = crypto.upper()
    
    monnaie = input("[default:EUR]   Which currency pair do you want ? ")
    if monnaie == "":
        monnaie = "EUR"
    else:
        monnaie = monnaie.upper()
    while monnaie not in ["USDT", "EUR", "GBP", "AUD", "BRL"]:
        print("Please enter a valid currency pair : EUR, USD or GBP...")
        monnaie = input("\n[default:EUR]   Which currency pair do you want ? ")
        if monnaie == "":
            monnaie = "EUR"
        else:
            monnaie = monnaie.upper()
        
    print("\nSearching... check the price of " + crypto + " in " + monnaie + " !")
    res = request(url + crypto + monnaie)
    
    print("\n# ~~~~~~~~~~~~~~~ Result ~~~~~~~~~~~~~~~ #")
    print("   result : 1", crypto,"=",res,monnaie,)
    print("# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #\n")
    
    time.sleep(1)
    choice = input("\nDo you want to continue ? [Y/N] ").upper()
    if choice == "Y":
        clear()
        time.sleep(1)
        main()
    elif choice == "N":
        print("\nGoodbye !")
        time.sleep(2)
        clear()
        exit()
    else:
        while choice not in ["Y", "N"]:
            print("Please enter a valid choice : Y or N...")
            choice = input("\nDo you want to continue ? [Y/N] ").upper()
            if choice == "Y":
                clear()
                time.sleep(1)
                main()
            elif choice == "N":
                print("\nGoodbye !")
                time.sleep(2)
                clear() 
                exit()               
                
if __name__ == "__main__":
    main()