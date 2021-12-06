# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:07:55 2021
@author: Muhammad Danil Hidayat
@NIM : 065002100032
@Judul : Praktikum 12
"""

class Mahasiswa:
    
    def _init_(self, nama, angkatan, nim):
        self.nama=nama
        self.angkatan=angkatan
        self.nim=nim
        
    def BiodataMahasiswa(self):
        print("\nNama : ", self.nama,"\nNim : ", self.nim,"\nAngkatan : ", self.angkatan)

name=input("Masukan namamu : ")
nomor=int(input("Masukan NIM mu : "))
tahun=int(input("Masukan Tahun Angkatanmu : "))
maha1=Mahasiswa(name, tahun, nomor)
maha1.BiodataMahasiswa()