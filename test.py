height = input("please input your height")
weight = input("please input your weight")

BMI = round(int(weight) / (int(height)/100) ** 2)
print(BMI)