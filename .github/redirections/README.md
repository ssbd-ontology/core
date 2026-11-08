# Check and test redirection rules
This folder contains scripts checking and testing redirection rules.


## Configure
1. Check out the w3id repository locally

    cd /BASE/DIRECTORY/FOR/YOUR/GIT/REPOS
    git clone git@github.com:perma-id/w3id.org.git


2. Add a file called `config` to the current directory with the following content:

   ```bash
   # Path to the checked out w3id directory
   W3ID_PATH="/BASE/DIRECTORY/FOR/YOUR/GIT/REPOS/w3id"

   # Name of the w3id project
   W3ID_PROJECT=ssbd

   # In case you want to change the default port
   #export W3ID_BASE=http://localhost:8080
   ```


## Check .htaccess file syntactically
Make sure that you have `nodejs` installed and run the script

    .github/redirections/check.sh


## Test redirection rules
Make sure that you have `curl` and `docker-compose` installed.

On redhat-based distros, SELinux may block checking the .htaccess file.
If that is the case, run the following commands:

    cd /BASE/DIRECTORY/FOR/YOUR/GIT/REPOS
    sudo semanage fcontext -a -t container_file_t 'ids(/.*)?'
    sudo restorecon -Rv ids

Run the script

    .github/redirections/test.sh
