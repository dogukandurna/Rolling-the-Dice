from operator import truediv
import random

yüzey=[1,2,3,4,5,6]

zarsayısı=int(input('Kaç tane zar atmak istiyorsunuz?'))

i=0
while i<zarsayısı:
    secilenyüz=random.choice(yüzey)
    print(secilenyüz)
    i+=1

input("ENTER tuşuna basarak çıkış yapabilirsiniz...")