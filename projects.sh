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

    # - install laravel and homestead, script in vagrant file
    vagrant provision

    rm bootstrap.sh

    # add landrush to Vagrant config
    sed "s/http:\/\/localhost/$NAME.dev" .env
    # REALLY, ADD LANDRUS TO VAGRANT!!!

    # - change vagrant file to homestead
    # rm Vagrantfile
    # cp $SCRIPT_DIR/template/laravel-vagrantfile-2 $PROJ_DIR/Vagrantfile

    # some error here. Dunno what exactly
    $SCRIPT_DIR/homestead.sed $PROJ_DIR/Homestead.yaml | sed "s/NAME/$NAME/" > $PROJ_DIR/Homestead.yaml.tmp
    rm $PROJ_DIR/Homestead.yaml
    mv $PROJ_DIR/Homestead.yaml.tmp $PROJ_DIR/Homestead.yaml

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
