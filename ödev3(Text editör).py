import os

# Mevcut txt dosyalarını tara
dosyalar = []
for dosya in os.listdir('.'):
    if dosya.endswith('.txt'):
        dosyalar.append(dosya[:-4])

while True:
    print("\nYapmak istediğiniz işlemi seçiniz:")
    print("1. Dosya aç")
    print("2. Yeni dosya oluştur")
    print("3. Dosyaları listele")
    print("4. Çıkış")

    islem = input("Seçiminiz: ")

    # Dosya oku
    if islem == "1":
        print("Mevcut dosyalar:", dosyalar)
        dosyaadi = input("Dosya adını giriniz: ")

        if dosyaadi + ".txt" in os.listdir('.'):
            dosya = open(dosyaadi + ".txt", 'r', encoding='utf-8')
            icerik = dosya.read()
            dosya.close()
            print(icerik)
        else:
            print("Hata: Dosya bulunamadı!")

    # Dosya yaz
    elif islem == "2":
        dosyaadi = input("Dosya adını giriniz: ")
        metin = input("Metin giriniz: ")

        dosya = open(dosyaadi + ".txt", 'w', encoding='utf-8')
        dosya.write(metin)
        dosya.close()

        if dosyaadi not in dosyalar:
            dosyalar.append(dosyaadi)

        print(dosyaadi + ".txt dosyası oluşturuldu.")

    # Listele ve sil
    elif islem == "3":
        if len(dosyalar) == 0:
            print("Henüz hiç dosya yok.")
        else:
            print("Dosyalar:", dosyalar)

        cevap = input("Dosya silmek ister misiniz? (e/h): ")

        if cevap == "e":
            dosyaadi = input("Silmek istediğiniz dosya adını giriniz: ")

            if dosyaadi in dosyalar:
                os.remove(dosyaadi + ".txt")
                dosyalar.remove(dosyaadi)
                print(dosyaadi + ".txt silindi.")
            else:
                print("Hata: Dosya bulunamadı!")

        elif cevap == "h":
            continue
        else:
            print("Hatalı giriş!")

    # Çıkış
    elif islem == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Hatalı giriş! Lütfen 1-4 arasında bir değer giriniz.")
