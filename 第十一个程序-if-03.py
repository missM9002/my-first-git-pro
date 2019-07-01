score = input("请输入你考试成绩:")

# 100

if int(score) >= 90:
	print("优秀") # 如果有一个条件成立了. 其他的判断就不存在了
elif int(score) >= 80:
	print("良好")
elif int(score) >= 70:
	print("中等")
elif int(score) >= 60:
	print("及格")
else:
	# 收尾. 以上条件都不成立
	print("不及格")
	
	

