from fitur import create,read,update,delete

def menu():
    print('''==== MENU ====
1. Create
2. Read
3. Update 
4. Delete''')
    return input('Pilih: ')


def main():
    while True:
        pilihan_menu=menu()
        if pilihan_menu=='1':
            create()
        elif pilihan_menu=='2':
            read()
        elif pilihan_menu=='3':
            update()
        elif pilihan_menu=='4':
            delete()
        

main()
    
