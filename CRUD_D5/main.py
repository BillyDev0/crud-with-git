def menu():
    print('''======= MENU CRUD =======
1. Create Data
2. Read Data
3. Update Data
4. Delete Data
5. Exit''')
    return input('Pilih: ')

def main():
    while True:
        pilihan_menu=menu()
        if pilihan_menu == "1":
            pass
        elif pilihan_menu == "2":
            pass
        elif pilihan_menu =="3":
            pass
        elif pilihan_menu == "4":
            pass
        elif pilihan_menu == "5":
            print('Program selesai')
            break
        else:
            continue

main()
