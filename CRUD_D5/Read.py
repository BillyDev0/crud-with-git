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
            print('input id harus angka')
            continue
        cek_id=df[df['id']==id]
        if not cek_id.empty:
            print(cek_id)
            break
        else:
            print('Data tidak ditemukan')
    else:
        print('input id kosong')
        