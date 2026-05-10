def create(data):
    nama=input('Nama: ')
    kelas=input('Kelas: ')
    no_absen=input('No absen: ')

    data_baru={
        'Nama':nama,
        'Kelas':kelas,
        'No absen':no_absen
    }
    data.append(data_baru)
    
    
    print('Berhasil membuat data siswa')


def read(data):
  while True:
    nama=input('Nama: ')
    if nama =='':
       continue
    for item in data:
        if nama==item['Nama']:
            print(f'Kelas: {item['Kelas']}')
            print(f'No absen: {item['No absen']}')
        
        else:
           print('Data tidak ditemukan')


def update(data):
  while True:
    nama=input('Nama: ').strip()
    if nama=='':
       continue

    for item in data:
      if nama in item['Nama']:
        nama_baru=input('Nama (enter jika tetap): ')
        kelas=input('Kelas (enter jika tetap): ')
        no_absen=input('No absen (enter jika tetap): ')

        if nama_baru:
            item['Nama']=nama
        if kelas:
            item['Kelas']=kelas
        if no_absen:
            item['No absen']=no_absen
        
        print('Data berhasil modifikasi')
        return
        
    
      else:
        print('Data tidak ditemukan')

    
def delete(data):
  while True:
    nama=input('Nama: ')
    if nama=='':
       continue
    for item in data:
       if nama == item['Nama']:
          data.remove(item)
          return
       else:
          print('Data tidak ditemukan')