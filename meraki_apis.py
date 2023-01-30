#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import time
import requests
import urllib3
import os

from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

# Meraki
MERAKI_URL = "https://api.meraki.com"
MERAKI_API_KEY = 'Meraki API key'
MERAKI_SW_SN = 'Meraki SW serial number'


urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def update_interface_admin(switch_sn, port_id, admin_status):
    """
    This function will update the interface admin status
    :param switch_sn: Meraki switch serial number
    :param port_id: switch port id
    :param admin_status: interface admin status: 'DOWN', 'UP'
    :return: list with all the devices
    """
    if admin_status == 'DOWN':
        enable_value = False
    else:
        enable_value = True
    url = MERAKI_URL + '/api/v1/devices/' + switch_sn + '/switch/ports/' + port_id
    payload = {'enabled': enable_value,
               'poeEnabled': enable_value}
    header = {'content-type': 'application/json', 'X-Cisco-Meraki-API-Key': MERAKI_API_KEY}
    enable_interface = requests.put(url, data=json.dumps(payload), headers=header, verify=False)
    enable_interface_json = enable_interface.json()
    return enable_interface_json


