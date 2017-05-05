import random

matris=[]
for x in range(3):
    cur_list=random.sample(range(1, 10), 3)
    matris.extend(cur_list)
cozumler=random.sample(range(1, 10), 3)
x1,x2,x3=0,0,0  # bilinmeyenler
x3=cozumler[2]/matris[8]
x2=(cozumler[1]-matris[5]*x3)/matris[4]
x1=(cozumler[0]-matris[1]*x2-matris[2]*x3)/matris[0]
print(x1,x2,x3)
