
num1 = 38
num2 = 11
num3 = 0
num4 = 98947

def summ(num):
	cislo_str = str(num)
	arr_simbol = []
	for i in cislo_str:
		arr_simbol.append(i)
	
	process = ''
	itog = 0
	for i in arr_simbol:
		itog += int(i)
		process += str(i)

	print_process = list(process)
	print_finaly = " + ".join(print_process)
	
	print("Итог: " +  str(itog),"Процесс: " + print_finaly)
	

summ(num1)
summ(num2)
summ(num3)
summ(num4)


