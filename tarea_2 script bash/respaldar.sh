#!/bin/bash
clear #limpiar la pantalla
echo -e '\033[4;34m'Respaldo de carpeta a .tar : Francisco Gonzalez - 2016'\033[0m' #imprime en colores
#'\033[0m': termina de aplicar color (no color)
#'\033[4;34m' ; 34m:color azul 4: subrayado
echo -e '\033[0;44m''\033[1;37m'[Programa iniciado]'\033[0m'
if [ -z "$1" ];then #si el largo de $1 es 0, no se hace nada y se indica el error
	echo -e '\033[0;31m'[Error] Debe indicar como primer parámetro la carpeta que se desee comprimir.'\033[0m'
else
	fecha=$(date +"%d_%m_%Y")
	nombre_comprimido="$fecha"_"$1".tar #nombre que tendrá el archivo tar (incluye la extensión ".tar")
	tar -zcf $nombre_comprimido $1 #comprime y crea el archivo .tar
	if [[ -e $nombre_comprimido ]]; then
		printf "archivo \"$nombre_comprimido\" creado correctamente.\n" #utilize printf para poder imprimir comillas (\")
		if [ -z "$2" ];then #si el largo de $2 es 0, no se mueve el comprimido
			echo "Archivo guardado en este mismo directorio"
		else
			if [[ -d $2 ]]; then #si el directorio de destino existe...
				mv $nombre_comprimido $2 #si se indica el destino, se mueve al destino indicado por el usuario
				echo "Archivo movido a $2"
			else #si no...
				echo -e '\033[0;31m'[Error] Directorio de destino especificado no existe'\033[0m'
				echo "Desea crear el directorio? s/n" #da la posibilidad de crear la carpeta
				read ans
				if [[ "$ans" == "s" ]]; then
					mkdir $2
					echo "creado directorio $2"
					if [[ ! -d $2 ]]; then #verifica nuevamente que la carpeta exista
										 #si no se tienen permisos, puede que la carpeta no se ha creado
						echo "[Error]No se pudo crear la carpeta"
						echo "Archivo guardado en este mismo directorio"
					else
						mv $nombre_comprimido $2 #si se indica el destino, se mueve al destino indicado por el usuario
						echo "Archivo movido a $2"
					fi
				fi
				
			fi
			
		fi
	else
		#En caso de que el archivo comprimido no exista (por la razon que sea), se imprime un error
		echo -e '\033[0;31m'Ocurrio un problema al detectar el archivo comprimido'\033[0m'
	fi
fi
echo -e '\033[0;44m''\033[1;37m'[Programa terminado]'\033[0m'