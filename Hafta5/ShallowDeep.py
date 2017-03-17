class Sinifim:
  def _init_(self):
    self.x=[]
  def ekle(self,eklenecek):
    self.x.append(eklenecek) #Ekleme sıralı oluyor ve bir hesap olmadığı için O(1)
  
a=Sinifim() # Nesne oluşumu tek işlem O(1)
b=Sinifim()
c=Sinifim()

a.ekleme(1) 
b.ekleme(2)
c.ekleme(3)

a=b #Nesneleri birbirine atarken shallow kopyalama oluyor O(1)

print("Nesne idleri:" , "a = " , id(a) , "b = " , id(b))
print("Nesneler aynı yeri mi gösteriyor? ",a is b)

a.ekleme(4)

# Alt kısımda nesnelerin kopyalanmadığı aynı yeri gösterdiği gösterilmiştir. 
print("Nesne idleri:" , "a = " , id(a) , "b = " , id(b))
print("Nesneler aynı yeri mi gösteriyor? ",a is b)
print(a.x,b.x) 

# Karmaşıklık O(1) olarak bulunmuştur.
