import pandas as pd
import requests

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
        
        cek=df['id']==id
        if (df['id']==id).any():
            userId=input('Masukan usereId: ')
            title=input('Masukan title: ')
            body=input('Masukan body: ')

            data={}
            if userId:
                try:
                    userId=int(userId)
                except:
                    print('input userId harus angka')
                    continue
                data['userId']=userId
            
            if title:
                data['title']=title
            
            if body:
                data['body']=body
            
            if data:
                res=requests.patch(f'{url}/{id}',json=data)
                if res.status_code < 400:
                    print('Data berhasil diupdate')
                    res=requests.get(url)
                    df=pd.DataFrame(res.json())
                    df.to_csv(file,index=False)
                    
                else:
                    print('Data tidak dapat diupdate ke server')

                break
        else:
            print('Data tidak ditemukan')
    else:
        print('input id kosong')