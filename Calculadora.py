import os

Suma= 0

Resta= 0

Multi= 0

Div= 0

print("\t\t\tCalculadora")

print("\n1-Suma")

print("2-Resta")

print("3-Multiplicación")

print("4-División")

print("5-Salir")

Pregunta1= int(input("\nElija una opción: "))

os.system("clear")

if Pregunta1== 1:
	
	while True:
		
		print("\t\t\tSuma")
		
		N= int(input("\nIngrese un número: "))
		
		Suma= Suma+N
		
		Pregunta2= input("\n¿Desea ingresar otro número? (s/n): ")
		
		os.system("clear")
		
		if Pregunta2== 'n' or Pregunta2== 'N':
			
			print("La suma, es: ", Suma)
			
			break

elif Pregunta1== 2:
		
	print("\t\t\tResta")
		
	N= int(input("\nIngrese un número: "))
	
	N2= int(input("Ingrese otro número: "))
	
	Resta= N-N2
		
	os.system("clear")
		
	print("La resta, es: ", Resta)
			
elif Pregunta1== 3:
	
	while True:
		
		print("\t\t\tMultiplicación")
		
		N= int(input("\nIngrese un número: "))
		
		Multi= Multi*N
		
		Pregunta2= input("\n¿Desea ingresar otro número? (s/n): ")
		
		os.system("clear")
		
		if Pregunta2== 'n' or Pregunta2== 'N':
			
			print("La multiplicación, es: ", Multi)
			
			break

elif Pregunta1== 4:
	
	print("\t\t\t\tDivisión")
		
	N= int(input("\nIngrese un número: "))
		
	N2= int(input("Ingrese otro número: "))
		
	Div= N/N2
		
	os.system("clear")
			
	print("La multiplicación, es: ", Div)

elif Pregunta1==5:
	
	exit