import random
r = random.randint(1, 100)
while True:
	num = input('猜一個數字')
	num = int(num)
	if num == r:
	    print('猜對！！')
	    break
	elif num > r:
	    print('再試試看，答案比你猜的小')
	elif num < r:
	    print('再試試看，答案比你猜的大')