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
                                    fg="white", command=self.p44)
        self.pilihan3_1.place(y=250, x=20)
        self.pilihan3_2 = tk.Button(window, text=kunci_mtk[2][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p44)
        self.pilihan3_2.place(y=300, x=20)
        self.pilihan3_3 = tk.Button(window, text=kunci_mtk[2][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p4)
        self.pilihan3_3.place(y=350, x=20)
        self.pilihan3_4 = tk.Button(window, text=kunci_mtk[2][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p44)
        self.pilihan3_4.place(y=400, x=20)
    def p4 (self):
        global count
        self.count+=1
        self.p44()
    def p44 (self):
        self.soal_mtk3.destroy()
        self.pilihan3_1.destroy()
        self.pilihan3_2.destroy()
        self.pilihan3_3.destroy()
        self.pilihan3_4.destroy()
        self.soal_mtk4 = tk.Label(window, text=soal_mtk[3], font=('arial', 30))
        self.soal_mtk4.place(y=70)
        self.pilihan4_1 = tk.Button(window, text=kunci_mtk[3][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p55)
        self.pilihan4_1.place(y=250, x=20)
        self.pilihan4_2 = tk.Button(window, text=kunci_mtk[3][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p5)
        self.pilihan4_2.place(y=300, x=20)
        self.pilihan4_3 = tk.Button(window, text=kunci_mtk[3][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p55)
        self.pilihan4_3.place(y=350, x=20)
        self.pilihan4_4 = tk.Button(window, text=kunci_mtk[3][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.p55)
        self.pilihan4_4.place(y=400, x=20)
    def p5 (self):
        global count
        self.count+=1
        self.p55()
    def p55 (self):
        self.soal_mtk4.destroy()
        self.pilihan4_1.destroy()
        self.pilihan4_2.destroy()
        self.pilihan4_3.destroy()
        self.pilihan4_4.destroy()
        self.soal_mtk5 = tk.Label(window, text=soal_mtk[4], font=('arial', 30))
        self.soal_mtk5.place(y=70)
        self.pilihan5_1 = tk.Button(window, text=kunci_mtk[4][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.hasil1)
        self.pilihan5_1.place(y=250, x=20)
        self.pilihan5_2 = tk.Button(window, text=kunci_mtk[4][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.hasil1)
        self.pilihan5_2.place(y=300, x=20)
        self.pilihan5_3 = tk.Button(window, text=kunci_mtk[4][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.hasil1)
        self.pilihan5_3.place(y=350, x=20)
        self.pilihan5_4 = tk.Button(window, text=kunci_mtk[4][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self.poin)
        self.pilihan5_4.place(y=400, x=20)
    def poin (self):
        global count
        self.count+=1
        self.hasil1()
    def hasil1 (self):
        self.judul.destroy()
        self.soal_mtk5.destroy()
        self.pilihan5_1.destroy()
        self.pilihan5_2.destroy()
        self.pilihan5_3.destroy()
        self.pilihan5_4.destroy()
        global count
        self.kkm = 60
        #perintah nilai adalah jika poin (count) dikali 20
#perintah benar adalah poin (count) itu sendiri
#perintah salah adalah ketika jumlah soal (5) dikurangi poin(count)
        self.nilai = self.count*20
        self.benar = self.count
        self.salah = 5-self.count
#mb.showinfo adalah tampilan pemberitahuan dengan cara menampilkan layar kecil 
#informasi yang ditulis berupa nama yang tadi telah dimasukan pada saat login, dan juga nim. Nilai, jumlah benar dan salah juga akan tampil
        mb.showinfo("Hasil",f"Nama :{layar2_entry1.get()}\nNim :{layar2_entry22.get()}\nNilai :{self.nilai}\nJumlah Benar :{self.benar}\nJumlah Salah :{self.salah}")
#fungsi percabangan if else, jika nilai dibawah kkm(60) maka akan langsung mengeksekusi perintah ingin mengulang atau tidak
#Jika mengulang maka akan langsung pindah ke soal pertama, jika tidak maka aplikasi akan keluar
        if self.nilai < self.kkm:
            gagal = mb.askyesno('Kamu Gagal', 'Apakah ingin mengulang?')
            if gagal == True:
                matematika()
            else:
                window.destroy()
#Jika jumlah nilai diatas kkm maka akan tampil informasi selamat dan aplikasi akan keluar
        else :
            mb.showinfo("Selamat", 'Anda Berhasil menyelesaikan kuis')
            window.destroy()

#Perintah menghancurkan 3 variable dibawah
#masuk ke kelas matematika yang ada diatas
#fungsi ini sebagai loncatan dari pemilihan pelajaran ke kuis
def mtk ():
    layar3_title.destroy()
    layar3_btn.destroy()
    layar3_btn1.destroy()
    matematika()


soal_ipa = [ '1.) Sebuah transformator step up menghasilkan beda potensial 200 volt. Transformator tersebut dihubungkan\n dengan sumber tegangan 100 volt. Jika arus yang mengalir pada kumparan primer 150 mA, maka arus listrik\n yang mengalir pada kumparan skunder adalah ...',
             '2.) Ketika bayi baru lahir tingginya 50 cm, setelah 1 bulan diukur tingginya di posyandu menjadi 55 cm. Hal\n ini merupakan ciri makhluk hidup yaitu … .',
             "3.) Sel tumbuhan lebih kuat dan lebih kaku dibandingkan sel hewan, bagian organel sel yang membedakan adalah",
         "4.) Kebiasaan membawa beban yang terlalu berat dibagian punggung sehingga tubuh membungkuk. Kebiasaan tersebut\n dapat mengakibatkan kelainan tulang yang disebut … ",
         "5.) Sebuah benda bergerak di atas lantai. Kecepatan benda tersebut semakin lama semakin kecil dan akhirnya \nberhenti. Gaya yang menyebabkan gerak benda tersebut semakin melambat adalah … .",]
kunci_ipa =[ [' A. 75mA  ',' B. 100mA',' C. 150mA',' D. 300mA'],
         ["A.          Tumbuh         ","B. Memerlukan Nutrisi","C.       Berkembang     ","D.  Berkembang Biak  "],
         ["A.    Dinding Sel  ","B. Membrane Sel","C.    Kloroplas    ","D.  Mitokondria  "],
         ["A. Skoliosis","B.   Rakitis ","C.   Kifosis ","D. Lordosis"],
         ["A. Gaya Dorong  ","B. Gaya Gesekan","C.    Gaya Tarik   ","D.   Gaya Berat   "],]


class ipaa ():
    def __init__(self1):
        self1.p1()
        global count
        self1.count = 0
    def p1 (self1) :
        self1.judul = tk.Label(window, text="Ujian Online",width=43, bg="green", fg="white", font=("ariel", 40, "bold"))
        self1.judul.place(x=0, y=2)
        self1.soal_ipa1=tk.Label(window, text=soal_ipa[0], font=('arial', 20))
        self1.soal_ipa1.place(y=70)
        self1.pilihan1_1 = tk.Button(window, text=kunci_ipa[0][0], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self1.p2)
        self1.pilihan1_1.place(y=250, x=20)
        self1.pilihan1_2 = tk.Button(window, text=kunci_ipa[0][1], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self1.p22)
        self1.pilihan1_2.place(y=300, x=20)
        self1.pilihan1_3 = tk.Button(window, text=kunci_ipa[0][2], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self1.p22)
        self1.pilihan1_3.place(y=350, x=20)
        self1.pilihan1_4 = tk.Button(window, text=kunci_ipa[0][3], font=('arial', 15, 'bold'),bg="blue", fg="white",command=self1.p22)
        self1.pilihan1_4.place(y=400, x=20)
    def p2 (self1):
        global count
        self1.count+=1
        self1.p22()
    def p22 (self1):
        self1.soal_ipa1.destroy()
        self1.pilihan1_1.destroy()
        self1.pilihan1_2.destroy()
        self1.pilihan1_3.destroy()
        self1.pilihan1_4.destroy()
        self1.soal_ipa2 = tk.Label(window, text=soal_ipa[1], font=('arial',20))
        self1.soal_ipa2.place(y=70)
        self1.pilihan2_1 = tk.Button(window, text=kunci_ipa[1][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p3)
        self1.pilihan2_1.place(y=250, x=20)
        self1.pilihan2_2 = tk.Button(window, text=kunci_ipa[1][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p33)
        self1.pilihan2_2.place(y=300, x=20)
        self1.pilihan2_3 = tk.Button(window, text=kunci_ipa[1][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p33)
        self1.pilihan2_3.place(y=350, x=20)
        self1.pilihan2_4 = tk.Button(window, text=kunci_ipa[1][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p33)
        self1.pilihan2_4.place(y=400, x=20)
    def p3 (self1):
        global count
        self1.count+=1
        self1.p33()
    def p33 (self1):
        self1.soal_ipa2.destroy()
        self1.pilihan2_1.destroy()
        self1.pilihan2_2.destroy()
        self1.pilihan2_3.destroy()
        self1.pilihan2_4.destroy()
        self1.soal_ipa3 = tk.Label(window, text=soal_ipa[2], font=('arial', 20))
        self1.soal_ipa3.place(y=70)
        self1.pilihan3_1 = tk.Button(window, text=kunci_ipa[2][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p4)
        self1.pilihan3_1.place(y=250, x=20)
        self1.pilihan3_2 = tk.Button(window, text=kunci_ipa[2][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p44)
        self1.pilihan3_2.place(y=300, x=20)
        self1.pilihan3_3 = tk.Button(window, text=kunci_ipa[2][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p44)
        self1.pilihan3_3.place(y=350, x=20)
        self1.pilihan3_4 = tk.Button(window, text=kunci_ipa[2][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p44)
        self1.pilihan3_4.place(y=400, x=20)
    def p4 (self1):
        global count
        self1.count+=1
        self1.p44()
    def p44 (self1):
        self1.soal_ipa3.destroy()
        self1.pilihan3_1.destroy()
        self1.pilihan3_2.destroy()
        self1.pilihan3_3.destroy()
        self1.pilihan3_4.destroy()
        self1.soal_ipa4 = tk.Label(window, text=soal_ipa[3], font=('arial', 20))
        self1.soal_ipa4.place(y=70)
        self1.pilihan4_1 = tk.Button(window, text=kunci_ipa[3][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p55)
        self1.pilihan4_1.place(y=250, x=20)
        self1.pilihan4_2 = tk.Button(window, text=kunci_ipa[3][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p55)
        self1.pilihan4_2.place(y=300, x=20)
        self1.pilihan4_3 = tk.Button(window, text=kunci_ipa[3][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p5)
        self1.pilihan4_3.place(y=350, x=20)
        self1.pilihan4_4 = tk.Button(window, text=kunci_ipa[3][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.p55)
        self1.pilihan4_4.place(y=400, x=20)
    def p5 (self1):
        global count
        self1.count+=1
        self1.p55()
    def p55 (self1):
        self1.soal_ipa4.destroy()
        self1.pilihan4_1.destroy()
        self1.pilihan4_2.destroy()
        self1.pilihan4_3.destroy()
        self1.pilihan4_4.destroy()
        self1.soal_ipa5 = tk.Label(window, text=soal_ipa[4], font=('arial', 20))
        self1.soal_ipa5.place(y=70)
        self1.pilihan5_1 = tk.Button(window, text=kunci_ipa[4][0], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.hasil1)
        self1.pilihan5_1.place(y=250, x=20)
        self1.pilihan5_2 = tk.Button(window, text=kunci_ipa[4][1], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.poin)
        self1.pilihan5_2.place(y=300, x=20)
        self1.pilihan5_3 = tk.Button(window, text=kunci_ipa[4][2], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.hasil1)
        self1.pilihan5_3.place(y=350, x=20)
        self1.pilihan5_4 = tk.Button(window, text=kunci_ipa[4][3], font=('arial', 15, 'bold'), bg="blue", fg="white", command=self1.hasil1)
        self1.pilihan5_4.place(y=400, x=20)
    def poin (self1):
        global count
        self1.count+=1
        self1.hasil1()
    def hasil1 (self1):
        self1.judul.destroy()
        self1.soal_ipa5.destroy()
        self1.pilihan5_1.destroy()
        self1.pilihan5_2.destroy()
        self1.pilihan5_3.destroy()
        self1.pilihan5_4.destroy()
        global count
        self1.kkm = 60
        self1.nilai = self1.count*20
        self1.benar = self1.count
        self1.salah = 5-self1.count
        mb.showinfo("Hasil", f"Nama :{layar2_entry1.get()}\nNim :{layar2_entry22.get()}\nNilai :{self1.nilai}\nJumlah Benar :{self1.benar}\nJumlah Salah :{self1.salah}")
        if self1.nilai < self1.kkm:
            gagal = mb.askyesno('Kamu Gagal', 'Apakah ingin mengulang?')
            if gagal == True:
                ipaa()
            else:
                window.destroy()
        else :
            mb.showinfo("Selamat", 'Anda Berhasil menyelesaikan kuis')
            window.destroy()

def ipa ():
    layar3_title.destroy()
    layar3_btn.destroy()
    layar3_btn1.destroy()
    ipaa()

#perintah menampilkan GUI (Graphic User Interface)
window = tk.Tk()
#perintah agar program ketika di run layar window langsung dalam keaadan jendela penuh (maximize)
window.state('zoomed')
#perintah menampilkan judul aplikasi
window.title(' KUIS ')

#perintah untuk mengatur ukuran row dan column
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#perintah untuk membedakan layar
layar1 = tk.Frame(window)
layar2 = tk.Frame(window)
layar3 = tk.Frame(window)

#perintah perulangan agar layar dapat berubah2
for frame in (layar1,layar2,layar3):
    frame.grid(row=0,column=0,sticky='nsew')

#perintah layar pertama 
#tk.Label untuk menampilkan tulisan (teks)
#tk.Button untuk menampilkan tombol

layar1_title = tk.Label(layar1, text="SELAMAT DATANG DI PORTAL UJIAN ONLINE", font=('eras bold itc',40),width=80, height=3)
layar1_title.pack()
layar1_title1 = tk.Label(layar1, text="Tekan Login untuk Melanjutkan", font=('eras bold itc',20),width=80, height=3)
layar1_title1.pack()
layar1_button = tk.Button(layar1, text="LOGIN", font=('eras bold itc',10),bg='green', fg='white',width=15, height=3, command=lambda:tampilkan(layar2))
layar1_button.pack()
tampilkan(layar1)

#perintah layar kedua
#tk.Entry untuk menampilkan kolom untuk menginput
#Perbedaan pack dan place adalah, jika pack maka objek akan langsung tampil pada tengah layar. sedangkan place untuk mengatur posisi objek, x=kanan-kiri,y=atas bawah
#perintah comman:lambda adalah perintah untuk menampilkan layar berbeda
layar2_title = tk.Label(layar2, text="UJIAN ONLINE", font=('Algerian',40))
layar2_title.pack(pady=50)
layar2_title = tk.Label(layar2, text='NAMA', font=('Arial', 10))
layar2_title.pack(padx=(0,260), pady=(50,0))
layar2_entry1 = tk.Entry(layar2, font=('Arial',15))
layar2_entry1.place(x=600,y=215)
layar2_entry2 = tk.Label(layar2, text='NIM', font=('Arial', 10))
layar2_entry2.pack(padx=(0,280), pady=(30,0))
layar2_entry22 = tk.Entry(layar2,font=('Arial',15))
layar2_entry22.place(x=600,y=265)
layar2_btn = tk.Button(layar2, text='    Enter    ', command=lambda:tampilkan(layar3))
layar2_btn.place(x=600,y=305)
tampilkan(layar1)

#perintah layar ketiga
#command untuk menjalankan fungsi 
layar3_title = tk.Label(layar3, text="Silahkan Pilih Mata pelajaran Anda", font=('Algerian',40))
layar3_title.pack(pady=50)
layar3_btn = tk.Button(layar3, text='MATEMATIKA',font=('Arial',15), command=mtk)
layar3_btn.pack(pady=20)
layar3_btn1 = tk.Button(layar3, text='   IPA    ',font=('Arial',15), command=ipa)
layar3_btn1.pack()
tampilkan(layar1)

#panggilan untuk GUI agar berjalan secara terus menerus.
window.mainloop()