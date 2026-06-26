#!/bin/sh

apk update && apk upgrade
#apt update && apt upgrade

REPO="OWNER/REPO"
FILE_TAG="linux-x64.tar.gz"
APP_NAME=""

DOWNLOAD_URL=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" | grep -o '"browser_download_url": *"[^"]*"' | grep "$FILE_TAG" | awk -F'"' '{print $4}')

if [ -z "$DOWNLOAD_URL" ]; then 
	echo "Error: Archivo no encontrado en el repo" 
	exit 1 
fi

FILENAME=$(basename "$DOWNLOAD_URL")

mkdir -p /opt/$APP_NAME
wget $DOWNLOAD_URL

# Modify accordingly if file is packed or not
#tar -xzf $FILENAME --no-same-owner
#
#cp -af <FOLDER_NAME>/* /opt/$APP_NAME
#install <FILE_NAME> /opt/$APP_NAME/$APP_NAME
#
#rm -rf $FILENAME <FOLDER_NAME>

install $FILENAME /opt/$APP_NAME/$APP_NAME
rm -rf $FILENAME

#
# Añadir comando para reiniciar el servicio
#

echo "Actualización completada"
