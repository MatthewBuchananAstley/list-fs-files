% list-fs-files(SECTION) | User Commands
%
% "June 25 2025"

[comment]: # The lines above form a Pandoc metadata block. They must be
[comment]: # the first ones in the file.
[comment]: # See https://pandoc.org/MANUAL.html#metadata-blocks for details.

[comment]: # pandoc -s -f markdown -t man package.md -o package.1
[comment]: # 
[comment]: # A manual page package.1 will be generated. You may view the
[comment]: # manual page with: nroff -man package.1 | less. A typical entry
[comment]: # in a Makefile or Makefile.am is:
[comment]: # 
[comment]: # package.1: package.md
[comment]: #         pandoc --standalone --from=markdown --to=man $< --output=$@
[comment]: # 
[comment]: # The pandoc binary is found in the pandoc package. Please remember
[comment]: # that if you create the nroff version in one of the debian/rules
[comment]: # file targets, such as build, you will need to include pandoc in
[comment]: # your Build-Depends control field.

[comment]: # lowdown is a low dependency, lightweight alternative to
[comment]: # pandoc as a markdown to manpage translator. Use with:
[comment]: # 
[comment]: # package.1: package.md
[comment]: #         lowdown -s -Tman -o $@ $<
[comment]: # 
[comment]: # And add lowdown to the Build-Depends control field.

[comment]: # Remove the lines starting with '[comment]:' in this file in order
[comment]: # to avoid warning messages.

# NAME

list-fs-files - A python script to list files in a directory on a linux system including the stat information. 

# SYNOPSIS

**list-fs-files.py** [ **-h** ] [ **-p** ] [ **-fnf** ] [ **-e** ] [ **-j** ] [ **-f** ] [ **-b** ] _directory_ 

# DESCRIPTION

**list-fs-files** is a Python utility designed to scan and analyze the contents of a specified file system directory. It can report various aspects of the scan, including all found files, files that were not found (e.g., due to permission issues or being removed during scan), and errors encountered during the process. The results can be printed to the console or saved to files, and can also be formatted as JSON for programmatic use.

# OPTIONS

The program follows the usual command line syntax, with long options starting with two dashes ('--'). A summary of options is included below.

* **-h**, **--help**
    : Show the help message and exit. This displays a brief overview of the command's usage and options.

* **-p**
    : Print all scan results to standard output. This includes successful file listings and any other information gathered during the scan.

* **-fnf**
    : Print a list of files that were not found during the scan to standard output. This can occur for various reasons, such as files being moved, deleted, or inaccessible due to permissions.

* **-e**
    : Print a list of errors encountered during the file system scan to standard output. This helps in diagnosing issues like permission denied, inaccessible directories, or other system-level problems.

* **-j**
    : Print the scan results in JSON (JavaScript Object Notation) format. This is useful for integrating the output with other scripts or applications for automated processing.

* **-f**
    : Save the scan results, including the list of files found, the list of files not found, and the error list, to separate output files. The specific filenames will typically be derived from the input directory or a default pattern.

* **-b**
    : Perform a normal result listing. This is often the default behavior or a more concise output format compared to the full scan results (equivalent to not specifying -p, -fnf, -e, -j, or -f).

# POSITIONAL ARGUMENTS

* _directory_
    : The path to the file system directory that the utility should scan and analyze. This argument is mandatory.

# EXAMPLES

Scan the current directory and print all results:

list-fs-files.py -p .

Scan a specific directory and save all results to files:

list-fs-files.py -f /path/to/my/files

Scan a directory and output results in JSON format:

list-fs-files.py -j /var/log

# BUGS

https://github.com/MatthewBuchananAstley/list-fs-files/security/advisories/new

# AUTHOR

root <root@unknown>
: Wrote this manpage for the Debian system.

# COPYRIGHT

Copyright @ 2025 root 

This manual page was written for the Debian system (and may be used by others).

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU General Public License, Version 2 or (at your option)
any later version published by the Free Software Foundation.

On Debian systems, the complete text of the GNU General Public License
can be found in /usr/share/common-licenses/GPL.

[comment]: #  Local Variables:
[comment]: #  mode: markdown
[comment]: #  End:
