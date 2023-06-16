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