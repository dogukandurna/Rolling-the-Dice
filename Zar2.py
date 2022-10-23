import random

yüzeysayısı=int(input('Kaç yüzeyli zar atmak istiyorsunuz?'))
flag=True
while flag==True:
    yüzey=random.randint(1,yüzeysayısı)
    print(str(yüzey) +'/' + str(yüzeysayısı))
    yüzeysayısı=int(input('Kaç yüzeyli zar atmak istiyorsunuz?'))