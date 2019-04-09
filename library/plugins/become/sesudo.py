# -*- coding: utf-8 -*-
# Copyright (c) 2018, Michael Hatoum <michael@adaltas.com>
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    become: sesudo
    short_description: CA Privileged Access Manager (by sesudo exec)
    description:
        - This become plugins allows your remote/login user to execute commands as another user via the sesudo utility.
    author: michael@adaltas.com
    options:
        become_exe:
            description: sesudo executable
            default: /opt/seos/bin/sesudo
            ini:
              - section: privilege_escalation
                key: become_exe
            vars:
              - name: ansible_become_exe
            env:
              - name: ANSIBLE_BECOME_EXE
        become_flags:
            description: Options to pass to sesu
            default: SU-
            ini:
              - section: privilege_escalation
                key: become_flags
            vars:
              - name: ansible_become_flags
            env:
              - name: ANSIBLE_BECOME_FLAGS
"""

from ansible.plugins.become import BecomeBase


class BecomeModule(BecomeBase):

    name = '/opt/seos/bin/sesudo'
    command = 'SU-'

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        become = self.get_option('become_exe') or self.name
        flags = self.get_option('become_flags') or self.command

        return '%s %s -c %s' % (become, flags, self._build_success_command(cmd, shell))
