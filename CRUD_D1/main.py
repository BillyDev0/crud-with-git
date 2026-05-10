from fitur import create,read,update,delete
def menu():
    print('''==== MENU ====
1. Create
2. Read
3. Update
4. Delete
5. keluar''')
    return input('Pilih: ')

def main():
    data_siswa=[]
    while True:
        pilihan_menu=menu()
        if pilihan_menu=='1':
            create(data_siswa)

        elif pilihan_menu=='2':
            read(data_siswa)

        elif pilihan_menu=='3':
            update(data_siswa)

        elif pilihan_menu=='4':
            delete(data_siswa)

        elif pilihan_menu=='5':
            break
        
        else:
            continue

main()