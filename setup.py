#!/usr/bin/env python
from distutils.core import setup

setup(name='proxmox-cli',
      version="1.0",
      description="control proxmox with cli",
      install_requires=open("requirements.txt").read().splitlines()
     )
