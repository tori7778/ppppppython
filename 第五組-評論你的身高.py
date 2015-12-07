
# coding: utf-8

# In[ ]:




# In[21]:

a=int(input("輸入性別(男=1,女=2):"))
b=int(input("輸入身高:"))

if (a==1):
    if (b<165):
        print("矮子")
    elif (b>=165)and(b<170):
        print("不上不下")
    elif(b>=170)and(b<175):
        print("剛剛好(?")
    elif(b>=175)and(b<180):
        print("受歡迎")
    elif(b>=180)and(b<185):
        print("嫁嫁嫁")
    else: 
        print("好可怕")
else:
    if (b<155):
        print("挺可愛")
    elif (b>=155)and(b<160):
        print("女孩樣")
    elif(b>=160)and(b<165):
        print("穿衣剛好")
    elif(b>=165)and(b<170):
        print("大家羨慕")
    elif(b>=170)and(b<175):
        print("名模身高")
    else: 
        print("好可怕")


# In[ ]:



