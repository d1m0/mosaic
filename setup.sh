#! /usr/bin/env bash

if [[ $# -ne 1 ]] ; then
    echo "Usage $0 <target-directory>"
      exit -1
    fi

if [ ! -d "$1" ] ; then
    echo "Directory $1 does not exist. Creating..."
    mkdir $1
fi

MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR="$( cd $1 && pwd )"


virtualenv $DIR

source $DIR/bin/activate

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

deactivate

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

wget http://blueimp.github.io/JavaScript-Load-Image/js/load-image.all.min.js
wget http://blueimp.github.io/JavaScript-Canvas-to-Blob/js/canvas-to-blob.min.js
popd

echo "export PATH=\$PATH:$MYDIR/node_modules/.bin/" >> $DIR/bin/activate
echo "To begin developing run source $DIR/bin/activate and then make"
