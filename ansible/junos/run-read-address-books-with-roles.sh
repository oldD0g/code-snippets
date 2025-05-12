#!/bin/bash
#
#
#
env ANSIBLE_ROLES_PATH="${ANSIBLE_ROLES_PATH}:~/dev/ansible/roles" ansible-playbook \
  --extra-vars "@/home/ivan/ansible/junos-fw01.yml" \
   --extra-vars "{config_output: /tmp}" \
   --extra-vars "{debug_enabled: True}" \
   --extra-vars "{output_path: .}" \
  --inventory ~/dev/ansible/inventory.yml \
  --limit junos-fw01 \
  ~/dev/ansible/playbook.yml
