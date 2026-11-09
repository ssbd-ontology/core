#!/bin/sh
# Test redirection rules
set -e

rootdir="$(git rev-parse --show-toplevel)"
curdir="$rootdir"/.github/redirections
conffile="$curdir"/config

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


# Start w3id redirection service
(cd "$W3ID_PATH"/tools/server && docker compose up -d)

# Define and register cleanup command
cleanup() {
    (cd "$W3ID_PATH"/tools/server && docker compose down)
}
trap cleanup EXIT


"$W3ID_PATH"/tools/server/bin/resolve-identifier $W3ID_PROJECT

redirectioncheck "$curdir"/expected_redirections.yaml


# Ensure to trigger cleanup
exit
