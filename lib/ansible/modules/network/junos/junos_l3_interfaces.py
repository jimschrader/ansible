#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_l3_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: junos_l3_interfaces
version_added: 2.9
short_description: Manage Layer 3 interface on Juniper JUNOS devices
description: This module provides declarative management of a Layer 3 interface on Juniper JUNOS devices
author: Daniel Mellado (@dmellado)
requirements:
  - ncclient (>=v0.6.4)
notes:
  - This module requires the netconf system service be enabled on the device being managed.
  - This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
  - Tested against JunOS v18.4R1
options:
  config:
    description: A dictionary of Layer 3 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Full name of interface, e.g. ge-0/0/1
        type: str
        required: True
      unit:
        description:
          - Logical interface number. Value of C(unit) should be of type integer
        default: 0
        type: int
      ipv4:
        description:
          - IPv4 addresses to be set for the Layer 3 logical interface mentioned in I(name) option.
            The address format is <ipv4 address>/<mask>. The mask is number in range 0-32
            for example, 192.0.2.1/24, or C(dhcp) to query DHCP for an IP address
        type: list
        elements: dict
        suboptions:
          address:
            description:
              - IPv4 address to be set for the specific interface
            type: str
      ipv6:
        description:
          - IPv6 addresses to be set for the Layer 3 logical interface mentioned in I(name) option.
            The address format is <ipv6 address>/<mask>, the mask is number in range 0-128
            for example, 2001:db8:2201:1::1/64 or C(auto-config) to use SLAAC
        type: list
        elements: dict
        suboptions:
          address:
            description:
              - IPv6 address to be set for the specific interface
            type: str
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted

# Before state:
# -------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 10.200.16.10/24;
#         }
#     }
# }
# ge-0/0/2 {
#     description "non L3 interface";
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members 2;
#             }
#         }
#     }
# }

- name: Delete JUNOS L3 logical interface
  junos_l3_interfaces:
    config:
      - name: ge-0/0/1
      - name: ge-0/0/2
  state: deleted

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "deleted L3 interface";
# }
# ge-0/0/2 {
#     description "non L3 interface";
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members 2;
#             }
#         }
#     }
# }


# Using merged

# Before state
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 10.200.16.10/24;
#         }
#     }
# }
# ge-0/0/2 {
#     description "non configured interface";
#     unit 0;
# }

- name: Merge provided configuration with device configuration (default operation is merge)
  junos_l3_interfaces:
    config:
      - name: ge-0/0/1
        ipv4:
           - address: 192.168.1.10/24
        ipv6:
           - address: 8d8d:8d01::1/64
      - name: ge-0/0/2
        ipv4:
           - address: dhcp
    state: merged

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 10.200.16.10/24;
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     description "L3 interface with dhcp";
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }


# Using overridden

# Before state
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 10.200.16.10/24;
#         }
#     }
# }
# ge-0/0/2 {
#     description "L3 interface with dhcp";
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# ge-0/0/3 {
#     description "another L3 interface";
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#     }
# }

- name: Override provided configuration with device configuration
  junos_l3_interfaces:
    config:
      - name: ge-0/0/1
        ipv4:
           - address: 192.168.1.10/24
        ipv6:
           - address: 8d8d:8d01::1/64
      - name: ge-0/0/2
        ipv6:
           - address: 2001:db8:3000::/64
    state: overridden

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     description "L3 interface with ipv6";
#     unit 0 {
#         family inet6 {
#             address 2001:db8:3000::/64;
#         }
#     }
# }
# ge-0/0/3 {
#     description "overridden L3 interface";
#     unit 0;
# }


# Using replaced

# Before state
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 10.200.16.10/24;
#         }
#     }
# }
# ge-0/0/2 {
#     description "non configured interface";
#     unit 0;
# }
# ge-0/0/3 {
#     description "another L3 interface";
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#     }
# }

- name: Replace provided configuration with device configuration
  junos_l3_interfaces:
    config:
      - name: ge-0/0/1
        ipv4:
           - address: 192.168.1.10/24
        ipv6:
           - address: 8d8d:8d01::1/64
      - name: ge-0/0/2
        ipv4:
           - address: dhcp
    state: replaced

# After state:
# ------------
#
# admin# show interfaces
# ge-0/0/1 {
#     description "L3 interface";
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#         family inet6 {
#             address 8d8d:8d01::1/64;
#         }
#     }
# }
# ge-0/0/2 {
#     description "L3 interface with dhcp";
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# ge-0/0/3 {
#     description "another L3 interface";
#     unit 0 {
#         family inet {
#             address 192.168.1.10/24;
#         }
#     }
# }


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.junos.argspec.l3_interfaces.l3_interfaces import L3_interfacesArgs
from ansible.module_utils.network.junos.config.l3_interfaces.l3_interfaces import L3_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',)),
                   ('state', 'overridden', ('config',))]

    module = AnsibleModule(argument_spec=L3_interfacesArgs.argument_spec,
                           required_if=required_if,
                           supports_check_mode=True)

    result = L3_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
