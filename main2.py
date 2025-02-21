import json
from abc import ABC, abstractmethod


def json_saqlash(fayl, malumotlar):
    with open(fayl, 'w') as f:
        json.dump(malumotlar, f, indent=4)

def json_oqish(fayl):
    try:
        with open(fayl, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

class Shaxs(ABC):
    def __init__(self, ism, telefon, email):
        self.ism = ism
        self.__telefon = telefon  
        self.__email = email

    def get_telefon(self):
        return self.__telefon

    def get_email(self):
        return self.__email

    @abstractmethod
    def malumot(self):
        pass


class Mijoz(Shaxs):
    def __init__(self, ism, telefon, email, mijoz_id):
        super().__init__(ism, telefon, email)
        self.mijoz_id = mijoz_id

    def malumot(self):
        return {"Ism": self.ism, "Telefon": self.get_telefon(), "Email": self.get_email(), "ID": self.mijoz_id}

class Xodim(Shaxs):
    def __init__(self, ism, telefon, email, lavozim):
        super().__init__(ism, telefon, email)
        self.lavozim = lavozim

    def malumot(self):
        return {"Ism": self.ism, "Telefon": self.get_telefon(), "Email": self.get_email(), "Lavozim": self.lavozim}


class Mahsulot:
    def __init__(self, nomi, narxi, mavjud_soni):
        self.nomi = nomi
        self.narxi = narxi
        self.mavjud_soni = mavjud_soni

    def malumot(self):
        return {"Nomi": self.nomi, "Narxi": self.narxi, "Mavjud soni": self.mavjud_soni}


class Buyurtma:
    def __init__(self, mahsulot, soni):
        self.mahsulot = mahsulot
        self.soni = soni

    def malumot(self):
        return {"Mahsulot": self.mahsulot.nomi, "Soni": self.soni, "Jami": self.mahsulot.narxi * self.soni}


class Tolov(ABC):
    @abstractmethod
    def tolov_amalga_oshirish(self):
        pass

class PlastikTolov(Tolov):
    def tolov_amalga_oshirish(self, summa):
        return f"Plastik karta orqali to'lov amalga oshirildi: {summa} so'm"

mijozlar_fayli = 'mijozlar.json'
mahsulotlar_fayli = 'mahsulotlar.json'
buyurtmalar_fayli = 'buyurtmalar.json'

def mijoz_qoshish():
    ism = input("Ism: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    mijoz_id = input("Mijoz ID: ")
    mijozlar = json_oqish(mijozlar_fayli)
    mijoz = Mijoz(ism, telefon, email, mijoz_id)
    mijozlar.append(mijoz.malumot())
    json_saqlash(mijozlar_fayli, mijozlar)
    print("Mijoz muvaffaqiyatli qo'shildi!")


def mahsulot_qoshish():
    nomi = input("Mahsulot nomi: ")
    narxi = float(input("Narxi: "))
    mavjud_soni = int(input("Mavjud soni: "))
    mahsulotlar = json_oqish(mahsulotlar_fayli)
    mahsulot = Mahsulot(nomi, narxi, mavjud_soni)
    mahsulotlar.append(mahsulot.malumot())
    json_saqlash(mahsulotlar_fayli, mahsulotlar)
    print("Mahsulot muvaffaqiyatli qo'shildi!")


def buyurtma_berish():
    mijoz_id = input("Mijoz ID: ")
    mahsulot_nomi = input("Mahsulot nomi: ")
    soni = int(input("Nechta olasiz: "))
    mahsulotlar = json_oqish(mahsulotlar_fayli)
    mahsulot = next((m for m in mahsulotlar if m["Nomi"] == mahsulot_nomi), None)
    if mahsulot:
        buyurtmalar = json_oqish(buyurtmalar_fayli)
        buyurtma = Buyurtma(mijoz_id, Mahsulot(mahsulot_nomi, mahsulot["Narxi"], mahsulot["Mavjud soni"]), soni)
        buyurtmalar.append(buyurtma.malumot())
        json_saqlash(buyurtmalar_fayli, buyurtmalar)
        print("Buyurtma qabul qilindi!")
    else:
        print("Mahsulot topilmadi!")


def menyu():
    while True:
        print("\n1. Mijoz qo'shish")
        print("2. Mahsulot qo'shish")
        print("3. Buyurtma berish")
        print("4. Chiqish")
        tanlov = input("Tanlov: ")
        if tanlov == '1':
            mijoz_qoshish()
        elif tanlov == '2':
            mahsulot_qoshish()
        elif tanlov == '3':
            buyurtma_berish()
        elif tanlov == '4':
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    menyu()



