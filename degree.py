degree = input('請輸入華氏或攝氏：')
if degree == '華氏':
	fahrenheit = input('請輸入華氏溫度:')
	fahrenheit = float(fahrenheit)
	celsius = (fahrenheit - 32) * 5 / 9
	print('攝氏溫度:', celsius)

if degree == '攝氏':
	celsius = input('請輸入攝氏溫度:')
	celsius = float(celsius)
	fahrenheit = celsius  * ( 9 / 5 ) + 32
	print('華氏溫度:', fahrenheit)