class BankHisobi:
    def __init__(self, egasi, hisob_raqami, balans):
        self.egasi = egasi
        self.hisob_raqami = hisob_raqami
        self.balans = balans

    def pul_qoshish(self, summa):
        self.balans += summa
        return self.balans

    def pul_yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
        return self.balans

    def balansni_tekshirish(self):
        return self.balans


class JamgarmaHisobi(BankHisobi):
    def __init__(self, egasi, hisob_raqami, balans, foiz):
        super().__init__(egasi, hisob_raqami, balans)
        self.foiz = foiz

    def foiz_hisobla(self):
        foyda = self.balans * self.foiz
        self.balans += foyda
        return self.balans


hisob = BankHisobi("Azizbek", "UZ123456", 500000)

print("Egasi:", hisob.egasi)
print("Hisob raqami:", hisob.hisob_raqami)
print("Balans:", hisob.balans)

hisob.pul_qoshish(200000)
print("Pul qo'shilgandan keyin:", hisob.balans)

hisob.pul_yechish(100000)
print("Pul yechilgandan keyin:", hisob.balans)


jamgarma = JamgarmaHisobi("Malika", "UZ987654", 1000000, 0.10)

print("Jamg'arma egasi:", jamgarma.egasi)
print("Boshlang'ich balans:", jamgarma.balans)

jamgarma.foiz_hisobla()
print("Foiz qo'shilgandan keyin:", jamgarma.balans)
