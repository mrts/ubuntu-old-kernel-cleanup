# ubuntu-old-kernel-cleanup

Script that helps to remove unused kernels from an Ubuntu (and possibly also
Debian) Linux system.

See [this question from Ask Ubuntu](http://askubuntu.com/questions/401581/bash-one-liner-to-delete-only-old-kernels)
for the original problem.

## Installation

Install the package with `pip`:

    sudo pip install git+http://github.com/mrts/ubuntu-old-kernel-cleanup.git

Verify that the script was installed successfully by running it:

    ubuntu-old-kernel-cleanup

## Running

Do a dry run first to see what would be removed:

    ubuntu-old-kernel-cleanup | xargs sudo apt-get --dry-run purge

Then run the actual cleanup:

    ubuntu-old-kernel-cleanup | xargs sudo apt-get -y purge
