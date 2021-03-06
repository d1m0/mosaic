#! /usr/bin/env bash

MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install flask-uploads
pip install guess_language
pip install flipflop
pip install coverage
pip install google-api-python-client
pip install dropbox
pip install titlecase

if [ ! -d $DIR/third_party ] ; then
  mkdir $DIR/third_party
fi

which node;
if [[ $? -ne 0 ]]; then
  echo "node not found! Please make sure nodejs is installed"
  exit -1
fi

npm install

# Make tmp directory for logs
mkdir $DIR/../tmp

# Install bootstrap
pushd $DIR/../mosaic/static/
wget https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip
unzip bootstrap-3.3.7-dist.zip
rm bootstrap-3.3.7-dist.zip

wget https://code.jquery.com/jquery-3.1.1.min.js
wget https://github.com/blueimp/jQuery-File-Upload/archive/9.12.5.zip
unzip 9.12.5.zip
rm 9.12.5.zip

wget https://jqueryui.com/resources/download/jquery-ui-1.12.1.zip
unzip jquery-ui-1.12.1.zip
rm jquery-ui-1.12.1

wget https://github.com/KidSysco/jquery-ui-month-picker/zipball/master
unzip master
rm master

wget https://unpkg.com/masonry-layout@4.1/dist/masonry.pkgd.min.js

wget http://gsgd.co.uk/sandbox/jquery/easing/jquery.easing.1.3.js

wget http://blueimp.github.io/JavaScript-Load-Image/js/load-image.all.min.js
wget http://blueimp.github.io/JavaScript-Canvas-to-Blob/js/canvas-to-blob.min.js
popd
