import json

def load():
    try:
        with open('CRUD_D2/data.json') as f:
            data=f.read().strip()
            if data:
                return json.loads(data)
            else:
                return []
            
    except FileNotFoundError:
        return []
    
def save(data):
    with open('CRUD_D2/data.json', 'w') as f:
        json.dump(data,f,indent=1)
    