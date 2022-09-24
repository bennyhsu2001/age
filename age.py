driving = input('請問你有沒有開過車(Y/N) ')
if driving != 'Y' and driving !='N' :
	print('請輸入 Y or N')
	raise SystemExit

age = input('請問你的年齡是')
age = int(age)

if driving == 'Y':
	if age >= 18 :
		print('你好棒')
	else :
		print('這樣是不可以的喔!!')
elif driving == 'N' :
	if age >= 18 :
		print('可以去考照了')
	else :
		print('加油，再幾年就可以了 !')

