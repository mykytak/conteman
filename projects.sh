#!/bin/bash

# chkName name
# if [-f name]

# projects name add (add to gitlab etc.)
# projects name new type
# projects name archive
# projects name open (firefox profile)

# $2: new|archive|start


SCRIPT_DIR=$(pwd)

NAME=$1
PROJ_DIR=/home/xedar/devel/$NAME

# new: $3: lar|wp
#   lar:
    # - create base composer file

    mkdir $PROJ_DIR
    cd $PROJ_DIR

    # - create vagrant file
    cp $SCRIPT_DIR/template/laravel-vagrantfile-1 $PROJ_DIR/Vagrantfile
    sed -i "s/HOSTNAME/$NAME.dev/" $PROJ_DIR/Vagrantfile

    # - go to /vagrant and install all composer requirements
    touch bootstrap.sh

    cat <<EOF > bootstrap.sh
#/bin/bash

cd /vagrant
composer create-project laravel/laravel repo
mv repo/.[!.]* ./
rmdir repo
composer require --dev laravel/homestead
php vendor/bin/homestead make
php artisan key:generate
EOF

    touch .env
    cat <<EOF > .env
APP_ENV=local
APP_DEBUG=true
APP_KEY=

DB_HOST=localhost
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=secret

CACHE_DRIVER=file
SESSION_DRIVER=file
QUEUE_DRIVER=sync

MAIL_DRIVER=smtp
MAIL_HOST=mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
EOF

    # - up vagrant machine
    vagrant up


    # - shutdown machine
    vagrant halt

    rm bootstrap.sh

    # - change vagrant file

    rm Vagrantfile
    cp $SCRIPT_DIR/template/laravel-vagrantfile-2 $PROJ_DIR/Vagrantfile


    # some error here. Dunno what exactly
    $SCRIPT_DIR/homestead.sed $PROJ_DIR/Homestead.yaml | sed "s/NAME/$NAME/" > $PROJ_DIR/Homestead.yaml.tmp
    rm $PROJ_DIR/Homestead.yaml
    mv $PROJ_DIR/Homestead.yaml.tmp $PROJ_DIR/Homestead.yaml

    touch .gitignore
    cat <<EOF > .env
vendor
.git

EOF

    # - create git initial commit
    git init
    git commit -A -m 'initiate laravel project'

    # - create sublime project

    # (?):
    #     - create gitignore
    #     - create and push to gitlab project

# function new()
# function archive()
# function open()
