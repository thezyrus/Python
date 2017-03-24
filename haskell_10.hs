--  Ejercicio Programacion Logica y Funcional

autor = "Luis Antonio Canul Cauich"

-- Media Aritmetica de Tres Numeros
media3 x y z = (x+y+z)/3

-- Maximo de tres numeros
maximo3 x y z = maximum[x,y,z]

--Volumen de la esfera
volesfera r = (4/3)*pi*r^3

-- 10 numeros impares empezando con el 13
impares = [13,15..32]

-- Rotar lista de numeros
rota1 x y z = rota1.reverse[x,y,z]
rota n x = drop n x ++ take n x
rota3 x = drop 3 x ++ take 3 x

--Suma de cubos de los primero n
intervSuma n=sum [x^3 | x <- [1..n]] 
 
 --intervalos de los cuadrados de n numeros >100
sumMayor n=[x^2 | x <- [1..n], x^2>100] -- llamar al metodo sumMayor n y mandar un apartir del 11 para que imprima su cuadrado

--Intervalo de n numeros entre 20 y 60
intervN n=[x | x <- [20..n], x>= 20, x<=60] -- llamar al metodo interN y mandar un numero a partir del 20 para que imprima un dato

--Calcular la hipotenusa de un triangulo
hipotenusa:: Double -> Double -> Double
hipotenusa x y = sqrt(x^2 + y^2)

-- Suma de los cuadrados de n numeros
sumaNum::Integer->Integer
sumaNum 0=0
sumaNum y = y^2 + sumaNum(y-1)