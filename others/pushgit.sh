#!/bin/bash

FECHA=$(date +'%Y-%m-%d %H-%M-%S')

# sincronzo el directorio local y remoto
git fetch
pull=$(git pull)
git add .

git commit -m "automatico $FECHA"
#git status
git push
# como  no tengo forma de capturar la salida de git push si veo que el ultimo commit tiene la hora en la que se ha ejecutado 
# significa que hemos actualizado el repositorio remoto, por lo que si hemos puesto 1 parametro generamos la pagina y la subimos
push=$(git log -p -1 | grep "$FECHA" | wc -l)

if [ $# -ge 1 ] 
then
	cd generate_pdf/ && python3 generate_pdf.py && cd -
	if [ "$pull" != "Already up-to-date." ] || [ "$push" ==  "1" ]
	then
		make html
		DIR=$(pwd)
		cd "$DIR/output" && bash pushgit.sh >> /tmp/wiki_out.log 2>&1
	fi
fi

