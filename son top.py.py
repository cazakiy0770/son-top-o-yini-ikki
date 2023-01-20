import random 
print("siz bilan bir o'yin o'ynaymizma ha yoki yo'q") 
asa=input(">>>") 
while True: 
    def men01(): 
            a=0 
            q = int(input("bosh oraliq=")) 
            w = int(input("tuxtash oralig'i oraliq=")) 
            print("men son o'ylayman siz topasiz") 
            k_m=random.randint(q, w) 
            while True: 
                men=int(input("son keriting >>>")) 
                a+=1 
             
                 
                if men>k_m: 
                    print(f"men o'ylagan son {men} dan kechikroq") 
                elif men<k_m: 
                    print(f"men o'ylagan son {men} dan kattaroq ") 
                else: 
                    if a>4: 
                        print(f"siz yutdingiz {a} marta urinishda tabriklayman") 
                        print("natijangiz yaxshi emas yana xarakatqiling kallani eshlatish kerak") 
                    elif a<4: 
                        print(f"siz yutdingiz {a} marta urinishda tabriklayman") 
                        print("yaxshi chidasa bo'ladi yana harakat qiling") 
                    elif a<2: 
                        print(f"siz yutdingiz {a} marta urinishda tabriklayman") 
                        print("bravo qoyil tasonno kallani ishlatsa bo'larkanku") 
                    break 
    def k_01(): 
            a=0 
            print("siz son o'ylang men topaman") 
            q = int(input("bosh oraliq=")) 
            w = int(input("tuxtash oralig'i oraliq=")) 
            input("son va enter tugmasini bosing ") 
            k_m=random.randint(q, w) 
            while True: 
                k_m=random.randint(q, w) 
                a+=1 
              #  if  
                print(f"{k_m} siz o'ylaganson shumidi") 
                r=input(f"agar javob to'g'ri bo'lsa (y) harfini keriting" 
                        f"yoki siz o'ylagan sondan katta bo'lsa(+) kichik bo'lsa(-)") 
                if r =="+": 
                    q=k_m+1 
                elif r=="-": 
                    w=k_m-1 
                else: 
                    break 
    men01() 
    k_01()