#! /bin/bash

VALID_PASSWORD="secret"
echo "Ingrese la password:"
read PASSWD

if [ "$PASSWD" == "$VALID_PASSWORD" ]; then
	echo "Acceso concedido."
else
	echo "Accedo denegado."
fi