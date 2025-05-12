#!/usr/bin/python

import ast


class FilterModule(object):
    def filters(self):
        return {
            'json2setBGP': self.json_to_set_bgp_commands
        }

    def json_to_set_bgp_commands(self, json_config, prefix):
        """
          This converts JSON as returned from a 'parsed' module state into
          set commands for the SRX firewall. As the JSON does not contain
          a full configuration, the command prefix is passed in so that
          each command can be prefixed with the correct information.

        """

        def do_bgp_neighbor(grp_name, nb, prefix):

            nb_address = nb.get('neighbor_address') or 'UNKNOWN-ADDRESS'

            prefix = f"{prefix} neighbor {nb_address}"

            nb_cmds = []

            for attr, val in nb.items():
                if attr != 'neighbor_address' and attr != 'description':
                    nb_cmds.append(f"{prefix} {attr.replace('_','-')} {val}")
                elif attr == 'description':
                    nb_cmds.append(f"{prefix} {attr} \"{val}\"")

            return nb_cmds

        def do_bgp_group(group_entry, prefix):
            """
            Process a BGP group entry in JSON format
            """

            grp_cmds = []
            grp_name = group_entry.get('name') or 'UNKNOWN-GROUP'
            for attr, val in group_entry.items():
                if isinstance(val, str) and attr != 'name':
                    if attr != 'description':
                        grp_cmds.append(f"{prefix} "
                                        f"{attr.replace('_','-')} {val}")
                    else:
                        grp_cmds.append(f"{prefix} {attr} \"{val}\"")

                if attr == 'neighbors':
                    for nb_entry in val:
                        grp_cmds.extend(do_bgp_neighbor(grp_name, nb_entry,
                                                        prefix +
                                                        ' group ' + grp_name))

            return grp_cmds

        cmd_list = []
        # The supplied JSON is sometimes of type AnsibleUnsafeText and cannot
        #  be used directly.
        # Using ast.literal_eval after casting it to a string seems to work OK.
        bgp_conf = ast.literal_eval(str(json_config))

        for attr, val in bgp_conf.items():
            if attr == 'groups':
                for grp_entry in val:
                    cmd_list.extend(do_bgp_group(grp_entry, prefix))
            elif isinstance(val, str):
                cmd_list.append(f"{prefix} {attr.replace('_','-')} {val}")

        return cmd_list
