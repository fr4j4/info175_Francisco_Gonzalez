#! /bin/bash
num1=2
num2=2
echo "numero1:"
read num1
echo "numero2:"
read num2
#if
if [ $num1 == $num2 ]; then
	echo "son iguales"
elif [ $num1 > $num2 ]; then
	echo "numero1 es mayor que numero2"
elif [ $num1 < $num2 ]; then
	echo "numero2 es mayor que numero1"
fi
