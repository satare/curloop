#!/bin/bash
echo "****************************************"
echo "Installation in progress, please wait..."
echo "****************************************"
echo
echo 'Downloading Binary ...'
cd $(mktemp -d)
curl -sOL https://github.com/satare/curloop/releases/latest/download/curloop.tar.gz
echo 'Uncompressing archive ...'
tar -xzf curloop.tar.gz
echo 'Setting correct execution rights ...'
chmod +x curloop
echo 'moving to /usr/local/bin ...'
mv curloop /usr/local/bin/
echo
echo "**********************"
echo "Installation Complete"
echo "**********************"
echo
curloop -h