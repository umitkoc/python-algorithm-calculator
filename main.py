from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QPushButton
from sys import argv, exit
from math import pow,log2
from os import system


class Main(QWidget):
    def __init__(self):
        super().__init__()
        system("cls")
        self.array_mx=[]
        self.array_x=[]
        self.array_y=[]
        self.setWindowTitle("MTKC")
        self.resize(500, 1000)
        self.ht()
        self.h_x_t()
        self.bellektanima()
        self.manhattan()
        self.minkowski()
        self.oklid()
        self.Knn()
        self.total = 0.0
        self.lbl2 = QLabel(self)
        self.lbl2.setText(100*'x')
        self.lbl2.move(10, 200)
        self.lbl2.resize(400, 20)
        self.reset = QPushButton(self)
        self.reset.setText("reset")
        self.reset.move(400, 10)
        self.reset.clicked.connect(self.reset_)
        self.toplat = QPushButton(self)
        self.toplat.setText("kazanç oranı bul")
        self.toplat.move(10, 250)
        self.toplat.clicked.connect(self.topladim)
        self.gini()
    def topladim(self):
        sayı = float(self.lbl_hsonuc.text())-float(self.htxtsonuc.text())
        self.lbl_htsonuc.setText(f"{round(sayı,5)}")
    def reset_(self):
        self.array_x=[]
        self.array_y=[]
        self.total = 0.0
    def ht(self):
        self.ht = QLabel(self)
        self.ht.setText("H(T):")
        self.ht.move(10, 10)
        ####
        self.ht_txt = QLineEdit(self)
        self.ht_txt.move(40, 10)
        self.ht_txt.setPlaceholderText("Örn..Evet")
        self.ht_txt.resize(50, 30)
        ###
        self.ht_txt2 = QLineEdit(self)
        self.ht_txt2.move(100, 10)
        self.ht_txt2.setPlaceholderText("Örn..Hayır")
        self.ht_txt2.resize(50, 30)
        ####
        self.lbl_hsonuc = QLabel(self)
        self.lbl_hsonuc.setText("sonuc")
        self.lbl_hsonuc.move(160, 10)
        #####
        self.hbtn = QPushButton(self)
        self.hbtn.move(250, 10)
        self.hbtn.setText("hesapla")
        self.hbtn.clicked.connect(self.hesapla1)
        self.lbl = QLabel(self)
        self.lbl.move(10, 60)
        self.lbl.setText(100*'x')
        self.lbl.resize(400, 10)
    def h_x_t(self):
        self.lblhxt = QLabel(self)
        self.lblhxt.move(10, 100)
        self.lblhxt.setText("H(X,T): ")
        #######
        self.htxtxt = QLineEdit(self)
        self.htxtxt.setPlaceholderText("Örn Sıcak")
        self.htxtxt.move(50, 100)
        self.htxtxt.resize(80, 30)
        #######
        self.htxtxt2 = QLineEdit(self)
        self.htxtxt2.setPlaceholderText("Tümü")
        self.htxtxt2.move(140, 100)
        self.htxtxt2.resize(80, 30)
        #########
        self.htxtxt3 = QLineEdit(self)
        self.htxtxt3.setPlaceholderText("evet")
        self.htxtxt3.move(230, 100)
        self.htxtxt3.resize(80, 30)
        #########
        self.htxtxt4 = QLineEdit(self)
        self.htxtxt4.setPlaceholderText("hayır")
        self.htxtxt4.move(315, 100)
        self.htxtxt4.resize(80, 30)
        #########
        self.htxtbutton = QPushButton(self)
        self.htxtbutton.setText("hesapla")
        self.htxtbutton.move(400, 100)
        self.htxtbutton.clicked.connect(self.hesapla2)
        ########
        self.htxtsonuc = QLabel(self)
        self.htxtsonuc.move(200, 150)
        self.htxtsonuc.setText("sonuc")
        ########
        self.lbl_htsonuc=QLabel(self)
        self.lbl_htsonuc.setText("H(T)-H(X,T)")
        self.lbl_htsonuc.move(150,250)
    def hesapla2(self):
        tur = float(self.htxtxt.text())/float(self.htxtxt2.text())
        toplam = float(self.htxtxt3.text())+float(self.htxtxt4.text())
        sayı1 = float(self.htxtxt3.text())/toplam
        sayı2 = float(self.htxtxt4.text())/toplam
        sonuc = -1*(log2(sayı1)*sayı1+log2(sayı2)*sayı2)*tur
        self.total += sonuc
        self.htxtsonuc.setText(f"{round(self.total,4)}")
    def hesapla1(self):
        sayı1 = float(self.ht_txt.text())
        sayı2 = float(self.ht_txt2.text())
        toplam = sayı1+sayı2
        sayı1 /= toplam
        sayı2 /= toplam
        sonuc = -1*(log2(sayı1)*sayı1+log2(sayı2)*sayı2)
        self.lbl_hsonuc.setText(f"{round(sonuc,4)}")
    def gini(self):
        self.lbl3=QLabel(self)
        self.lbl3.setText(50*"x"+"   \n   gini hesaplaması")
        self.lbl3.resize(400,30)
        self.lbl3.move(10,300)
        ########
        self.lbl_sol=QLabel(self)
        self.lbl_sol.setText("sol:")
        self.lbl_sol.move(10,350)
        ########
        self.soliyi=QLineEdit(self)
        self.soliyi.setPlaceholderText("iyi")
        self.soliyi.move(50,350)
        self.soliyi.resize(30,30)
        ########
        self.solkotu=QLineEdit(self)
        self.solkotu.setPlaceholderText("kötü")
        self.solkotu.move(90,350)
        self.solkotu.resize(30,30)
        ##########
        self.lbl_sag=QLabel(self)
        self.lbl_sag.setText("sag:")
        self.lbl_sag.move(10,400)
        ##########
        self.sagiyi=QLineEdit(self)
        self.sagiyi.setPlaceholderText("iyi")
        self.sagiyi.resize(30,30)
        self.sagiyi.move(50,400)
        ##########
        self.sagkotu=QLineEdit(self)
        self.sagkotu.setPlaceholderText("kötü")
        self.sagkotu.resize(30,30)
        self.sagkotu.move(90,400)
        ##########
        self.ginibtn=QPushButton(self)
        self.ginibtn.setText("Gini Hesapla")
        self.ginibtn.move(150,375)
        self.ginibtn.clicked.connect(self.hesapla3)
        ##########
        self.ginisonuc=QLabel(self)
        self.ginisonuc.setText("sonuc")
        self.ginisonuc.move(300,375)
        ##########
    def hesapla3(self):
        solt = float(self.soliyi.text())+float(self.solkotu.text())
        solcu = (float(self.soliyi.text())/solt)**2
        sagci = (float(self.solkotu.text())/solt)**2
        sol=1-(solcu+sagci)
        #######
        sagt = float(self.sagiyi.text())+float(self.sagkotu.text())
        sagci2 = (float(self.sagiyi.text())/sagt)**2
        solcu2 = (float(self.sagkotu.text())/sagt)**2
        sag=1-(sagci2+solcu2)
        toplam=(solt*sol+sagt*sag)/(solt+sagt)
        self.ginisonuc.setText(f"{round(toplam,5)}")
    def bellektanima(self):
        self.lbl4 = QLabel(self)
        self.lbl4.setText(50*"x"+"   \n   uzaklık hesabı hesaplaması")
        self.lbl4.resize(400,30)
        self.lbl4.move(10,450)
        ########
        self.dij=QLabel(self)
        self.dij.setText("D(i,j):")
        self.dij.move(10,500)
        #######
        self.x1=QLineEdit(self)
        self.x1.setPlaceholderText("X1")
        self.x1.move(50,500)
        self.x1.resize(30,30)
        ########
        self.y1=QLineEdit(self)
        self.y1.setPlaceholderText("Y1")
        self.y1.move(100,500)
        self.y1.resize(30,30)
        ######
        self.x2=QLineEdit(self)
        self.x2.resize(30,30)
        self.x2.move(200,500)
        self.x2.setPlaceholderText("X2")
        ##
        self.y2 = QLineEdit(self)
        self.y2.resize(30, 30)
        self.y2.move(240, 500)
        self.y2.setPlaceholderText("Y2")
        ######
        self.dijbtn=QPushButton(self)
        self.dijbtn.setText("hesapla")
        self.dijbtn.move(300,500)
        self.dijbtn.clicked.connect(self.hesapla4)
        ##########
        self.dijlbl=QLabel(self)
        self.dijlbl.setText("sonuc")
        self.dijlbl.move(425,500)
    def hesapla4(self):
        sayı1=(float(self.x1.text())-float(self.x2.text()))**2
        sayı2=(float(self.y1.text())-float(self.y2.text()))**2
        toplam=pow((sayı2+sayı1),0.5)
        self.dijlbl.setText(f"{round(toplam,3)}")
    def manhattan(self):
        self.manhat=QLabel(self)
        self.manhat.setText("manhattan uzaklığı ve minkowski uzaklığı bulma")
        self.manhat.resize(500,30)
        self.manhat.move(10,550)
        ########
        self.one=QLineEdit(self)
        self.one.setPlaceholderText("m1")
        self.one.resize(30,30)
        self.one.move(10,600)
        ########
        self.two = QLineEdit(self)
        self.two.setPlaceholderText("m2")
        self.two.resize(30, 30)
        self.two.move(50, 600)
        ########
        self.three = QLineEdit(self)
        self.three.setPlaceholderText("m3")
        self.three.resize(30, 30)
        self.three.move(90, 600)
        ########
        self.one2 = QLineEdit(self)
        self.one2.setPlaceholderText("n1")
        self.one2.resize(30, 30)
        self.one2.move(150, 600)
        ########
        self.two2 = QLineEdit(self)
        self.two2.setPlaceholderText("n2")
        self.two2.resize(30, 30)
        self.two2.move(190, 600)
        ########
        self.three2 = QLineEdit(self)
        self.three2.setPlaceholderText("n3")
        self.three2.resize(30, 30)
        self.three2.move(230, 600)
        #########
        self.manhatbtn=QPushButton(self)
        self.manhatbtn.setText("manhat hesapla")
        self.manhatbtn.move(270,600)
        self.manhatbtn.clicked.connect(self.hesapla5)
        #########
        self.manhatsonuc=QLabel(self)
        self.manhatsonuc.setText("sonuc")
        self.manhatsonuc.move(10,650)
    def hesapla5(self):
        sayı1=(float(self.one.text())-float(self.one2.text()))**2
        sayı2 = (float(self.two.text())-float(self.two2.text()))**2
        sayı3 = (float(self.three.text())-float(self.three2.text()))**2
        toplam=pow((sayı1+sayı2+sayı3),0.5)
        self.manhatsonuc.setText(f"{round(toplam,5)}")
    def minkowski(self):
        self.minkowsbtn=QPushButton(self)
        self.minkowsbtn.setText("minkows hesapla")
        self.minkowsbtn.move(380,600)
        self.minkowsbtn.clicked.connect(self.hesapla6)
    def hesapla6(self):
        uc=1/3
        sayı1 = (float(self.one.text())-float(self.one2.text()))**3
        sayı2 = (float(self.two.text())-float(self.two2.text()))**3
        sayı3 = (float(self.three.text())-float(self.three2.text()))**3
        toplam=pow((sayı1+sayı2+sayı3),uc)
        self.manhatsonuc.setText(f"{round(toplam,5)}")
    def oklid(self):
        self.oklidx1=QLineEdit(self)
        self.oklidx1.setPlaceholderText("x1")
        self.oklidx1.move(10,700)
        self.oklidx1.resize(30,30)
        ####
        self.oklidx2=QLineEdit(self)
        self.oklidx2.setPlaceholderText("x2")
        self.oklidx2.move(50,700)
        self.oklidx2.resize(30,30)
        #####
        self.oklidx3=QLineEdit(self)
        self.oklidx3.setPlaceholderText("x3")
        self.oklidx3.move(90,700)
        self.oklidx3.resize(30,30)
        
        ######
        self.oklidxx1=QLineEdit(self)
        self.oklidxx1.setPlaceholderText("x1")
        self.oklidxx1.move(170,700)
        self.oklidxx1.resize(30,30)
        ######
        self.oklidxx2=QLineEdit(self)
        self.oklidxx2.setPlaceholderText("x2")
        self.oklidxx2.move(210,700)
        self.oklidxx2.resize(30,30)
         ######
        self.oklidxx3=QLineEdit(self)
        self.oklidxx3.setPlaceholderText("x3")
        self.oklidxx3.move(250,700)
        self.oklidxx3.resize(30,30)

        ########
        self.oklidbtn=QPushButton(self)
        self.oklidbtn.setText("Oklid Hesapla")
        self.oklidbtn.move(290,700)
        self.oklidbtn.resize(120,30)
        ####
        self.oklid_lbl=QLabel(self)
        self.oklid_lbl.setText("sonuc")
        self.oklid_lbl.move(10,750)
        self.oklidbtn.clicked.connect(self.oklid_hesapla)
    def oklid_hesapla(self):
        sayı1=(float(self.oklidx1.text())-float(self.oklidxx1.text()))**2
        sayı2=(float(self.oklidx2.text())-float(self.oklidxx2.text()))**2
        sayı3=(float(self.oklidx3.text())-float(self.oklidxx3.text()))**2
        kare=1/2
        sonuc=pow((sayı1+sayı2+sayı3),kare)
        self.oklid_lbl.setText(f"{round(sonuc,2)}")
    def Knn(self):
        self.knn_lbl=QLabel(self)
        self.knn_lbl.setText(f"{'*'*50}\nKNN Hesaplaması")
        self.knn_lbl.move(10,770)
        self.knn_lbl.resize(300,30)
        #######
        self.knx=QLineEdit(self)
        self.knx.setPlaceholderText("x1")
        self.knx.resize(30, 30)
        self.knx.move(10,800)
         #######
        self.knx_btn=QPushButton(self)
        self.knx_btn.setText("x ekle")
        self.knx_btn.resize(50,30)
        self.knx_btn.move(50,800)
        self.knx_btn.clicked.connect(self.x_total)
        #######
        self.kny=QLineEdit(self)
        self.kny.setPlaceholderText("y1")
        self.kny.resize(30, 30)
        self.kny.move(120,800)
        #######
        self.kny_btn=QPushButton(self)
        self.kny_btn.setText("y ekle")
        self.kny_btn.resize(50,30)
        self.kny_btn.move(160,800)
        self.kny_btn.clicked.connect(self.y_total)
        #######
        self.m_total_btn=QPushButton(self)
        self.m_total_btn.setText("m hesapla")
        self.m_total_btn.resize(100,30)
        self.m_total_btn.move(230,800)
        #########
        self.xy_reset_btn=QPushButton(self)
        self.xy_reset_btn.setText("resetle")
        self.xy_reset_btn.resize(100,30)
        self.xy_reset_btn.move(350,800)
        self.xy_reset_btn.clicked.connect(self.xy_reset)
        #########
        self.mx=QLineEdit(self)
        self.mx.move(10,850)
        self.mx.resize(40,30)
        self.mx.setPlaceholderText("mx")
        self.mx.setEnabled(False)
        #######
        self.my=QLineEdit(self)
        self.my.move(50,850)
        self.my.resize(40,30)
        self.my.setPlaceholderText("my")
        self.my.setEnabled(False)
        ########
        self.m_btn=QPushButton(self)
        self.m_btn.move(90,850)
        self.m_btn.resize(50,30)
        self.m_btn.setText("m ekle")
        self.m_btn.clicked.connect(self.m_total)
        #########
        self.m_hesap_btn=QPushButton(self)
        self.m_hesap_btn.setText("e^2 hesapla")
        self.m_hesap_btn.move(150,850)
        self.m_hesap_btn.resize(100,30)
        #########
        self.e_lbl=QLabel(self)
        self.e_lbl.setText("e^2:")
        self.e_lbl.move(10,900)
        #########
    def x_total(self):
        self.array_x.append(float(self.knx.text()))
    def y_total(self):
        self.array_x.append(float(self.kny.text()))
    def xy_total(self):
        totalx=0
        totaly=0
        for i in self.array_x:
            totalx+=i
        totalx/=len(self.array_x)
        for i in self.array_y:
            totaly+=i
        totaly/=len(self.array_y)
        self.mx.setText(f"{round(totalx,3)}")
        self.my.setText(f"{round(totaly,3)}")
    def xy_reset(self):
        self.array_x.clear()
        self.array_y.clear()
        self.array_mx.clear()
    def m_total(self):
        pass



    


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec_())
