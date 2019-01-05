# !/bin/bash

dirname=$1

if [ ! -d "$dirname" ]
then
    mkdir ./$dirname && cd $dirname
    mkdir ./application
    mkdir -p ./application/controllers
    mkdir -p ./application/models
    mkdir -p ./application/static
    mkdir -p ./application/static/css
    mkdir -p ./application/static/js
    mkdir -p ./application/templates
    touch manage.py
    touch requirements.txt
    touch ./application/__init__.py
    touch ./application/app.py
    touch ./application/configs.py
    touch ./application/extensions.py
    touch ./application/controllers/__init__.py
    touch ./application/models/__init__.py
    touch ./application/static/css/style.css
    touch ./application/templates/404.html
    touch ./application/templates/base.html
    echo "File created"
else
    echo "File exists"
fi
