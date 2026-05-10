import pandas as pd
import os 
import requests

url='https://jsonplaceholder.typicode.com/posts'
file='CRUD_D4/data.csv'

res=requests.get(url)
data=res.json()
df=pd.DataFrame(data)
df.to_csv(file,index=False)

def create():
    if not os.path.exists(file):
        df=pd.DataFrame(columns=['userId','id','title','body']) 
    else:
        df=pd.read_csv(file)
    
    while True:
      userId=input('userId: ').strip()
      id=input('id: ').strip()

      if userId and id:
        try:
            id=int(id)
            userId=int(userId)
        except:
            print('input harus number')
            continue
        
        if not (df['id']==id).any():
                title=input('Title: ')
                body=input('Body: ')

                if title and body:
                    data_baru={
                        'id':id,
                        'userId':userId,
                        'title':title,
                        'body':body
                    }
                    
                    res=requests.post(url,json=data_baru)
                    pd.DataFrame([data_baru]).to_csv(file,index=False,mode='a',header=not os.path.exists(file) or os.stat(file).st_size==0)

                    print('Status code: ',res.status_code)
                    print('Data berhasil ditambah')
                    break
                else:
                    print('input tidak lengkap!!')
        else:
            print('Data id telah terdaftar')
      else:
          print('input tidak lengkap')



def read():
    try:
        df=pd.read_csv(file)
    except:
        print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
        return
    
    while True:
        id=input('id: ').strip()
        if id:
            try:
                id=int(id)
                hasil=df[df['id']==id]
                if not hasil.empty:
                   print(hasil)
                   break
                else:
                    print('Data tidak ditemukan')
            except:
                print('input id harus angka')
        else:
            print('input id tidak boleh kosong')


def update():
    try:
        df=pd.read_csv(file)
    except:
        print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
        return
    
    while True:
        id=input('id: ')
        
        if id:
            try:
                id=int(id)
            except:
                print('input id harus angka!!!')
                continue

            hasil=df['id']==id
            if hasil.any():
               input_userId=input('userId (enter jika tidak): ')
               input_id=input('id (enter jika tidak): ')

               if (df['id']==input_id).any():
                   print('id sudah ada')
                   continue
               
               input_title=input('title (enter jika tidak): ')
               input_body=input('body (enter jika tidak): ')
               
               try:
                   if input_userId:
                       input_userId=int(input_userId)
                       data['userId']=input_userId                     
                       df.loc[hasil,'userId']=input_userId

                   if input_id:
                       input_id=int(input_id)                      
                       data['id']=input_id
                       df.loc[hasil,'id']=input_id

                   if input_title:
                       data['title']=input_title
                       df.loc[hasil,'title']=input_title

                   if input_body:
                       data['body']=input_body
                       df.loc[hasil,'body']=input_body

                   if data:
                       res=requests.patch(f'{url}/{id}',json=data)
                   df.to_csv(file,index=False)

                   print('Data berhasil diupdate')
                   break
               
               except:
                   print('input id dan userId harus angka')
            else:
                print('Data tidak ditemukan')
        else:
            print('input id tidak boleh kosong')

def delete(): 
  try:
    df=pd.read_csv(file)
  except:
    print('File tidak ditemukan. Klik menu create untuk membuat file atau menambah data')
    return
  
  while True:  
    id=input('id: ')
    try:
        id=int(id)
    except:
        print('input id harus angka!')
        continue
    if id:
        hasil=df['id']==id

        if any():
            res=requests.delete(f'{url}/{id}')
            print(res.status_code)

            df=df[~hasil]
            df.to_csv(file,index=False)

            print('Data berhasil dihapus')
            break
        else:
            print('Data tidak ditemukan')
    else:
        print('input id tidak boleh kosong')

            
                


                


        
