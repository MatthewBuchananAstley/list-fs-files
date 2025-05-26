[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/MatthewBuchananAstley/list-fs-files/badge)](https://securityscorecards.dev/viewer/?uri=github.com/MatthewBuchananAstley/list-fs-files)

# list-fs-files

A python script to list files in a directory on a linux system including the stat information. 

    usage: list-fs-files.py [-h] [-p] [-fnf] [-e] [-j] [-f] [-b] directory

    positional arguments:
      directory

    options:
      -h, --help  show this help message and exit
      -p          Print all scan results
      -fnf        Print filenotfound results
      -e          Print error results
      -j          Print result in json
      -f          Save scan results, filenotfoundlist and errorlist results
      -b          Normal result listing

# Usage

    Git clone https://github.com/MatthewBuchananAstley/list-fs-files.git
    cd list-fs-files
    ./list-fs-files "options" "directory"
 
# Zlib scan result archives

The scan results are saved in a zlib compressed archive.

