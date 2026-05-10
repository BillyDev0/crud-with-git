import pandas as pd
import requests

url='https://jsonplaceholder.typicode.com/posts'
file='CRUD_D5/Data.csv'

res=requests.get(url)
df=pd.DataFrame(res.json())

df.to_csv(file,index=False)

while True:
    userId=input('Masukan userId: ')
    id=input('Masukan Id: ')
    if userId and id:
        try:
            userId=int(userId)
            id=int(id)
        except:
            print('input id dan userId harus angka')
            continue

        cek_id=df['id']==id
        if not cek_id.any():
           title=input('Masukan title: ')
           body=input('Masukan body: ')

           if title and body:
               data_baru={
                   'userId':userId,
                   'id':id,
                   'title':title,
                   'body':body
               }

               res=requests.post(url,json=data_baru)
               if res.status_code<400:
                   print('Data berhasil ditambah ke API')

                   res=requests.get(url)
                   df=pd.DataFrame(res.json())

                   df.to_csv(file,index=False)

               else:
                   print('Data tidak berhasil conect ke API')

               break
           else:
               print('Input tidak lengkap')
        
        else:
            print('Data id sudah terdaftar')
    
    else:
        print('Input tidak lengkap')
               
                   

