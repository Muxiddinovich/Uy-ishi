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




mijozlar_fayli = 'mijozlar.json'
mahsulotlar_fayli = 'mahsulotlar.json'
buyurtmalar_fayli = 'buyurtmalar.json'
tolovlar_fayli = 'tolovlar.json'




class Shaxs(ABC):
    def __init__(self, ism, telefon):
        self._ism = ism
        self._telefon = telefon



    @abstractmethod
    def malumot_korish(self):
        pass




class Mijoz(Shaxs):
    def __init__(self, ism, telefon, email, mijoz_id):
        super().__init__(ism, telefon)
        self.email = email
        self.mijoz_id = mijoz_id




    def malumot_korish(self):
        return {"ism": self._ism, "telefon": self._telefon, "email": self.email, "mijoz_id": self.mijoz_id}





class Hodim(Shaxs):
    def __init__(self, ism, telefon, lavozim):
        super().__init__(ism, telefon)
        self.lavozim = lavozim




    def malumot_korish(self):
        return {"ism": self._ism, "telefon": self._telefon, "lavozim": self.lavozim}




class Mahsulot:
    def __init__(self, nomi, narxi, mavjud_soni):
        self.nomi = nomi
        self.narxi = narxi
        self.mavjud_soni = mavjud_soni




    def malumot_korish(self):
        return {"nomi": self.nomi, "narxi": self.narxi, "mavjud_soni": self.mavjud_soni}





class Buyurtma:
    def __init__(self, mijoz_id, mahsulot_nomi, soni, umumiy_narx):
        self.mijoz_id = mijoz_id
        self.mahsulot_nomi = mahsulot_nomi
        self.soni = soni
        self.umumiy_narx = umumiy_narx




    def malumot_korish(self):
        return {"mijoz_id": self.mijoz_id, "mahsulot_nomi": self.mahsulot_nomi, "soni": self.soni, "umumiy_narx": self.umumiy_narx}






def mijoz_qoshish():
    ism = input("Ism: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    mijoz_id = input("Mijoz ID: ")
    mijozlar = json_oqish(mijozlar_fayli)
    mijoz = Mijoz(ism, telefon, email, mijoz_id)
    mijozlar.append(mijoz.malumot_korish())
    json_saqlash(mijozlar_fayli, mijozlar)
    print("Mijoz muvaffaqiyatli qo'shildi!")





def mahsulot_qoshish():
    nomi = input("Mahsulot nomi: ")
    narxi = float(input("Narxi: "))
    mavjud_soni = int(input("Mavjud soni: "))
    mahsulotlar = json_oqish(mahsulotlar_fayli)
    mahsulot = Mahsulot(nomi, narxi, mavjud_soni)
    mahsulotlar.append(mahsulot.malumot_korish())
    json_saqlash(mahsulotlar_fayli, mahsulotlar)
    print("Mahsulot muvaffaqiyatli qo'shildi!")






def buyurtma_qoshish():
    mijoz_id = input("Mijoz ID: ")
    mahsulot_nomi = input("Mahsulot nomi: ")
    soni = int(input("Soni: "))
    mahsulotlar = json_oqish(mahsulotlar_fayli)
    for mahsulot in mahsulotlar:
        if mahsulot["nomi"] == mahsulot_nomi and mahsulot["mavjud_soni"] >= soni:
            umumiy_narx = mahsulot["narxi"] * soni
            buyurtmalar = json_oqish(buyurtmalar_fayli)
            buyurtma = Buyurtma(mijoz_id, mahsulot_nomi, soni, umumiy_narx)
            buyurtmalar.append(buyurtma.malumot_korish())
            json_saqlash(buyurtmalar_fayli, buyurtmalar)
            mahsulot["mavjud_soni"] -= soni
            json_saqlash(mahsulotlar_fayli, mahsulotlar)
            print("Buyurtma muvaffaqiyatli qo'shildi!")
            return

        print("Mahsulot muvaffaqiyatli qo'shildi!")







def menyu():
    while True:
        print("\n1. Mijoz qo'shish")
        print("2. Mahsulot qo'shish")
        print("3. Buyurtma qo'shish")
        print("4. Chiqish")
        tanlov = input("Tanlov: ")
        
        if tanlov == '1':
            mijoz_qoshish()
        elif tanlov == '2':
            mahsulot_qoshish()
        elif tanlov == '3':
            buyurtma_qoshish()
        elif tanlov == '4':
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    menyu()




