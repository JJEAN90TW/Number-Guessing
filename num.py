import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('猜一個數字')
    num = int(num)
    if num == r:
        print('猜對！！')
        print('最後一次是你猜的第', count, '次')
        break
    elif num > r:
        print('再試試看，答案比你猜的小')
    elif num < r:
        print('再試試看，答案比你猜的大')
    print('這是你猜的第', count, '次')