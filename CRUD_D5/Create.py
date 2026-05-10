import pandas as pd
import requests

url='https://jsonplaceholder.typicode.com/posts'
file='CRUD_D5/Data.csv'

res=requests.get(url)
data=res.json()
df=pd.DataFrame(data)
df.to_csv(file,index=False)