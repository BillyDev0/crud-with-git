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

        cek_id=df['id']==id

        if cek_id.any():
            input_userId=input('Masukan userId (enter jika tidak): ')
            input_title=input('Masukan title (enter jika tidak): ')
            input_body=input('Masukan body (enter jika tidak): ')
            
            data={}
            try:
               if input_userId:
                  input_userId=int(input_userId)
                  data['userId']=input_userId
               
               if input_title:
                   data['title']=input_title
               
               if input_body:
                   data['body']=input_body
               
               if data:
                   res=requests.patch(f'{url}/{id}',json=data)
                   if res.status_code<400:
                       print('Berhasil diupdate')
                       res=requests.get(url)
                       df=pd.DataFrame(res.json())
                       df.to_csv(file,index=False)
                       
                   else:
                       print('Data gagal diupdate')
                   break
            except:
                print('input userId dan id harus angka')
        
        else:
            print('Data tidak ditemukan')
    else:
        print('input id kosong')

               
            
            

            
