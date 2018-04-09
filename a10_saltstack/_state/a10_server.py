# Copyright (C) 2018, A10 Networks Inc. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import salt.config

from acos_client import client

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.loader.grains(__opts__)

ret = {
    'name': 'a10_server',
    'changes': {},
    'result': False,
    'comment': ''
    }

def _get_client():
    host = __grains__['host']
    username = __grains__['username']
    password = __grains__['password']
    port = __grains__['port']
    protocol = __grains__['protocol']
    version = __grains__['version']
    return client.Client(host, version, username, password, port, protocol)

def create(**kwargs):
    try:
        client = _get_client()
        changes = client.slb.server.create(name, host, status)
        ret['result'] = True
        ret['changes'] = changes
    except Exception as e:
        pass
    return ret

def update():
    return ret

def delete(server_name):
    result = client.slb.server.delete(server_name) 
    return ret
