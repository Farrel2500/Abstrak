class ikan:
     def __init__(var,q):
        var.quest = q
        var.jaw=[]
        var.isi=[]
        var.nilai= 0

     def Siu(self):
        if self.quest == "M":
            print('_ _ _ _ _')
            self.isi = [int(x) for x in input("Jawaban: ").split()]
            print("Jawaban yang benar:", self.jaw)
            print("Skor:", self.nilai)

     def Messi(self):
     import random
     x=[1,2,3,4,5]

     for i in range(len(x)):
         k= random.choice(x)
         self.jaw.append(x)
         x.remove(x)
     def skor(self):
        if self.jaw[0] == self.isi[0]:
            self.nilai += 20
        elif self.jaw[1]== self.isi[1]:
            self.nilai += 20
        elif self.jaw[2] == self.isi[2]:
            self.nilai += 20
        elif self.jaw[3]== self.isi[3]:
            self.nilai += 20
        elif self.jaw[4]== self.isi[4]:
            self.nilai += 20
def output():
    print('Selamat datang')
    q.Siu()
if __name__ =="__main__":
 while True:
  output()