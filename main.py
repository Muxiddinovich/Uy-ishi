import json
from abc import ABC, abstractmethod

class Shaxs:
    def __init__(self, ism, telefon, email):
        self.ism = ism
        self.telefon = telefon
        self.email = email


class Mijoz(Shaxs):
    def __init__(self, ism, telefon, email, mijoz_id):
        super().__init__(ism, telefon, email)
        self.mijoz_id = mijoz_id



class Maxsulot:
    def __init__(self, maxsulot_id, nomi, narxi, soni):
        self.maxsulot_id = maxsulot_id
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni


class Buyurtma:
    def __init__(self, buyurtma_id, mijoz, maxsulotlar):
        self.buyurtma_id = buyurtma_id
        self.mijoz = mijoz
        self.maxsulotlar = maxsulotlar



class Tolov:
    def __init__(self, tolov_id, buyurtma, tolov_usuli, summa):
        self.tolov_id = tolov_id
        self.buyurtma = buyurtma
        self.tolov_usuli = tolov_usuli
        self.summa = summa



def json_saqlash(fayl, malumot):
    with open(fayl, 'w') as f:
        json.dump(malumot, f, indent=4)

def json_oqish(fayl):
    try:
        with open(fayl, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
mijozlar_fayli = 'mijozlar.json'
maxsulotlar_fayli = 'maxsulotlar.json'

def mijoz_qoshish():
    ism=input("Ism:")
    telefon=input("Telefon:")
    email=input("Email:")
    mijoz_id=input("Mijoz ID:")
    mijozlar=json_oqish(mijozlar_fayli)
    mijozlar.append({"Ism":ism, "Telefon":telefon, "Email":email, "Mijoz_id":mijoz_id})
    json_saqlash(mijozlar_fayli, mijozlar)
    print("Mijoz muvaffaqiyatli qo'shildi!")


def maxsulot_qoshish():
    nomi=input("Maxsulot nomi:")
    narxi=float(input("Maxsulot narxi:"))
    soni=int(input("Mavjud soni:"))
    maxsulotlar=json_oqish(maxsulotlar_fayli)
    maxsulotlar.append({"Nomi":nomi, "Narxi":narxi, "Son":soni})
    json_saqlash(maxsulotlar_fayli, maxsulotlar)
    print("Maxsulot muvaffaqiyatli qo'shildi!")


def mijozlar_royxati():
    mijozlar=json_oqish(mijozlar_fayli)
    for i in mijozlar:
        print(i)


def menyu():
    while True:
        print("\n1. Mijoz qo'shish")
        print("2. Maxsulot qo'shish")
        print("3. Mijozlar ro'yxati")
        print("4. Chiqish")
        tanlov=input("Tanlov:")

        if tanlov=='1':
            mijoz_qoshish()
        elif tanlov=='2':
            maxsulot_qoshish()
        elif tanlov=='3':
            mijozlar_royxati()
        elif tanlov=='4':
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__=="__main__":
    menyu()































# def mijoz_qoshish():
#     ism = input("Ism: ")
#     telefon = input("Telefon: ")
#     email = input("Email: ")
#     mijoz_id = input("Mijoz ID: ")
#     mijozlar = json_oqish(mijozlar_fayli)
#     mijoz = Mijoz(ism, telefon, email, mijoz_id)
#     mijozlar.append(mijoz.malumot_korish())
#     json_saqlash(mijozlar_fayli, mijozlar)
#     print("Mijoz muvaffaqiyatli qo'shildi!")





# def mahsulot_qoshish():
#     nomi = input("Mahsulot nomi: ")
#     narxi = float(input("Narxi: "))
#     mavjud_soni = int(input("Mavjud soni: "))
#     mahsulotlar = json_oqish(mahsulotlar_fayli)
#     mahsulot = Mahsulot(nomi, narxi, mavjud_soni)
#     mahsulotlar.append(mahsulot.malumot_korish())
#     json_saqlash(mahsulotlar_fayli, mahsulotlar)
#     print("Mahsulot muvaffaqiyatli qo'shildi!")






# def buyurtma_qoshish():
#     mijoz_id = input("Mijoz ID: ")
#     mahsulot_nomi = input("Mahsulot nomi: ")
#     soni = int(input("Soni: "))
#     mahsulotlar = json_oqish(mahsulotlar_fayli)
#     for mahsulot in mahsulotlar:
#         if mahsulot["nomi"] == mahsulot_nomi and mahsulot["mavjud_soni"] >= soni:
#             umumiy_narx = mahsulot["narxi"] * soni
#             buyurtmalar = json_oqish(buyurtmalar_fayli)
#             buyurtma = Buyurtma(mijoz_id, mahsulot_nomi, soni, umumiy_narx)
#             buyurtmalar.append(buyurtma.malumot_korish())
#             json_saqlash(buyurtmalar_fayli, buyurtmalar)
#             mahsulot["mavjud_soni"] -= soni
#             json_saqlash(mahsulotlar_fayli, mahsulotlar)
#             print("Buyurtma muvaffaqiyatli qo'shildi!")
#             return
#     print("Mahsulot yetarli emas yoki topilmadi!")







# def menyu():
#     while True:
#         print("\n1. Mijoz qo'shish")
#         print("2. Mahsulot qo'shish")
#         print("3. Buyurtma qo'shish")
#         print("4. Chiqish")
#         tanlov = input("Tanlov: ")
        
#         if tanlov == '1':
#             mijoz_qoshish()
#         elif tanlov == '2':
#             mahsulot_qoshish()
#         elif tanlov == '3':
#             buyurtma_qoshish()
#         elif tanlov == '4':
#             break
#         else:
#             print("Noto'g'ri tanlov!")

# if __name__ == "__main__":
#     menyu()
