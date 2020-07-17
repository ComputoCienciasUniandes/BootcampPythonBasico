#Suponga que tiene dos enteros A y B que representan fechas.

#La fecha 7 de enero del 2020 se representaría de la forma 20200107. Es decir, los cuatro primeros dígitos de la izquierda corresponden al año, los siguientes dos al mes (con un cero por delante si el mes es anterior a octubre) y los últimos dos digitos al día del mes (con un cero por delante si el día es menor que 10). 

#Escriba un programa de python que:

# 1. Asigne al entero A la fecha de su nacimiento. (Simplemente A=19901010, por ejemplo)

#2. Le asigne al entero B la fecha de hoy (16 de julio del 2020). 

#3. A partir de operaciones sobre A y B le asigne a un entero C el número de meses que han pasado entre la fecha A y la fecha B.

#4. Imprima A, B y C.

#Solamente son permitidas las operaciones en python que aparezcan en los videos 00, 01, 02 y 03 de la playlist del curso. 
#El programa debe funcionar correctamente si se cambian A y B a cualquier otra fecha entre el año 1 y el año 9999.

A = 19811014
B = 20200716


A_year = A//10000 # esto saca el año
A_month =  (A//100)%100 # esto saca el mes 
A_all_months = 12*A_year + A_month # esta es la cantidad de meses que han pasado desde la fecha 0

B_year = B//10000
B_month =  (B//100)%100
B_all_months = 12*B_year + B_month

C = B_all_months - A_all_months
print(A, B, C)
