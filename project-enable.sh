# get truly script directory
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
    SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
    SOURCE="$(readlink "$SOURCE")"
    [[ $SOURCE != /* ]] && SOURCE="$SCRIPT_DIR/$SOURCE"
done
SCRIPT_DIR="$( cd "$( dirname "$SOURCE" )" && pwd )"


# $1 -> project name

# open existing project
# go to project dir (~/devel/proj_name)
# open firefox profile
# run vagrant
# open sublime project
# save pids for fox and sublime

# new project
# create vagrant
# create new fox profile
# create new sublime project
# create git
# create bitbucket (?)
# new trello/jira board (?)

# archive project
# move all to bitbucket
# move all to some archive folder (files dir, fox profile, sublime project)
# remove fox profile from available
