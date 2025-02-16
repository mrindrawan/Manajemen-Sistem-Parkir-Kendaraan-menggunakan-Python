from tabulate import tabulate

list_kendaraan = [
    {"NO TIKET": "PK0001", "PLAT": "B3234AC", "JENIS": "MOTOR", "MERK": "YAMAHA", "CHECKIN": "07:12", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0002", "PLAT": "E1292DS", "JENIS": "MOBIL", "MERK": "TOYOTA", "CHECKIN": "07:45", "TARIF/JAM": 5000},
    {"NO TIKET": "PK0005", "PLAT": "D5426PAE", "JENIS": "MOTOR", "MERK": "HONDA", "CHECKIN": "08:23", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0006", "PLAT": "B6467KG", "JENIS": "MOTOR", "MERK": "SUZUKI", "CHECKIN": "09:10", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0007", "PLAT": "B1155FR", "JENIS": "MOBIL", "MERK": "HONDA", "CHECKIN": "09:37", "TARIF/JAM": 5000},
    {"NO TIKET": "PK0010", "PLAT": "E4548ZA", "JENIS": "MOTOR", "MERK": "VESPA", "CHECKIN": "10:05", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0012", "PLAT": "F4279DU", "JENIS": "MOTOR", "MERK": "DUCATI", "CHECKIN": "10:52", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0015", "PLAT": "B5914NS", "JENIS": "MOTOR", "MERK": "KAWASAKI", "CHECKIN": "11:11", "TARIF/JAM": 2000},
    {"NO TIKET": "PK0017", "PLAT": "E1886ABB", "JENIS": "MOBIL", "MERK": "DAIHATSU", "CHECKIN": "12:02", "TARIF/JAM": 5000},
    {"NO TIKET": "PK0020", "PLAT": "E1465FH", "JENIS": "MOBIL", "MERK": "ISUZU", "CHECKIN": "12:28", "TARIF/JAM": 5000}
]

def input_int(pesan_input,pesan_error):
    while True:
        int_input = input(pesan_input)
        if int_input.isdigit():  # Mengecek apakah input hanya angka positif
            return int(int_input)
        else:
            print(pesan_error)


def input_str(pesan_input,pesan_error):
    while True:
        str_name = input(pesan_input)
        if str_name.isalpha(): # Mengecek apakah input hanya huruf
            return str_name
        else:
            print(pesan_error)


def input_alnum(pesan_input,pesan_error):
    while True:
        alnum_name = input(pesan_input)
        if alnum_name.isalnum() and not (alnum_name.isdigit() or alnum_name.isalpha()): # Mengecek apakah input hanya kombinasi huruf dan angka
            return alnum_name
        else:
            print(pesan_error)


def tampilkan_tabel(prompt): # Tampilkan Daftar Parkir Kendaraan
    print(f"\n{" "*23} DAFTAR PARKIR KENDARAAN {" "*23}")
    table = tabulate(
        prompt, 
        headers="keys", 
        tablefmt="fancy_grid",
        numalign="center",
        stralign="center"
        )
    print(table)


def konfirmasi(prompt1,prompt2): # konfirmasi ya/tidak
    while True:
        konfirmasi = input(prompt1).upper()
        if konfirmasi in ("YA","TIDAK"):
            return konfirmasi
        else:
            print(prompt2)


def notif_list_kosong(): # Menampilkan notif data kosong
    print("\n=======================================================================")
    print("!!! DAFTAR KENDARAAN KOSONG❌. SILAHKAN TAMBAH DAN UPDATE KENDARAAN !!!")
    print("=======================================================================")

    
def main_menu(): # Menampilkan main_menu()
    while True:
        print("\n============ SISTEM PARKIR KENDARAAN ============")
        print("\nSELAMAT DATANG DI SISTEM KENDARAAN PARKIR\n")
        print("""LIST MENU :\n
    1. DAFTAR PARKIR KENDARAAN
    2. TAMBAH DATA KENDARAAN
    3. HAPUS DATA KENDARAAN 
    4. UPDATE DAFTAR PARKIR KENDARAAN
    5. PEMBAYARAN PARKIR
    6. KELUAR\n""")

        angka_menu = input_int("Masukkan angka Menu yang ingin dijalankan : ", "Input tidak valid. Pilih angka dari 1-6.")

        if angka_menu == 1: # Fungsi untuk menampilkan Daftar Parkir Kendaraan (READ MENU)
            daftar_kendaraan()

        elif angka_menu == 2: # Fungsi untuk Tambah Kendaraan
            tambah_kendaraan()

        elif angka_menu == 3: # Fungsi untuk Hapus Kendaraan
            hapus_kendaraan()
            
        elif angka_menu == 4: # Fungsi untuk Update Kendaraan
            update_kendaraan()

        elif angka_menu == 5: # Fungsi untuk Tarif Parkir Kendaraan
            tarif_kendaraan()

        elif angka_menu == 6: # Fungsi untuk Exit program
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar(YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                print("\n>>> TERIMA KASIH <<<\n")
                break
            else:
                print("\n------------------------------------")
                print("> > > > KEMBALI KE MAIN MENU < < < <")
                print("------------------------------------")
                pass
        else:
            print("Input tidak valid. Pilih angka dari 1-6.")


def daftar_kendaraan(): # <-------------------- (READ MENU)
    while True:
        print("""\nMENU 1: DAFTAR PARKIR KENDARAAN\n
        1. Tampilkan Seluruh Daftar Parkir Kendaraan
        2. Tampilkan Data Kendaraan berdasarkan Nomor Tiket
        3. Tampilkan Data Kendaraan berdasarkan Plat Nomor (Untuk Tiket yang Hilang)
        4. Keluar\n""")
        
        inputDaftarKendaraan = input_int("Masukkan angka Menu yang ingin dijalankan : ", 
                                         "Input tidak valid. Pilih angka dari 1-4.")
        
        if inputDaftarKendaraan == 1: # Fungsi untuk menampilkan seluruh Daftar Parkir Kendaraan

            if not list_kendaraan:
                notif_list_kosong()
            else:
                # Tampilkan Daftar Parkir Kendaraan
                tampilkan_tabel(list_kendaraan)

        elif inputDaftarKendaraan == 2: 

            if not list_kendaraan:
                notif_list_kosong()
            else:
                # Masukkan input NO TIKET Daftar Parkir Kendaraan
                while True:
                    inputNoTiket = input_alnum("Masukkan [NO TIKET] Parkir Kendaraan : ", 
                                                    "Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.").upper()
                    if len(inputNoTiket) == 6 and inputNoTiket[:2] == "PK" and inputNoTiket[2:].isdigit():
                        break
                    else:
                        print("Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.")

                # Cek apakah NO TIKET sudah ada di list_kendaraan
                find_kendaraan = None 

                for kendaraan in list_kendaraan: # Cek apakah NO TIKET sudah ada di list_kendaraan
                    if kendaraan["NO TIKET"] == inputNoTiket:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    # Tampilkan Daftar Parkir Kendaraan berdasarkan PLAT Nomor
                    tampilkan_tabel([find_kendaraan])
                else:
                    print("\n======================================================================")
                    print(f"❌ NOMOR TIKET '{inputNoTiket}' TIDAK DITEMUKAN. MASUKKAN NOMOR TIKET KEMBALI.")
                    print("======================================================================")

        elif inputDaftarKendaraan == 3:

            if not list_kendaraan:
                notif_list_kosong()
            else:
                # Masukkan input PLAT Nomor Daftar Parkir Kendaraan
                input_platno = input_alnum("Masukkan [PLAT] Nomor Kendaraan (Tanpa Spasi): ", 
                                           "Input tidak valid. Masukkan input dengan kombinasi huruf dan angka untuk [PLAT] Nomor.").upper()

                # Cek apakah PLAT nomor sudah ada di list_kendaraan
                find_kendaraan = None 

                for kendaraan in list_kendaraan: # Cek apakah PLAT nomor sudah ada di list_kendaraan
                    if kendaraan["PLAT"] == input_platno:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    tampilkan_tabel([find_kendaraan])
                else:
                    print("\n=====================================================================")
                    print(f"❌ PLAT NOMOR '{input_platno}' TIDAK DITEMUKAN. MASUKKAN PLAT NOMOR KEMBALI.")
                    print("=====================================================================")
        
        elif inputDaftarKendaraan == 4: # Fungsi untuk Keluar dari Daftar Parkir Kendaraan
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar (YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                break
            else:
                pass

        else:
            print("Input tidak valid. Pilih angka dari 1-4.")


def tambah_kendaraan(): # <-------------------- (CREATE MENU)
    while True:
        print("""\nMENU 2: TAMBAH DATA KENDARAAN\n
        1. Masukkan Kendaraan Baru
        2. Keluar\n""")

        input_tambahBaru = input_int("Masukkan angka Menu yang ingin dijalankan : ", 
                                     "Input tidak valid. Pilih angka dari 1-2.")
        
        if input_tambahBaru == 1: # Fungsi untuk menampilkan tambah Kendaraan Baru
        
            if not list_kendaraan:
                notif_list_kosong()
            else:
                # Tampilkan Daftar Parkir Kendaraan
                tampilkan_tabel(list_kendaraan)        

            lanjut_update_data = konfirmasi("\nLanjut Tambah Data Kendaraan? (YA/TIDAK) : ",
                                            "Input tidak valid. Ketik (YA/TIDAK)")
            
            if lanjut_update_data == "YA":
                # List Tambahan
                list_tambah = []

                # Masukkan input Kolom Nomor Tiket (dengan validasi)
                while True:
                    input_no_tiket = input_alnum("\nMasukkan [NO TIKET] baru dengan kode 'PK' diawal dan 4 angka setelahnya : ", 
                                                "Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.").upper()
                    if len(input_no_tiket) == 6 and input_no_tiket[:2] == "PK" and input_no_tiket[2:].isdigit():
                        break
                    else:
                        print("Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.")

                # Cek No Tiket (keluar dari loop jika sudah terdaftar)
                for kendaraan in list_kendaraan: # Cek apakah NO TIKET sudah ada di list_kendaraan
                    if kendaraan["NO TIKET"] == input_no_tiket:
                        print("\n==============================================================================================")
                        print(f"!!! NO TIKET [{input_no_tiket}] KENDARAAN SUDAH TERDAFTAR, SILAHKAN MASUKKAN NO TIKET KENDARAAN BARU !!!")
                        print("==============================================================================================")
                        break    
                else:
                    # Masukkan Plat No Kendaraan
                    input_plat = input_alnum("Masukkan [PLAT] Nomor Kendaraan Baru (Tanpa Spasi): ", 
                                            "Input tidak valid. Masukkan [PLAT] Nomor dengan kombinasi huruf dan angka.").upper()

                    # Masukkan input Jenis Kendaraan
                    while True:
                        input_jenis = input_str("Masukkan [JENIS] Kendaraan Baru (MOBIL/MOTOR) : ", 
                                                "Input tidak valid. Masukkan [JENIS] kendaraan MOBIL/MOTOR").upper()
                        if input_jenis == "MOBIL" or input_jenis == "MOTOR":
                            break
                        else:
                            print("Input tidak valid. Masukkan [JENIS] kendaraan MOBIL/MOTOR")
                    
                    # Masukkan MERK Kendaraan
                    input_merk = input_str("Masukkan [MERK] Kendaraan Baru : ", 
                                        "Input tidak valid. Masukkan [MERK] Kendaraan hanya huruf").upper()

                    # Masukkan Jam Masuk Kendaraan
                    while True:
                        input_jammasuk1 = input_int("Masukkan Waktu Jam Masuk [CHECKIN] dengan 4 angka (HHMM = JamMenit) tanpa tanda ':' = ", 
                                                    "Input tidak valid. Pastikan terdapat 4 angka untuk Jam dan Menit (HHMM)")
                        
                        # Ubah kembali ke format 4 digit dengan leading zero jika perlu
                        input_jammasuk1 = f"{input_jammasuk1:04d}"

                        # Ambil 2 angka pertama sebagai jam dan 2 angka terakhir sebagai menit
                        jam = int(input_jammasuk1[:2])
                        menit = int(input_jammasuk1[2:])

                        # Validasi jam (00-23) dan menit (00-59)
                        if 0 <= jam <= 23 and 0 <= menit <= 59:
                            input_jammasuk2 = f"{jam:02d}:{menit:02d}"  # Format HH:MM
                            break
                        else:
                            print("Input tidak valid. Jam harus antara 00-23 dan Menit antara 00-59.")

                    # Masukkan Tarif Per Jam Kendaraan
                    if input_jenis == "MOBIL":
                        input_perjam = 5000
                    elif input_jenis == "MOTOR":
                        input_perjam = 2000

                    # Tambahkan Dict ke list tambah
                    list_tambah.append({
                        'NO TIKET': input_no_tiket,
                        "PLAT": input_plat,
                        "JENIS": input_jenis,
                        "MERK": input_merk,
                        "CHECKIN": input_jammasuk2,
                        "TARIF/JAM": input_perjam
                    })

                    # Tampilkan list tambah
                    tampilkan_tabel(list_tambah)           

                    yakin_tambah = konfirmasi(f"Yakin ingin menambah Kendaraan dengan NO TIKET {input_no_tiket}? (YA/TIDAK) : ", 
                                            "Input tidak valid. Ketik (YA/TIDAK)")

                    if yakin_tambah == "YA":    
                        # Menambahkan buah baru ke dalam list_kendaraan
                        list_kendaraan.extend(list_tambah)
                        tampilkan_tabel(list_kendaraan)
                        print(f"\nKENDARAAN DENGAN NO TIKET '{input_no_tiket}' BERHASIL DITAMBAHKAN!")
                    else:
                        print("\n=========================================================")
                        print("PENAMBAHAN [DIBATALKAN]. KEMBALI KE MENU TAMBAH KENDARAAN.")   
                        print("=========================================================")
            else:
                print("\n===========================================================")
                print("TAMBAH [DIBATALKAN]. KEMBALI KE MENU TAMBAH DATA KENDARAAN.")
                print("===========================================================")

        elif input_tambahBaru == 2: # Fungsi untuk Keluar dari tambah Kendaraan Baru
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar (YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                break
            else:
                pass

        else:
            print("Input tidak valid. Pilih angka dari 1-2.")


def hapus_kendaraan(): # <-------------------- (DELETE MENU)
    while True:
        print("""\nMENU 3: HAPUS DATA KENDARAAN\n
        1. Hapus Kendaraan dari Daftar Parkir
        2. Keluar\n""")

        MenuKendaraanHapus = input_int("Masukkan angka Menu yang ingin dijalankan : ", 
                                       "Input tidak valid. Pilih angka dari 1-2.")
        
        if MenuKendaraanHapus == 1: # Fungsi untuk Hapus Kendaraan dari NO TIKET
            
            if not list_kendaraan:
                notif_list_kosong()
            else:
                tampilkan_tabel(list_kendaraan)

                # Masukkan input Kolom NO TIKET
                while True:
                    input_TiketNoBaru = input_alnum("Masukkan [NO TIKET] Parkir Kendaraan yang ingin dihapus : ", 
                                                    "Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.").upper()
                    if len(input_TiketNoBaru) == 6 and input_TiketNoBaru[:2] == "PK" and input_TiketNoBaru[2:].isdigit():
                        break
                    else:
                        print("Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.")

                # Cek apakah NO TIKET sudah ada di list_kendaraan
                find_kendaraan = None

                for kendaraan in list_kendaraan: # Cek apakah NO TIKET sudah ada di list_kendaraan
                    if kendaraan["NO TIKET"] == input_TiketNoBaru:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    tampilkan_tabel([find_kendaraan])

                    yakin_hapus = konfirmasi(f"Yakin ingin menghapus Kendaraan dengan [NO TIKET] {input_TiketNoBaru}? (YA/TIDAK) : ",
                                            "Input tidak valid. Ketik (YA/TIDAK)").upper()

                    if yakin_hapus == "YA":    
                        list_kendaraan.remove(kendaraan) # Hapus data kendaraan berdasarkan No Tiket

                        if not list_kendaraan:
                            notif_list_kosong()
                        else:
                            tampilkan_tabel(list_kendaraan)

                        print("\n======================================================")
                        print(f"KENDARAAN DENGAN [NO TIKET] '{input_TiketNoBaru}' BERHASIL DIHAPUS.")
                        print("======================================================")
                    else:
                        print("\n==========================================================")
                        print("PENGHAPUSAN [DIBATALKAN]. KEMBALI KE MENU HAPUS KENDARAAN.")
                        print("==========================================================")
            
                else:   
                    print("\n======================================================================")
                    print(f"❌ NOMOR TIKET '{input_TiketNoBaru}' TIDAK DITEMUKAN. MASUKKAN NOMOR TIKET KEMBALI.")
                    print("======================================================================")    

        elif MenuKendaraanHapus == 2: # Fungsi untuk Keluar dari Menu Hapus Kendaraan
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar (YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                break
            else:
                pass
        else:
            print("Input tidak valid. Pilih angka dari 1-2.")


def update_kendaraan(): # <-------------------- (UPDATE MENU)
    while True:
        print("""\nMENU 4: UPDATE DAFTAR PARKIR KENDARAAN\n
        1. Update Data Kendaraan dari Daftar Parkir
        2. Keluar\n""")

        MenuKendaraanUpdate = input_int("Masukkan angka Menu yang ingin dijalankan : ", 
                                        "Input tidak valid. Pilih angka dari 1-2.")

        if MenuKendaraanUpdate == 1:

            if not list_kendaraan:
                notif_list_kosong()
            else:
                tampilkan_tabel(list_kendaraan)

                while True:
                    input_tiket_update = input_alnum("Masukkan [NO TIKET] Parkir Kendaraan : ", 
                                                    "Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.").upper()
                    if len(input_tiket_update) == 6 and input_tiket_update[:2] == "PK" and input_tiket_update[2:].isdigit():
                        break
                    else:
                        print("Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.")
                
                find_kendaraan = None
                
                for kendaraan in list_kendaraan:
                    if kendaraan["NO TIKET"] == input_tiket_update:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    tampilkan_tabel([find_kendaraan])

                    lanjut_update = konfirmasi("Lanjut Update Data Kendaraan Parkir? (YA/TIDAK) : ", 
                                            "Input tidak valid. Ketik (YA/TIDAK)")

                    if lanjut_update == "YA":
                        while True:                     
                            input_kolom = input_str("Masukkan nama Kolom apa yang ingin di Update ( PLAT | JENIS | MERK | CHECKIN ) : ", 
                                                    "Input tidak valid. Masukkan nama kolom sesuai pada Daftar Parkir Kendaraan").upper() 
                            if input_kolom in find_kendaraan:
                                break
                            else:
                                print("Input tidak valid. Masukkan nama kolom sesuai pada Daftar Parkir Kendaraan")

                        while True:

                            if input_kolom == "PLAT":                           
                                input_nilai_baru = input_alnum("Masukkan [PLAT] Nomor yang baru (Tanpa Spasi): ", 
                                                            "Input tidak valid. Masukkan [PLAT] Nomor yang akan di Update").upper()
                                
                                find_kendaraan_PLAT = None
            
                                for kendaraan in list_kendaraan:
                                    if kendaraan["PLAT"] == input_nilai_baru:
                                        find_kendaraan_PLAT = kendaraan
                                        break

                                if find_kendaraan_PLAT:
                                    print("[PLAT] Nomor sudah 'Terdaftar'. Masukkan [PLAT] Nomor baru.")
                                else:
                                    break

                            elif input_kolom == "JENIS":                           
                                input_nilai_baru = input_str("Masukkan [JENIS] Kendaraan yang baru (MOBIL/MOTOR) : ", 
                                                            "Input tidak valid. Ketik MOBIL / MOTOR").upper()                           
                                if input_nilai_baru in ("MOBIL", "MOTOR"):
                                    if input_nilai_baru == "MOBIL":
                                        find_kendaraan["TARIF/JAM"] = 5000
                                        break
                                    else: 
                                        find_kendaraan["TARIF/JAM"] = 2000
                                        break
                                else:
                                    print("Input tidak valid. Ketik MOBIL / MOTOR")
                            
                            elif input_kolom == "MERK":
                                input_nilai_baru = input_str("Masukkan [MERK] Kendaraan yang baru : ", 
                                                            "Input tidak valid. Masukkan [MERK] Kendaraan harus berupa huruf semua").upper()                           
                                if input_nilai_baru.isalpha():
                                    break
                                else:
                                    print("Input tidak valid. Masukkan [MERK] Kendaraan dengan huruf")
                        
                            elif input_kolom == "CHECKIN":
                                while True:
                                    input_jam = input_int("Masukkan Waktu Jam Masuk [CHECKIN] dengan 4 angka (HHMM = JamMenit) tanpa tanda ':' = ", 
                                                                "Input tidak valid. Pastikan terdapat 4 angka untuk Jam dan Menit (HHMM)")
                                    
                                    # Ubah kembali ke format 4 digit dengan leading zero jika perlu
                                    input_jam = f"{input_jam:04d}"

                                    # Ambil 2 angka pertama sebagai jam dan 2 angka terakhir sebagai menit
                                    jam = int(input_jam[:2])
                                    menit = int(input_jam[2:])

                                    # Validasi jam (00-23) dan menit (00-59)
                                    if 0 <= jam <= 23 and 0 <= menit <= 59:
                                        input_nilai_baru = f"{jam:02d}:{menit:02d}"  # Format HH:MM
                                        break
                                    else:
                                        print("Input tidak valid. Jam harus antara 00-23 dan Menit antara 00-59.")


                        update_data = konfirmasi(f"Update Data Final {input_kolom} menjadi {input_nilai_baru}? (YA/TIDAK) : ", 
                                                "Input tidak valid. Ketik (YA/TIDAK)")

                        if update_data == "YA": # Update data berdasarkan Kolom yang dipilih
                            find_kendaraan[input_kolom] = input_nilai_baru
                            print(f"\nDATA KENDARAAN DENGAN NO TIKET '{input_tiket_update}' BERHASIL DIUPDATE!.")
                            tampilkan_tabel([find_kendaraan])
                            
                        else:
                            print("\n====================================================================")
                            print("UPDATE [DIBATALKAN]. KEMBALI KE MENU UPDATE DAFTAR PARKIR KENDARAAN.")
                            print("====================================================================")
                            
                    else:
                        print("\n====================================================================")
                        print("UPDATE [DIBATALKAN]. KEMBALI KE MENU UPDATE DAFTAR PARKIR KENDARAAN.")
                        print("====================================================================")

                else:
                    print("\n======================================================================")
                    print(f"❌ NOMOR TIKET '{input_tiket_update}' TIDAK DITEMUKAN. MASUKKAN NOMOR TIKET KEMBALI.")
                    print("======================================================================")
                
        elif MenuKendaraanUpdate == 2:
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar (YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                break
            else:
                pass

        else:
            print("Input tidak valid. Pilih angka dari 1-2.")

def tarif_kendaraan(): # <-------------------- (MENU TAMBAHAN)
    while True:
        print("""\nMENU 5: PEMBAYARAN PARKIR\n
        1. Bayar Parkir
        2. Bayar Denda Parkir (Untuk Tiket yang Hilang)
        3. Keluar\n""") 

        input_menu_tarif = input_int("Masukkan angka Menu yang ingin dijalankan : ", 
                                         "Input tidak valid. Pilih angka dari 1-3.")
        
        if input_menu_tarif == 1: # Fungsi untuk menampilkan seluruh Daftar Parkir Kendaraan

            if not list_kendaraan:
                notif_list_kosong()
            else:
                tampilkan_tabel(list_kendaraan)
                # Masukkan input NO TIKET Daftar Parkir Kendaraan
                while True:
                    inputNoTiket = input_alnum("\nMasukkan [NO TIKET] Parkir Kendaraan : ", 
                                                    "Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.").upper()
                    if len(inputNoTiket) == 6 and inputNoTiket[:2] == "PK" and inputNoTiket[2:].isdigit():
                        break
                    else:
                        print("Input tidak valid. Masukkan input dengan kombinasi huruf 'PK' diawal dan 4 angka setelahnya.")

                # Cek apakah NO TIKET sudah ada di list_kendaraan
                find_kendaraan = None 

                for kendaraan in list_kendaraan: # Cek apakah NO TIKET sudah ada di list_kendaraan
                    if kendaraan["NO TIKET"] == inputNoTiket:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    # Tampilkan Daftar Parkir Kendaraan berdasarkan PLAT Nomor
                    tampilkan_tabel([find_kendaraan])

                    # Masukkan Jam Keluar Kendaraan
                    while True:
                        input_jamkeluar = input_int("Masukkan Waktu Jam Keluar (CHECKOUT) dengan 4 angka (HHMM = JamMenit) tanpa tanda ':' = ", 
                                                    "Input tidak valid. Pastikan terdapat 4 angka untuk Jam dan Menit (HHMM)")

                        # Paksa input_jamkeluar menjadi 4 digit dengan leading zero jika perlu
                        input_jamkeluar = f"{input_jamkeluar:04d}"

                        # Ambil jam dan menit dari input pengguna
                        jam_keluar = int(input_jamkeluar[:2])
                        menit_keluar = int(input_jamkeluar[2:])

                        # Ambil jam dan menit dari CHECKIN tanpa menggunakan map
                        jam_masuk = int(find_kendaraan["CHECKIN"][:2])
                        menit_masuk = int(find_kendaraan["CHECKIN"][3:])  # Indeks ke-3 karena format "HH:MM"

                        # Validasi jam (00-23) dan menit (00-59)
                        if not (0 <= jam_keluar <= 23 and 0 <= menit_keluar <= 59):
                            print("Input tidak valid. Jam harus antara 00-23 dan Menit antara 00-59.")
                            continue

                        # Pastikan jam keluar harus lebih dari jam masuk
                        if (jam_keluar > jam_masuk) or (jam_keluar == jam_masuk and menit_keluar >= menit_masuk):
                            input_jamkeluar = f"{jam_keluar:02d}:{menit_keluar:02d}"  # Format HH:MM
                            break
                        else:
                            print("Waktu Jam Keluar harus lebih dari Waktu Jam Masuk. Input Jam Keluar kembali.")

                    # Konversi waktu ke dalam menit
                    total_masuk = (jam_masuk * 60) + menit_masuk
                    total_keluar = (jam_keluar * 60) + menit_keluar

                    # Hitung selisih waktu dalam menit
                    selisih_menit = total_keluar - total_masuk

                    # Hitung tarif parkir
                    if selisih_menit >= 60:
                        tarif = (selisih_menit // 60) * int(find_kendaraan["TARIF/JAM"])
                    else:
                        tarif = 0

                    # Tampilkan total tarif dn waktu
                    print(f"Jam Masuk  : {find_kendaraan['CHECKIN']}")
                    print(f"Jam Keluar : {input_jamkeluar}")
                    print(f"Total Waktu Parkir: {selisih_menit} Menit ({selisih_menit // 60} Jam)")
                    print(f"Total Biaya: Rp{tarif},-")

                    if tarif > 0:
                        while True:
                            input_uang = input_int("\nMasukkan Jumlah Uang pembayaran: Rp",
                                               "Input tidak valid. Masukkan hanya angka untuk Jumlah Uang")
                        
                            if input_uang >= tarif:
                                print("Terima kasih")
                                print(f"\nUang kembali anda: Rp{input_uang - tarif},-")
                                break
                            else:
                                print("Mohon Maaf")
                                print(f"\nUang Anda kurang: Rp{abs(tarif- input_uang)},-")
                    else:
                        print("\nTerima kasih")

                else:
                    print("\n======================================================================")
                    print(f"❌ NOMOR TIKET '{inputNoTiket}' TIDAK DITEMUKAN. MASUKKAN NOMOR TIKET KEMBALI.")
                    print("======================================================================")

        elif input_menu_tarif == 2: 

            if not list_kendaraan:
                notif_list_kosong()
            else:
                tampilkan_tabel(list_kendaraan)
                # Masukkan input PLAT Nomor Daftar Parkir Kendaraan
                inputPlatNo = input_alnum("\nMasukkan [PLAT] Nomor Kendaraan (Tanpa Spasi): ", 
                                           "Input tidak valid. Masukkan input dengan kombinasi huruf dan angka untuk [PLAT] Nomor.").upper()

                # Cek apakah NO TIKET sudah ada di list_kendaraan
                find_kendaraan = None 

                for kendaraan in list_kendaraan: # Cek apakah NO TIKET sudah ada di list_kendaraan
                    if kendaraan["PLAT"] == inputPlatNo:
                        find_kendaraan = kendaraan
                        break

                if find_kendaraan:
                    # Tampilkan Daftar Parkir Kendaraan berdasarkan PLAT Nomor
                    tampilkan_tabel([find_kendaraan])

                    # Masukkan Jam Keluar Kendaraan
                    while True:
                        input_jamkeluar = input_int("Masukkan Jam Keluar (CHECKOUT) dengan 4 angka (HHMM = JamMenit) tanpa tanda ':' = ", 
                                                    "Input tidak valid. Pastikan terdapat 4 angka untuk Jam dan Menit (HHMM)")

                        # Paksa input_jamkeluar menjadi 4 digit dengan leading zero jika perlu
                        input_jamkeluar = f"{input_jamkeluar:04d}"

                        # Ambil jam dan menit dari input pengguna
                        jam_keluar = int(input_jamkeluar[:2])
                        menit_keluar = int(input_jamkeluar[2:])

                        # Ambil jam dan menit dari CHECKIN tanpa menggunakan map
                        jam_masuk = int(find_kendaraan["CHECKIN"][:2])
                        menit_masuk = int(find_kendaraan["CHECKIN"][3:])  # Indeks ke-3 karena format "HH:MM"

                        # Validasi jam (00-23) dan menit (00-59)
                        if not (0 <= jam_keluar <= 23 and 0 <= menit_keluar <= 59):
                            print("Input tidak valid. Jam harus antara 00-23 dan Menit antara 00-59.")
                            continue

                        # Pastikan jam keluar harus lebih dari jam masuk
                        if (jam_keluar > jam_masuk) or (jam_keluar == jam_masuk and menit_keluar >= menit_masuk):
                            input_jamkeluar = f"{jam_keluar:02d}:{menit_keluar:02d}"  # Format HH:MM
                            break
                        else:
                            print("Waktu Jam Keluar harus lebih dari Waktu Jam Masuk. Input Jam Keluar kembali.")

                    # Konversi waktu ke dalam menit
                    total_masuk = (jam_masuk * 60) + menit_masuk
                    total_keluar = (jam_keluar * 60) + menit_keluar

                    # Hitung selisih waktu dalam menit
                    selisih_menit = total_keluar - total_masuk

                    # Hitung tarif parkir
                    if selisih_menit >= 60:
                        tarif = ((selisih_menit // 60) * int(find_kendaraan["TARIF/JAM"])) + 10000
                    else:
                        tarif = 10000

                    # Tampilkan hasil tarif
                    print(f"Jam Masuk  : {find_kendaraan['CHECKIN']}")
                    print(f"Jam Keluar : {input_jamkeluar}")
                    print(f"Total Waktu Parkir: {selisih_menit} Menit ({selisih_menit // 60} Jam)")
                    print("Denda Tiket Parkir Hilang : Rp10000,-")
                    print(f"Total Biaya: Rp{tarif},-")
                    
                    while True:
                        input_uang = input_int("\nMasukkan Jumlah Uang pembayaran: Rp",
                                            "Input tidak valid. Masukkan hanya angka untuk Jumlah Uang")
                    
                        if input_uang >= tarif:
                            print("Terima kasih")
                            print(f"\nUang kembali anda: Rp{input_uang - tarif},-")
                            break
                        else:
                            print("Mohon Maaf")
                            print(f"\nUang Anda kurang: Rp{abs(tarif- input_uang)},-")
                        
                else:
                    print("\n==========================================================================")
                    print(f"❌ PLAT NOMOR '{inputPlatNo}' TIDAK DITEMUKAN. MASUKKAN PLAT NOMOR KEMBALI.")
                    print("==========================================================================")

        
        elif input_menu_tarif == 3: # Fungsi untuk Keluar dari Daftar Parkir Kendaraan
            # kembali ke menu utama
            exit_daftar = konfirmasi("Yakin ingin keluar (YA/TIDAK)? ",
                                     "Input tidak valid. Ketik (YA/TIDAK)")
            if exit_daftar == "YA":
                break
            else:
                pass

        else:
            print("Input tidak valid. Pilih angka dari 1-3.")


# Perintah Menjalankan Program
main_menu()
