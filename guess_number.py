import random
num=random.randint(1,10)
i=0
while i<5:
    ans=int(input("請輸入數字:"))
    if ans == num:
        print("恭喜答對!!!")
        print(i,"times")
        break
    elif ans < num:
        print("bigger")
    elif ans > num:
        print("smaller")
    else:
        print("錯了ㄏㄏ")
    i=i+1