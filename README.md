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

# Installation

[Release v1.3.0](https://github.com/MatthewBuchananAstley/list-fs-files/releases/tag/v-test-20250623-170339) 

First check the signature of the signed package.

Import the public signing key from the repository:

    curl https://raw.githubusercontent.com/MatthewBuchananAstley/list-fs-files/refs/heads/master/Automated_Release_Signing_Key.pub | gpg --import 

Or from the keys.openpgp.org keyserver with "keyserver hkps://keys.openpgp.org" in ~/.gnupg/gpg.conf:

    $gpg --search-keys "ci@astley.nl"
    gpg: data source: https://keys.openpgp.org:443
    (1)	CI Release Bot (Automated Release Signing Key) <ci@astley.nl>
	  4096 bit RSA key B958339F1229A6EE, created: 2025-06-19

    $gpg --verify list-fs-files-1.3.0-1.el9.noarch.rpm.sig list-fs-files-1.3.0-1.el9.noarch.rpm
    gpg: Signature made Mon 23 Jun 2025 13:58:31 CEST
    gpg:                using RSA key 5E3097F9AF5D0E9B1DB0641FB958339F1229A6EE
    gpg: Good signature from "CI Release Bot (Automated Release Signing Key) <ci@astley.nl>" [ultimate]

    $sha256sum vop-1.4.0-1.el9.noarch.rpm
     016c8eb457c17d45f953c9118e3a7e881e160378aeede1aedf0005fed0b9f07e
     sha256:016c8eb457c17d45f953c9118e3a7e881e160378aeede1aedf0005fed0b9f07e 

If the signatures are good the latest release can be installed on rpm based systems:

    $sudo rpm -ivh https://github.com/MatthewBuchananAstley/list-fs-files/releases/download/v-test-20250623-170339/list-fs-files-1.3.0-1.el9.noarch.rpm 

Or the application can be downloaded via the git clone command:

    $git clone https://github.comm/MatthewBuchananAstley/vop.git

# Usage

    Git clone https://github.com/MatthewBuchananAstley/list-fs-files.git
    cd list-fs-files
    ./list-fs-files "options" "directory"
 
# Zlib scan result archives

The scan results are saved in a zlib compressed archive.

