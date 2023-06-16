#program perintah import GUI dan Message Box
import tkinter as tk
from tkinter import messagebox as mb

#Fungsi Menampilkan(ganti2) layar
def tampilkan (layar):
    layar.tkraise()

#Soal MTK
soal_mtk = [ '1.) Hasil dari 5 + [6 : (–3)] adalah ?                                                                                                                             ',
         '2.) Suatu barisan aritmetika diketahui U6 = 18 dan U10 = 30. Jumlah 16 suku\n pertama adalah?',
         "3.) Dua suku berikutnya dari pola bilangan 3, 4, 6, 9, … adalah ?                                                                             ",
         "4.) Suatu pekerjaan apabila dilakukan oleh 6 orang dapat diselesaikan dalam\n 6 hari, Apabila pekerja ditambah 3 orang, maka pekerjaan tersebut\n dapat selesai dalam waktu?"  ,
         "5.) Sebuah toko menjual satu lusin buku dengan harga Rp. 90.000,00. Uang \nyang harus dibayarkan Abdul jika membeli 15 buah buku tersebut adalah?",]
#Soal IPA
kunci_mtk =[ [' A. 7 ',' B. 4 ',' C. 3 ',' D. -3'],
         ["A. 360","B. 408","C. 512","D. 896"],
         ["A. 12,15","B. 12,16","C. 13,17","D. 13.18"],
         ["A. 2 Hari","B. 3 Hari","C. 4 Hari","D. 5 Hari"],
         ["A. Rp. 135.500,00","A. Rp. 125.500,00","C. Rp. 115.500,00","D. Rp. 112.500,00"],]

#Perintah Class (agar dapat membedakan dengan yg lain) 
class matematika ():
#Fungsi def init adalah fungsi yang digunakan untuk menjalankan beberapa fungsi lain secara berurutan sesuai urutan yang ditulis 
# Global count berguna untuk menjadikan "count"  agar menjadi keseluruhan dalam program
# Count = Poin benar
    def __init__(self):
        self.p1()
        global count
        self.count = 0
        # p1 adalah pertanyaan 1 dan selanjutnya
    def p1 (self) :
#Menampilkan judul
        self.judul = tk.Label(window, text="Kuis",width=43, bg="green", fg="white", font=("ariel", 40, "bold"))
        self.judul.place(x=0, y=2)
#Menampilkan soal pertama
        self.soal_mtk1=tk.Label(window, text=soal_mtk[0], font=('arial', 30))
        self.soal_mtk1.place(y=70)
#Menampilkan Pilihan (A,B,C,D)
#Command salah satu pilihan berbeda, yang berbeda itulah jawaban yang benar
#Jika memilih (A,B,D) maka akan langsung ke fungsi p22
#Jika memilih C makan akan ke fungsi p2
        self.pilihan1_1 = tk.Button(window, text=kunci_mtk[0][0], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self.p22)
        self.pilihan1_1.place(y=250, x=20)
        self.pilihan1_2 = tk.Button(window, text=kunci_mtk[0][1], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self.p22)
        self.pilihan1_2.place(y=300, x=20)
        self.pilihan1_3 = tk.Button(window, text=kunci_mtk[0][2], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self.p2)
        self.pilihan1_3.place(y=350, x=20)
        self.pilihan1_4 = tk.Button(window, text=kunci_mtk[0][3], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self.p22)
        self.pilihan1_4.place(y=400, x=20)
        #Fungsi p2 akan menambahkan poin (Count) menjadi 1 dan akan langsung menjalankan fungsi ke soal selanjutnya
    def p2 (self):
        global count
        self.count+=1
        self.p22()
#Fungsi soal selanjutnya (2)

    def p22 (self):
# perintah destroy adalah untuk menghancurkan perintah sebelumnya.
#Jika tidak menuliskan perintah destroy maka soal sebelumnya tidak akan hilang dan akan menjadi bertempelan (duplikat)
        self.soal_mtk1.destroy()
        self.pilihan1_1.destroy()
        self.pilihan1_2.destroy()
        self.pilihan1_3.destroy()
        self.pilihan1_4.destroy()
        self.soal_mtk2 = tk.Label(window, text=soal_mtk[1], font=('arial',30))
        self.soal_mtk2.place(y=70)
        self.pilihan2_1 = tk.Button(window, text=kunci_mtk[1][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p33)
        self.pilihan2_1.place(y=250, x=20)
        self.pilihan2_2 = tk.Button(window, text=kunci_mtk[1][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p3)
        self.pilihan2_2.place(y=300, x=20)
        self.pilihan2_3 = tk.Button(window, text=kunci_mtk[1][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p33)
        self.pilihan2_3.place(y=350, x=20)
        self.pilihan2_4 = tk.Button(window, text=kunci_mtk[1][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p33)
        self.pilihan2_4.place(y=400, x=20)
    def p3 (self):
        global count
        self.count+=1
        self.p33()
    def p33 (self):
        self.soal_mtk2.destroy()
        self.pilihan2_1.destroy()
        self.pilihan2_2.destroy()
        self.pilihan2_3.destroy()
        self.pilihan2_4.destroy()
        self.soal_mtk3 = tk.Label(window, text=soal_mtk[2], font=('arial', 30))
        self.soal_mtk3.place(y=70)
        self.pilihan3_1 = tk.Button(window, text=kunci_mtk[2][0], font=('arial', 15, 'bold'), bg="blue",