#!/usr/bin/env python

# TODO:
# -h help
# warn when running stale kernel (current kernel is not latest)

import re
import subprocess

def main():
    kernel_packages = list_all_installed_kernel_packages()
    current_kernel_version = get_current_kernel_version()
    old_kernel_packages = filter_old_kernel_packages(kernel_packages,
            current_kernel_version)
    output(old_kernel_packages)

KERNEL_PACKAGE_REGEX = re.compile(r'linux-(image|headers)-\d+.\d+.\d+')

def list_all_installed_kernel_packages():
    dpkg_output = run_command('dpkg-query',
            '--show',
            '--showformat=${binary:Package}\t${Version}\t${Status}\n',
            'linux-*').split('\n')
    installed_packages = [line.split('\t')[0:2]
            for line in dpkg_output
            if line.endswith('ok installed')]
    return [(package, get_version(version))
            for (package, version) in installed_packages
            if KERNEL_PACKAGE_REGEX.match(package)]

def get_current_kernel_version():
    kernel_version = run_command('uname', '-r')
    return get_version(kernel_version)

def filter_old_kernel_packages(kernel_packages, current_kernel_version):
    return [package for package in kernel_packages
            if package[1] < current_kernel_version]

def output(packages):
    result = ' '.join(line[0] for line in packages)
    print(result)

def get_version(version_string):
    return tuple(int(chunk) for chunk in re.split('[-\.]', version_string)
            if chunk.isdigit())

def run_command(*args):
    return subprocess.check_output(args)

if __name__ == '__main__':
    main()
