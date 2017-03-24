# -*- coding: utf-8 -*-
#import math


#1.Media de tres numeros
def media_Num(valorX, valorY, valorZ):
        media = (float(valorX) + float(valorY) +float(valorZ))/3
        print "La media es:", media

        
#2. Volumen de una esfera
def vol_Esf(radio):
        vol = (1.33 * 3.1416) * (float(radio)**3)
        print "El volumen de la esfera es:", vol

        
#3. Diez numeros impares inciando con en 13 
def impar_N(impar):
        while impar <= 32: 
                 print "Numero Impar:", str(impar) 
                 impar += 2


#4. Obtener el maximo de 3 numeros

def mayor_N(x, y, z):
        if x >= y and x >= z:
                print "Numero Mayor", x
        elif y >= x and y >= z:
                print "Numero Mayor", y
        elif z >= x and z >= y:
                print "Numero Mayor", z

                
#5: Rotar una lista
num = [1,2,3,4,5,6]

def rotar (lst, x):
    guardar = list(lst)
    for i in range(len(lst)):

        if x<0:
            lst[i+x] = guardar[i]
        else:
            lst[i] = guardar[i-x]
        
rotar(num, -5)

print (num)



#6. Realizar un programa que permita generar un intervalo de la suma de los cubos de los primeros n números. 
#Ejemplo suma = 1 + 8 + 27 + n
def intervaloSuma(x):      
        vacio=[(conta**3) for conta in range(1,x+1)]        
        print vacio
        return sum(vacio)



#7. Realizar un programa que permita generar un intervalo de los cuadrados de n números mayores a 100 (>100).
def intervaloMayor(x):
       vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1


#8. Realizar un programa que permita generar un intervalo de n numeros entre 20 y 60
def intervaloN (x):
        cont=1
        while cont<=x:
                if cont>=20 and cont<=60:
                        print cont
                cont+=1


#9. Realizar un programa que solicite dos argumentos de tipo Double para calcular la hipotenusa de un triángulo rectángulo y retorne un valor de tipo Double.        
def hipoT (x, y):
        return math.sqrt(x**2 + y**2)


#10. Crear un programa que por medio de recursión calcule la suma de los cuadrados de n números.
def recursive (dato, variable=0):
        if(dato>=0):
                variable+=dato**2
                return recu(dato-1,variable)
        else:
                print variable



