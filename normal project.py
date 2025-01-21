# Gelir Gider Hesaplama

gelir_kaynak = input("Gelirinizin kaynağı nedir? ")
gelir_miktar = int(input(f"{gelir_kaynak} miktarını giriniz: "))

gider_kaynak = input("Giderinizin kaynağı nedir? ")
gider_miktar = int(input(f"{gider_kaynak} miktarını giriniz: "))

print(f"Toplam Gelir: {gelir_miktar} ({gelir_kaynak})")
print(f"Toplam Gider: {gider_miktar} ({gider_kaynak})")