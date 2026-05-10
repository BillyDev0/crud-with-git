import pandas as pd
import os

file='CRUD_D3/data.csv'

def create():
    if not os.path.exists(file):
       df=pd.DataFrame(columns=["nama","umur","kota","score"])
    else:
       df=pd.read_csv(file)
    
    while True:
       nama=input('Nama: ').strip().lower()
       if nama:
         hasil=df[df['nama']==nama]
         if hasil.empty:
            umur=input('Umur: ')
            kota=input('Kota: ').strip().lower()
            score=input('Score: ')

            if umur and kota and score:
               try:
                  umur=int(umur)
                  score=int(score)

                  data_baru=pd.DataFrame([{
                     'nama':nama,
                     'umur':umur,
                     'kota':kota,
                     'score':score
                  }])

                  data_baru.to_csv(file,mode='a',index=False,header=not os.path.exists(file))
                  print('Data berhasil dibuat')
                  break

               except:
                  print('umur dan score harus angka!!')
            else:
               print('Input data tidak lengkap')
         else:
            print('Data sudah terdaftar')
       else:
          print('input nama kosong!!!')
        


def read():
  while True:
    try:
      df=pd.read_csv(file)
    except:
       print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
       return

    nama=input('Nama: ').lower().strip()
    if nama:
       hasil=df[df['nama']==nama]
       if not hasil.empty:
          print(hasil)
          break
       else:
          print('Data tidak ditemukan')
    else:
       print('input tidak boleh kosong!!')


def update():
    while True:
        try:
           df=pd.read_csv(file)
        except:
           print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
       
        nama=input('Nama: ').strip().lower()
        if nama:
           hasil=df['nama']==nama

           if hasil.any():
              input_nama=input('Nama (enter jika tidak): ').strip().lower()
              input_umur=input('Umur (enter jika tidak): ')
              input_kota=input('Kota (enter jika tidak): ').strip().lower()
              input_score=input('Score (enter jika tidak): ')

              try:
                 input_umur=int(input_umur)
                 input_score=int(input_score)

                 if input_nama:
                    df.loc[hasil,'nama']=input_nama
                 if input_umur:
                    df.loc[hasil,'umur']=input_umur
                 if input_kota:
                    df.loc[hasil,'kota']=input_kota
                 if input_score:
                    df.loc[hasil,'score']=input_score
                 
                 df.to_csv(file,index=False)
                 print('Data selesai diupdate')
                 break
              
              except:
                 print('umur dan score harus angka!! ')
                 
           else:
              print('Data tidak ditemukan')

        else:
           print('input nama tidak boleh kosong')

        
def delete():
    while True:
      try:
       df=pd.read_csv(file)
      except:
       print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
       return
      
      nama=input('Nama: ').strip().lower()
      if nama:
         hasil=df[df['nama'] == nama]
    
         if not hasil.empty:
           df=df[df['nama'] != nama]
           df.to_csv(file,index=False)

           print('Data berhasil dihapus')
         else:
           print('Data tidak ditemukan!!')
      else:
         print('input nama tidak boleh kosong!!')
        
    
def sorting():
  while True:
    try:
       df=pd.read_csv(file)
    except:
       print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')

    print('''1. Berdasarkan score
2. Berdasarkan umur''')
    
    pilihan_user=input('Pilih: ').strip().lower()
    
    if pilihan_user=='1':
        print(df.sort_values(by='score', ascending=False).reset_index(drop=True))
    elif pilihan_user=='2':
        print(df.sort_values(by='umur', ascending=False).reset_index(drop=True))
    else:
        continue
    return


