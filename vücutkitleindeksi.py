def vki_hesapla(boy, kilo):
    # Boyu metre cinsinden alıyoruz, o yüzden boyu 100'e bölüyoruz
    boy_metre = boy / 100
    vki = kilo / (boy_metre ** 2)
    return vki

while True:
    print("Vücut Kitle İndeksi Hesaplama Programı")
    print("Çıkış yapmak için 0'a basın.")

    try:
        boy = float(input("Boyunuzu (cm olarak) girin: "))
        if boy == 0:
            break
        kilo = float(input("Kilonuzu girin (kg olarak): "))
        if kilo == 0:
            break

        vki = vki_hesapla(boy, kilo)
        print(f"Vücut Kitle İndeksiniz: {vki:.2f}")
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")
