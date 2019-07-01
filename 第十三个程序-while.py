'''while True: # 次循环无法停下来, 死循环
	print("你愁啥")
	print("瞅你咋的")
	print("再瞅一个试试")
	print("试试就试试")
	
print("alex")



# 让用户输入他喜欢的电影. 暂时无限的输入 

while True:
	movie = input("请输入你喜欢的电影是什么, 输入Q退出?")
	if movie == "Q": # = 赋值, == 判断
		break # 打断, 彻底的打断当前本层循环

	print("此人喜欢的电影是:", movie)
	
'''

while True:
	movie = input("请输入你喜欢的电影是什么, 输入Q退出?") # Q
	if movie == "Q": # = 赋值, == 判断
		continue  # 打断, 终止当前本次循环. 继续执行下一次循环 
		

	print("此人喜欢的电影是:", movie)




