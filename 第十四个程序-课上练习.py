# 1. 让程序能数数 . 从1 - > 100
'''
print(1)
print(2)
print(3)
print(4)

# ......
i = 1
while True:
	print(i)
	if i >= 100:
		break
	i = i + 1


i = 1
while i <= 100:
	print(i)
	i = i + 1

	
# 除了67都打印
i = 1
while i <= 100:
	if i != 67: # == 等于   !=  不等于
		print(i)
	i = i + 1


i = 1
while i <= 100:
	if i == 67: # == 等于   !=  不等于
		i = i + 1
		continue
	print(i)
	i = i + 1



# 1+2+3+4+5+6+7+....+100 = ?
# 15+6

# 在循环的过程中. 本次运算需要之前所有的数据的运算的结果. 此时需要累加运算 
i = 1
sum = 0 # 求和
while i <= 10010:
	sum = sum + i
	i = i + 1

print(sum)

'''	

# 准备好正确的用户名和密码
usernmae  = "alex"
password = "dsb"
# 登录验证

uname = input("请输入你的用户名:")
upwd = input("请输入你的密码:")
if uname == usernmae and upwd == password:
	print("登录成功!!")
else:
	print("登录失败, 用户名或密码错误!!!")







