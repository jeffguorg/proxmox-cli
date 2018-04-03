#!/usr/bin/env python
from distutils.core import setup
setup(name='proxmox-cli',
      version="1.0",
      packages=["proxmoxcli"],
      description="control proxmox with cli",
      url="https://github.com/jeffguorg/proxmox-cli",
      scripts=["proxmoxcli/bin/proxmox"],
      install_requires=open("requirements.txt").read().splitlines(),
     )
