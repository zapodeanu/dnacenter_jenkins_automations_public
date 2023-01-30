#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2022 Cisco and/or its affiliates.
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
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import os
import time
import requests
import urllib3
import json
import sys
import logging
import datetime
import yaml

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from dotenv import load_dotenv
from dnacentersdk import DNACenterAPI
from datetime import datetime
from pprint import pprint
from requests.auth import HTTPBasicAuth  # for Basic Auth

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

load_dotenv('environment.env')

DNAC_URL = os.getenv('DNAC_URL')
DNAC_USER = os.getenv('DNAC_USER')
DNAC_PASS = os.getenv('DNAC_PASS')

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def get_dnac_token(dnac_auth):
    """
    Create the authorization token required to access Cisco DNA Center
    Call to Cisco DNA Center - /api/system/v1/auth/login
    :param dnac_auth - Cisco DNA Center Basic Auth string
    :return Cisco DNA Center Token
    """
    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    response_json = response.json()
    dnac_jwt_token = response_json['Token']
    return dnac_jwt_token


def create_fabric_site(site_hierarchy, dnac_token):
    """
    This function will create a new fabric at the site with the hierarchy {site_hierarchy}
    :param site_hierarchy: site hierarchy, for example {Global/OR/PDX-1/Floor-2}
    :param dnac_token: Cisco DNA Center auth token
    :return: response in JSON
    """
    payload = {
        "siteNameHierarchy": site_hierarchy
    }
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/fabric-site'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def add_edge_device(device_ip, site_hierarchy, dnac_token):
    """
    This function will add the device with the management IP address {device_ip}, as an edge device, to the fabric at
    the site with the hierarchy {site_hierarchy}
    :param device_ip: device management IP address
    :param site_hierarchy: fabric site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: API response
    """
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/edge-device'
    payload = {
        'deviceManagementIpAddress': device_ip,
        'siteNameHierarchy': site_hierarchy
    }
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def add_control_plane_node(device_ip, site_hierarchy, dnac_token):
    """
    This function will add the device with the management IP address {device_ip}, as a control-plane node to the fabric
    at the site with the hierarchy {site_hierarchy}
    :param device_ip: device management IP address
    :param site_hierarchy: fabric site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: API response
    """
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/control-plane-device'
    payload = {
        'deviceManagementIpAddress': device_ip,
        'siteNameHierarchy': site_hierarchy
    }
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def add_border_device(payload, dnac_token):
    """
    This function will add a new border mode device to fabric
    :param payload: the required payload per the API docs
    :param dnac_token: Cisco DNA Center auth token
    :return: API response
    """
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/border-device'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def create_l3_vn(l3_vn_name, site_hierarchy, dnac_token):
    """
    This function will create a new L3 virtual network with the name {l3_vn_name} at the site
    with the hierarchy {site_hierarchy}
    :param l3_vn_name: L3 VN name
    :param site_hierarchy: site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: API response
    """
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/virtual-network'
    payload = {
        'virtualNetworkName': l3_vn_name,
        "siteNameHierarchy": site_hierarchy
    }
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def create_auth_profile(auth_profile, site_hierarchy, dnac_token):
    """
    This function will create a new default auth profile for the fabric at the {site_hierarchy}
    :param auth_profile: auth profile, enum { No Authentication , Open Authentication, Closed Authentication, Low Impact}
    :param site_hierarchy: site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: API response
    """
    url = DNAC_URL + '/dna/intent/api/v1/business/sda/authentication-profile'
    payload = {
        'siteNameHierarchy': site_hierarchy,
        "authenticateTemplateName": auth_profile
    }
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json


def main():
    """
    This app will create a new fabric at the site specified in the param provided.
    """

    # logging basic
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('  App "create_fabric.py" run start, ' + current_time)

    with open('fabric_info.yml', 'r') as file:
        project_data = yaml.safe_load(file)

    # parse the input data
    area_name = project_data['area_info']['name']

    building_name = project_data['building_info']['name']

    floor_name = project_data['floor_info']['name']

    site_hierarchy = 'Global/' + area_name + '/' + building_name + '/' + floor_name

    device_ips = project_data['devices_info']['device_ips']

    ip_transit_pool_name = project_data['ip_transit_pool']['name']

    l3_vn_name = project_data['l3_vn']['name']

    border_device_ip = project_data['border_devices']['ip'][0]
    routing_protocol = project_data['border_devices']['routing_protocol']
    internal_bpg_as = str(project_data['border_devices']['internal_bgp_as'])
    external_bpg_as = str(project_data['border_devices']['external_bgp_as'])
    external_interface_name = project_data['border_devices']['external_interface']
    transit_network = project_data['border_devices']['transit_network']
    transit_vlan = str(project_data['border_devices']['transit_vlan'])

    control_plane_device_ips = project_data['control_plane_devices']['ip']
    edge_device_ips = project_data['edge_devices']['ip']

    default_auth_profile = project_data['auth_profile']['name']

    # Create a DNACenterAPI "Connection Object"
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.2.3', verify=False)

    # get Cisco DNA Center Auth token
    dnac_auth = get_dnac_token(DNAC_AUTH)

    # create a new fabric at site
    logging.info('  Creating new fabric at site:' + site_hierarchy)
    response = create_fabric_site(site_hierarchy, dnac_auth)
    time.sleep(15)

    # assign Layer 3 VN to fabric
    logging.info('  Assign L3 Virtual Network: ' + l3_vn_name)
    response = create_l3_vn(l3_vn_name, site_hierarchy, dnac_auth)
    time.sleep(5)

    # add auth profile to fabric
    logging.info('  Adding default auth profile to fabric: ' + default_auth_profile)
    response = create_auth_profile(default_auth_profile, site_hierarchy, dnac_auth)
    time.sleep(5)

    # add control plane node to fabric
    for device_ip in control_plane_device_ips:
        logging.info('  Adding control plane devices to fabric: ' + device_ip)
        response = add_control_plane_node(device_ip, site_hierarchy, dnac_auth)
        time.sleep(2)
    time.sleep(5)

    # add border node to fabric
    logging.info('  Adding a border node device: ' + border_device_ip)
    border_payload = {
        'deviceManagementIpAddress': border_device_ip,
        'siteNameHierarchy': site_hierarchy,
        'externalDomainRoutingProtocolName': routing_protocol,
        'externalConnectivityIpPoolName': ip_transit_pool_name,
        'internalAutonomouSystemNumber': internal_bpg_as,
        'borderSessionType': 'External',
        'connectedToInternet': True,
        'externalConnectivitySettings': [
            {
                'interfaceName': external_interface_name,
                'externalAutonomouSystemNumber': external_bpg_as,
                'l3Handoff': [
                    {
                        'virtualNetwork': {
                            'virtualNetworkName': l3_vn_name,
                            'vlanId': transit_vlan
                        }
                    }
                ]
            }
        ]
    }
    response = add_border_device(border_payload, dnac_auth)
    time.sleep(5)

    # add edge node devices to fabric
    for device_ip in edge_device_ips:
        logging.info('  Adding edge node devices to fabric: ' + device_ip)
        response = add_edge_device(device_ip, site_hierarchy, dnac_auth)
        time.sleep(2)
    time.sleep(5)

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "create_fabric.py" end, : ' + date_time)


if __name__ == '__main__':
    sys.exit(main())

