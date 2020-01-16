import os
import re
from setuptools import setup

# parse version from package/module without importing or evaluating the code
with open('vagrant/__init__.py') as fh:
    for line in fh:
        m = re.search(r"^__version__ = '(?P<version>[^']+)'$", line)
        if m:
            version = m.group('version')
            break

setup(
    name = 'vagrantpy',
    version = version,
    license = 'MIT',
    description = 'Python bindings for interacting with Vagrant virtual machines.',
    long_description = open(os.path.join(os.path.dirname(__file__),
                                         'README.md')).read(),
    long_description_content_type = 'text/markdown',
    keywords = 'python virtual machine box vagrant virtualbox vagrantfile',
    url = 'https://github.com/vagrantpy/vagrantpy',
    author = 'Todd Francis DeLuca',
    author_email = 'todddeluca@yahoo.com',
    maintainer = 'David McCheyne',
    maintainer_email = 'davidmccheyne@gmail.com',
    classifiers = ['License :: OSI Approved :: MIT License',
                   'Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                  ],
    packages = ['vagrant'],
)
