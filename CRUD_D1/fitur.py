def create(data):
    nama=input('Nama: ')
    for item in data:
        if nama == item['Nama']:
            print('Data sudah ada')
            return
        
    kelas=input('Kelas: ')
    no_absen=input('No absen: ')
    
    data_baru={
        'Nama':nama,
        'Kelas':kelas,
        'No absen':no_absen
    }

    data.append(data_baru)
    print('Data berhasil ditambah!')


def read(data):
    nama=input('Nama: ')
    for item in data:
        if nama == item['Nama']:
            print(item)
            return
    else:
        print('Data tidak ditemukan!')
    

def update(data):
    input_nama=input('Nama: ')
    for item in data:
        if input_nama == item['Nama']:

            nama=input('Nama (enter jika tidak): ')
            kelas=input('Kelas (enter jika tidak): ')
            no_absen=input('No absen (enter jika tidak): ')
            
            if not nama=='':
               item['Nama']=nama

            if not kelas=='':
               item['Kelas']=kelas

            if not no_absen=='':
               item['No absen']=no_absen
            
            print('Data berhasil diupdate')

        else:
            print('Data tidak ditemukan')

def delete(data):
    nama=input('Nama: ')
    for item in data:
        if nama == item['Nama']:
            data.remove(item)
            print('Data berhasil berhasil dihapus')

        else:
            print('Data tidak ditemukan')