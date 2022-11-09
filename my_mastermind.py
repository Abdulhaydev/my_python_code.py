import random

def tasodifiy_son():
    s = 0
    while True:
        t_son = random.randint(1000, 9999)
        t_son = str(t_son)
        for i in range(len(t_son)):
            for j in range(len(t_son)):
                if t_son[i] != t_son[j] and i != j:
                    s += 1
        if s == 12:
            return int(t_son)
        else:
            continue

def togri_joylashtirilgan(t_son, k_son):  # to'g'ri joylashtirilgan bo'lsa 4 qaytaradi
    t_son = str(t_son)
    k_son = str(k_son)
    t_joy = 0
    for i in range(len(k_son)):
        if t_son[i] == k_son[i]: 
            t_joy += 1
    return t_joy

def notogri_joylashtirilgan(t_son, k_son):  # noto'g'ri joylashtirilgan sonlarni sanab beradi
    t_son = str(t_son)
    k_son = str(k_son)
    n_joy = 0
    for i in range(len(t_son)):
        for j in range(len(k_son)):
            if t_son[i] == k_son[j] and i != j:
                n_joy += 1
    return n_joy

def notogri_kiritilgan(raqam):   # to'g'ri kiritilgan bo'lsa 12 qaytaradi
    jamla = 0
    if int(raqam):
        raqam = str(raqam)
        for i in range(len(raqam)):
            for j in range(len(raqam)):
                if raqam[i] != raqam[j] and i != j:
                    jamla += 1
                else:
                    continue
        return jamla
    
def asosiy_qism():
    n_joy = 0
    t_joy = 0
    n_kir = 0
    rd = 0
    t_son = tasodifiy_son()
    print(t_son)
    print("Mastermind o'yinini boshladik!!!")
    while rd <= 10:
        k_son = int(input(f"\nRound {rd}\nson kiriting >>> "))
        t_joy = togri_joylashtirilgan(t_son, k_son)
        n_joy = notogri_joylashtirilgan(t_son, k_son)
        n_kir = notogri_kiritilgan(k_son)
        if n_kir != 12:
            print("\nnoto'g'ri kiritdingiz 1 ta son 2 marta ishtirok etmasligi kerak")
            continue
        elif t_joy != 4:
            print("\ntog'ri joylashtirilgan ", t_joy)
            print("\nnoto'g'ri joylashtirilgan ", n_joy)
        elif t_joy == 4:
            print(f"\nTabriklayman siz yutdingiz men ham {t_son} ni o'ylagan edim!!!")
            break
        rd += 1

asosiy_qism()
