#!/bin/sh
# Syntactically check .htaccess file

rootdir="$(git rev-parse --show-toplevel)"
curdir="$rootdir/.github/redirections"
conffile="$curdir/config"
setupfile="$curdir/.setup"

if [ ! -f "$conffile" ]; then
    echo "No configuration file. See $curdir/README.md" >2
    exit 1
fi

source "$conffile"
if [ -z "$W3ID_PATH" ]; then
    echo "W3ID_PATH is not defined in $conffile" >2
    exit 1
fi
if [ -z "$W3ID_PROJECT" ]; then
    echo "W3ID_PROJECT is not defined in $conffile" >2
    exit 1
fi

if [ ! -f "$setupfile" ]; then
    (cd "$W3ID_PATH/tools/check" && npm ci)
    touch "$setupfile"
fi
(cd "$W3ID_PATH" && node tools/check/bin/w3id-check.js ids/$W3ID_PROJECT)
