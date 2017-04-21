import math
x = [2,3,5,9,82,-5,13,3]

def enKucuk(dizi):
    """Karmaşıklığı O(n)"""
    """En kücük elemanı döndüren fonksiyon"""
    kucuk = dizi[0] # Baslangic değeri
    for i in dizi:
        if i < kucuk:
            kucuk = i
    return kucuk
    
def enBuyuk(dizi):
    """Karmaşıklığı O(n)"""
    """En büyük elemanı döndüren fonksiyon"""
    buyuk = dizi[0] # Baslangic değeri
    for i in dizi:
        if i > buyuk:
            buyuk = i
    return buyuk

def ortalamaHesapla(dizi):
    """Karmaşıklığı O(n)"""
    """Dizinin ortalamasını döndüren fonksiyon"""
    return float(sum(dizi)) / max(len(dizi), 1)

print(ortalamaHesapla(x))
print(enKucuk(x))
print(enBuyuk(x))
ortalama = ortalamaHesapla(x)

def varyansHesapla(dizi,ortalama):
  """Karmaşıklığı O(n)"""
  varyansdegeri = 0
  for i in range(len(dizi)):
      varyansdegeri += (ortalama - dizi[i]) ** 2
  return varyansdegeri / len(dizi)

print(varyansHesapla(x,ortalama))

varyans = varyansHesapla(x,ortalama)

def standartSapmaHesapla(varyans):
  """ Math sqrt fonksiyonun karmaşıklığı O(logn) olduğu için
  karmaşıklık O(logn)'dir """
  return math.sqrt(float(varyans))

print(standartSapmaHesapla(varyans))
