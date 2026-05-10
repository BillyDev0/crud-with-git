import requests
import pandas as pd

url='https://jsonplaceholder.typicode.com/posts'
file='CRUD_D5/Data.csv'

res=requests.get(url)
df=pd.DataFrame(res.json())

df.to_csv(file,index=False)

while True:
    id=input('Masukan id: ')
    if id:
        try:
            id=int(id)
        except:
            print('Input id harus angka')
            continue
        cek_id=df['id']==id
        if cek_id.any():
            res=requests.delete(f'{url}/{id}')
            if res.status_code<400:
                print('Data berhasil di hapus')
                res=requests.get(url)
                df=pd.DataFrame(res.json())
                df.to_csv(file,index=False)
                
            else:
                print('Data gagal dihapus')
            break
        else:
            print('Data tidak ditemukan')
    else:
        print('input id kosong')
