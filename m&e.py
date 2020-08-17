E = int(input("輸入英文成績:"))
M = int(input("輸入數學成績:"))

if E >= 0 and M >= 0 and E <= 100 and M <= 100:
    if E >=90 and M >=90:
        print("幹的好,有獎品!")
    elif E <=60 and M <=60:
        print("幹的好,有處罰!!!")
    elif  M <=60 or  E <=60:
        print("幹的好,再加油!!")
    else: 
        print("隨便啦,沒獎品喇")   
else: 
        print("幹的好,輸入錯誤!!!!") 
    