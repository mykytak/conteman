#!/bin/bash

# chkName name
# if [-f name]

# projects name add (add to gitlab etc.)
# projects name new type
# projects name archive
# projects name open (firefox profile)

# $2: new|archive|start

# get truly script directory
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
    SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
    SOURCE="$(readlink "$SOURCE")"
    [[ $SOURCE != /* ]] && SOURCE="$SCRIPT_DIR/$SOURCE"
done
SCRIPT_DIR="$( cd "$( dirname "$SOURCE" )" && pwd )"

function laravel {
# new: $3: lar|wp
#   lar:
    # - create base composer file

    mkdir $PROJ_DIR
    cd $PROJ_DIR

    # - create vagrant file
    cp $SCRIPT_DIR/template/laravel-vagrantfile-1 $PROJ_DIR/Vagrantfile
    sed -i "s/HOSTNAME/$NAME.dev/" $PROJ_DIR/Vagrantfile

    # - install laravel and homestead, script in vagrant file
    # there mign be an error if this is fresh installation. Need to check all from start.
    vagrant provision

    rm bootstrap.sh

    # add landrush to Vagrant config
    sed "s/http:\/\/localhost/$NAME.dev" .env
    # REALLY, ADD LANDRUSH TO VAGRANT!!!

    # - change vagrant file to homestead
    # rm Vagrantfile
    # cp $SCRIPT_DIR/template/laravel-vagrantfile-2 $PROJ_DIR/Vagrantfile

    # some error here. Dunno what exactly
    # change paths to proj dir, fix names
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
}

# function new()
# function archive()
# function open()

function wordpress {
    mkdir PROJ_DIR
    cd PROJ_DIR
}




# create project dir
# create right composer file
# install composer
# fill database (get default sql, probably from wp-admin installation script)
# move wp-config and wp-content up one folder
# sed wp-config
# update database for new wp site url


case $1 in
    'new')
        case $2 in
            'laravel')
                if [[ -z "${3// }" ]]; then
                    echo "Project name cannot be empty. Aborted."
                    exit
                fi

                NAME=$3
                PROJ_DIR=/home/xedar/devel/$NAME

                laravel
                ;;
        esac
        ;;
esac
