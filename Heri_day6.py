print ("=====", "Operator Percabangan", "=====")

a = int(input("Masukkan nilai a :"))
operator = str(input("masukkan operator aritmatika :"))
b = int(input("Masukkan nilai b :"))

if operator == "+" :
	hasil = a + b
	print (a, "+", b, "=", hasil)
	
elif operator == "-" :
	hasil = a - b
	print (a, "-", b, "=", hasil)
	
elif operator == "*" :
	hasil = a * b
	print (a, "*", b, "=", hasil)
	
elif operator == "/" :
	hasil = a / b
	print (a, "/", b, "=", hasil)