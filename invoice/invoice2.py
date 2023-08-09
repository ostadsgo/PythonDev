import date2
import time2


class Factor:
    def __init__(self, shomare_factor, name_moshtari, tarikh, saat):
        self.radifhaye_factor = []
        self.name_moshtari = name_moshtari
        self.tarikh = tarikh
        self.saat = saat

    def afzodan_kala(self, kala, tedad=1):
        mahsol = kala + ":" + str(tedad)
        self.radifhaye_factor.append(mahsol)

    def jame_kol(self):
        mablaghe_kol = 0
        # Joda karda esme kala va qeymat
        for radif in self.radifhaye_factor:
            name, qeymat, qeymat_kol = radif[0], radif[1], radif[2]
            mablaghe_kol += qeymat_kol

        return mablaghe_kol

    def moshahdeh_factor(self):
        print()
        print(self.tarikh, "-", self.saat)
        print("Name Moshtari:", self.name_moshtari)
        print("------------------------------")
        print("Mahsol    Qeymat    Qeymate Kol")
        for radif in self.radifhaye_factor:
            name, qeymat, qeymat_kol = radif[0], radif[1], radif[2]
            # print ba 20 ta fasle barye esme mahsol va 10 ta barye bagheye
            print(name, qeymat, qeymat_kol)
        # jame kole factor
        kol = self.jame_kol()
        print("------------------------------")
        print("Mablagheh kol pardakhti:", "$" + str(kol))

    def moshadeh_masholat(self, mahsolat):
        shomare = 1
        for mahsol in mahsolat:
            #   name mahsol   qeymat
            name_mahsol = mahsol[0]
            qeymat_mahsol = mahsol[1]
            print(shomare, name_mahsol, qeymat_mahsol)
            shomare += 1

    def daryafte_kala(self, mahsolat):
        # Moshahdeh kol mahsolate anbar
        self.moshadeh_masholat(mahsolat)

        # Daryafte shomare mahsol az tarafe sandogdar.
        shomare_mahsol = int(input("Shomare kala ra vard konid: "))
        mahsole_entekhab_shode = mahsolat[shomare_mahsol - 1]
        name_mahsol = mahsole_entekhab_shode[0]
        qeymat_mahsol = mahsole_entekhab_shode[1]

        tedade = int(input("Tedade kala: "))

        # # tedade kala zarbdare qeymat mahsol
        qeymat_kol = qeymat_mahsol * tedade

        # # yek radif dar factor
        radife_factor = [name_mahsol, qeymat_mahsol, qeymat_kol]
        self.radifhaye_factor.append(radife_factor)


#             name   qeymat   name    qeymat   name      qeymat
mahsolat = [["Pitza", 14], ["Capochino", 5], ["Hamberger", 9]]

# Tarikhe va saate faktor
d = date2.Date(1403, 5, 16)
t = time2.Time(9, 25, 3)

# Daryfete name moshtari va ejad yek faktor barye moshtari
name_moshtari = input("Esme moshtari ra vard konid: ")
f = Factor(11, name_moshtari, d, t)

# Shart barye inke az karbar mahsol begirad ya na
q = 'y'
while q == 'y':
    # Daryfte darkhaste moshteri va ejade factor chapi
    f.daryafte_kala(mahsolat)
    q = input("Baraye edame 'y' ra bezan ya 'q' bazan kharej sho:")

# Chap factor roye tasvir
f.moshahdeh_factor()
