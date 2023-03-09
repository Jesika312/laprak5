def cek_perkalian(a,b):
    total=0
    while total<=a-2:
        print(b,end="+")
        total=total+1
    print(a*b,"=",a,"x",b,"=",b)
a=int(input("masukan nilai a:"))
b=int(input("masukan nilai b:"))
cek_perkalian(a,b)

# def cek_urutan_ganjil(atas,bawah):
#     if bawah<atas:
#         for total in range(bawah,atas,+1):
#             if total%2!=0:
#                 print(total,end=",")
            
#     else:
#         for total in range(bawah,atas,-1):
#             if total%2!=0:
#                 print(total,end=",")
# atas=int(input('masukan batas atas:'))
# bawah=int(input("masukan batas bawah:"))
# cek_ganjil(atas,bawah)


# print("Program penghitung IPS Mahasiswa")
# jlm_matkul=int(input("Berapa jumlah matakuliah:"))
# matakuliah=1
# nilai=0
# list_nilai=[]
# while matakuliah<=jlm_matkul+1:
#     print("nilai matkul",matakuliah,":",end=" ")
#     matakuliah=matakuliah+1
#     nilai1=input("")

