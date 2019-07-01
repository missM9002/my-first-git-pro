gender = input("请问你是男的还是女的??")

if gender == "女":
	age = input("你多大了??")
	if int(age) > 18 and int(age) < 28:
		print("开门, 来吧, 我家的西瓜又大又甜!!")
	else: # 前提条件是女
		print("去隔壁,隔壁太白在隔壁")
else:
	print("去对面, wusir在对面等你一晚了.")
	