from setuptools import setup, find_packages

version = '1.0.0'
name = 'ubuntu-old-kernel-cleanup'
package_name = name.replace('-', '_')

setup(
    name=name,
    version=version,
    description='Script that helps to remove unused kernels from an Ubuntu '
        '(and possibly also Debian) Linux system',
    author="Mart Somermaa",
    author_email="mrts.pydev at gmail dot com",
    url="http://github.com/mrts/" + name,
    license="MIT",
    packages=find_packages(exclude=['tests']),
    scripts=['bin/' + name + '.py'],
    entry_points={'console_scripts': ['{0}={1}.cleanup:main'.format(name, package_name)]}
)
